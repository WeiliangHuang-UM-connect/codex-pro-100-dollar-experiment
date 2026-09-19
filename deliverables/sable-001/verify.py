"""Check evidence consistency without network access or executing framework code."""
import hashlib
import json
from pathlib import Path
import sys


def verify(root):
    root = root.resolve()
    manifest = json.loads((root / "SHA256SUMS.json").read_text(encoding="utf-8"))
    assert manifest, "Empty manifest"
    for name, expected in manifest.items():
        path = (root / name).resolve()
        assert path.is_relative_to(root), "Manifest escapes evidence root"
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, name
    actual_json = {p.relative_to(root).as_posix() for p in root.rglob("*.json")
                   if p.name != "SHA256SUMS.json"}
    assert set(manifest) == actual_json, "Unmanifested or missing evidence JSON"
    summary = json.loads((root / "evidence/summary.json").read_text(encoding="utf-8"))
    provenance = json.loads((root / "provenance.json").read_text(encoding="utf-8"))
    assert summary["revision"] == provenance["source_revision"] == "51d10ecfddadc45fb2173ff161e40e7bcf48d0be"
    assert provenance["tracked_runtime_modifications"] is False
    for key, name in [("harness_sha256", "SablePilotTest.java"), ("runner_sha256", "run.py")]:
        assert hashlib.sha256((Path(__file__).parent / name).read_bytes()).hexdigest() == provenance[key]
    checks = {}
    for case in summary["cases"]:
        name = case["scenario"]
        assert name not in checks, "Duplicate case"
        folder = root / "evidence" / name
        assert case == json.loads((folder / "result.json").read_text(encoding="utf-8"))
        fresh = json.loads((folder / "fresh-read.json").read_text(encoding="utf-8"))
        assert fresh == case["fresh_process_read"]
        assert fresh["reader_pid"] != case["parent_pid"]
        assert fresh["assistant_count"] == len(fresh["assistant_texts"])
        state_files = list((folder / "state").rglob("agent_state.json")) if (folder / "state").exists() else []
        assert len(state_files) == int(fresh["state_present"])
        if state_files:
            state = json.loads(state_files[0].read_text(encoding="utf-8"))
            assert state["user_id"] == "synthetic-user" and state["session_id"] == "synthetic-session"
            stored = ["".join(b["text"] for b in m["content"] if b["type"] == "text")
                      for m in state["context"] if m["role"] == "ASSISTANT"]
            assert stored == fresh["assistant_texts"]
        trace = json.loads((folder / "http-trace.json").read_text(encoding="utf-8"))
        assert len(trace) == case["http_request_count"]
        assert case["http_retries_observed"] == max(0, len(trace) - 1)
        assert case["configured_max_attempts"] == 3
        for i, request in enumerate(trace, 1):
            assert request["request_number"] == i
            assert request["method"] == "POST"
            assert json.loads(request["request_body"])["stream"] is True
        if name == "done-only":
            assert all(t["response_status"] == 200 and t["response_body"] == "data: [DONE]\n\n" for t in trace)
            checks[name] = (case["terminal_signal"] == "onComplete" and not case["call_exception"]
                            and len(trace) == 1 and not case["delivered_assistant_texts"]
                            and not fresh["assistant_texts"])
        else:
            expected = [429, 200] if name == "retry-control" else [200]
            checks[name] = (case["terminal_signal"] == "onComplete" and not case["call_exception"]
                           and [t["response_status"] for t in trace] == expected
                           and case["delivered_assistant_texts"] == ["SABLE_LOCAL_CONTROL_OK"]
                           and fresh["state_present"] is True
                           and fresh["assistant_texts"] == ["SABLE_LOCAL_CONTROL_OK"])
    assert set(checks) == {"normal-control", "retry-control", "done-only"}
    controls = checks["normal-control"] and checks["retry-control"]
    empty = next(c for c in summary["cases"] if c["scenario"] == "done-only")
    incomplete = not controls or empty["terminal_signal"] == "NOT_OBSERVED"
    classification = "EVIDENCE GAP" if incomplete else "VERIFIED" if checks["done-only"] else "NOT VERIFIED"
    assert summary["controls_passed"] == controls
    assert summary["classification"] == classification
    print(json.dumps({"integrity": "PASS", "classification": classification, "case_checks": checks}, indent=2))


if __name__ == "__main__":
    verify(Path(sys.argv[1]))
