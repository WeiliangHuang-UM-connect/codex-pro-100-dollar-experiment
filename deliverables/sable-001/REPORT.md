# SABLE-001: VERIFIED within the tested boundary

**The DONE-only HTTP 200 case completed normally without an assistant reply, without a persisted assistant message, and without a retry. Both positive controls passed.** This is an independently executed observation, not a restatement of the upstream issue.

[Successful public CI run](https://github.com/WeiliangHuang-UM-connect/codex-pro-100-dollar-experiment/actions/runs/35435203603) · [Structured summary](observed-run/evidence/summary.json) · [SHA-256 manifest](observed-run/SHA256SUMS.json) · [Execution provenance](observed-run/provenance.json)

## Observed result

Execution completed on 2026-09-19. CI used Ubuntu 24.04 and Temurin Java 17.0.20.1. The tested upstream release is **AgentScope-Java 2.0.1**, source commit [`51d10ecfddadc45fb2173ff161e40e7bcf48d0be`](https://github.com/agentscope-ai/agentscope-java/tree/51d10ecfddadc45fb2173ff161e40e7bcf48d0be). The harness/runner used by CI are pinned by hashes in the provenance file and by CI checkout `fdee95738ea394fda267b13dc58e37d5255e9aa4`.

| Case | HTTP responses | Requests / retries | Call termination | Delivered assistant messages | Fresh JVM persisted assistant messages |
|---|---|---:|---|---:|---:|
| Normal control | 200, content + finish + DONE | 1 / 0 | onComplete, no exception | 1 | 1; exact harmless marker |
| Retry control | 429, then normal 200 | 2 / 1 | onComplete, no exception | 1 | 1; exact harmless marker |
| DONE-only | 200, exactly `data: [DONE]\n\n` | 1 / 0 | onComplete, no exception | 0 | 0; state file absent |

Every case configured `maxAttempts=3`. The 429 control establishes that the real request retry path was active. The DONE-only case never entered it. For the empty case, `state_present=false` is reported explicitly: the reader did not find an empty assistant message; it found no persisted state file. Each case used a fresh state directory. Separate reader PIDs and raw JSON files are preserved.

## Acceptance evidence

| Agreed item | Evidence |
|---|---|
| Pin version and source revision | Runner checks exact Git HEAD and refuses tracked source changes before/after execution; provenance records the revision. The peeled release-tag hash was also proposed to the requester in a [follow-up](https://github.com/socksninja/sable-agent-reliability/issues/54#issuecomment-5740746506). A reply approving that exact hash is not assumed. |
| Local OpenAI-compatible HTTP stub with DONE-only and normal control | Original [Java harness](SablePilotTest.java), actual JDK HTTP transport, per-case `http-trace.json` containing method, path, synthetic request and exact response body/status. |
| Request/retry counts and terminal signal | Per-case `result.json`, cross-checked against HTTP trace counts. |
| Persisted assistant output | Framework `JsonFileAgentStateStore` JSON files for both positive controls; no file for DONE-only. |
| Fresh-read from separate process | New JVM calls the framework's state deserializer and writes `fresh-read.json`; reader and parent process IDs differ. The offline verifier independently checks the persisted JSON content too. |
| Reproducible harness and machine-readable evidence | [Instructions](README.md), [runner](run.py), all synthetic [observations](observed-run), and manual CI workflow. No paid model calls or production credentials. |
| SHA-256 manifest | Every evidence JSON file is checked against `SHA256SUMS.json`; executed harness/runner hashes are checked too. |
| Scoped classification | VERIFIED for this exact local HTTP / call / persistence path. |

## Review and reproduce

Run the offline integrity/consistency check from this directory:

```sh
python verify.py observed-run
```

Follow [README.md](README.md) to independently rebuild and rerun against the pinned source. CI logs also contain the exact evidence bytes as base64 records prefixed `SABLE_EVIDENCE_FILE`; the published JSON files were decoded from those logs and verified locally. The CI result is tied to the linked run and checkout, not merely to a screenshot of a green badge.

The manifest is an integrity check, not a third-party signature. This package does not prove behavior on production gateways, frequency, provider prevalence, other revisions, or other call paths. No fallback model was configured, so no fallback-specific behavior is claimed. SLF4J reported no logging provider; the result relies on observed calls, exceptions, HTTP requests and persisted state, not on a claimed absence of warning logs. SABLE-002 mid-stream replay is outside scope.

## Execution history and payment

Local Windows run-001 failed to start its test JVM because of system memory commitment limits. After lowering the initial heap, run-002 completed with the same three-case observations. After hardening timeout handling, run-003 encountered a child JVM native-memory allocation failure. Those failed executions are environment gaps, not non-reproductions. The final attached evidence comes from the successful current-harness CI run, not from combining partial failed runs.

AI/Codex-assisted implementation and testing were disclosed and accepted by the requester. The requester confirmed US$250 contingent on acceptance and specified PayPal. A Base USDC alternative has been requested; it is not yet agreed. Publication/delivery of this evidence does not establish acceptance, an escrow balance, or payment. Verified receipts remain US$0.
