"""Build the pinned upstream source and run only the independent local-HTTP probe."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

REVISION = "51d10ecfddadc45fb2173ff161e40e7bcf48d0be"
MODULE = Path("agentscope-extensions/agentscope-extensions-model/agentscope-extensions-model-openai")
HERE = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--maven", default="mvn")
    args = parser.parse_args()
    source, output = args.source.resolve(), args.output.resolve()
    if output.exists():
        raise SystemExit("Output must not already exist; choose a fresh directory.")
    if not source.exists():
        subprocess.run(["git", "clone", "--depth", "1", "--branch", "v2.0.1",
                        "https://github.com/agentscope-ai/agentscope-java.git", str(source)], check=True)
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True).strip()
    if revision != REVISION:
        raise SystemExit(f"Unexpected revision: {revision}")
    # Refuse modified tracked runtime source, even when it would make the probe pass.
    subprocess.run(["git", "diff", "--exit-code", "HEAD", "--"], cwd=source, check=True)
    output.mkdir(parents=True)
    java = HERE / "SablePilotTest.java"
    dest = source / MODULE / "src/test/java/io/agentscope/extensions/model/openai/SablePilotTest.java"
    if dest.exists() and dest.read_bytes() != java.read_bytes():
        raise SystemExit("A different probe already exists at the injection path.")
    shutil.copyfile(java, dest)
    settings = output / "empty-settings.xml"
    settings.write_text('<settings xmlns="http://maven.apache.org/SETTINGS/1.2.0"/>', encoding="utf-8")
    command = [args.maven, "-B", "-ntp", "-s", str(settings), "-gs", str(settings),
               "-pl", ":agentscope-extensions-model-openai", "-am", "-Dspotless.skip=true",
               "-Djacoco.skip=true", "-DargLine=-Xms32m -Xmx256m", "-Dtest=SablePilotTest", "-Dsurefire.failIfNoSpecifiedTests=false",
               f"-Dsable.output={output / 'evidence'}", "test"]
    provenance = {"source_url": "https://github.com/agentscope-ai/agentscope-java", "source_revision": revision,
                  "tracked_runtime_modifications": False,
                  "harness_sha256": hashlib.sha256(java.read_bytes()).hexdigest(),
                  "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (output / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    with (output / "build.log").open("w", encoding="utf-8") as log:
        result = subprocess.run(command, cwd=source, stdout=log, stderr=subprocess.STDOUT)
    subprocess.run(["git", "diff", "--exit-code", "HEAD", "--"], cwd=source, check=True)
    evidence = output / "evidence"
    if result.returncode != 0:
        print(f"Build/probe failed ({result.returncode}). Inspect {output / 'build.log'}.")
        return result.returncode
    summary = json.loads((evidence / "summary.json").read_text(encoding="utf-8"))
    # Include only machine-readable evidence; omit local command arguments and reader logs.
    manifest = {p.relative_to(output).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(output.rglob("*.json"))}
    (output / "SHA256SUMS.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"classification": summary["classification"], "output": str(output)}, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
