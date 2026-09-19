# SABLE-001 independent verification pilot

This original harness tests the separately assigned [SABLE issue #54](https://github.com/socksninja/sable-agent-reliability/issues/54). Codex-assisted implementation is disclosed and was explicitly accepted by the requester. The fee is contingent on requester acceptance; this package is not evidence of payment.

## Scope

Pin AgentScope-Java **2.0.1**, source commit `51d10ecfddadc45fb2173ff161e40e7bcf48d0be` (the peeled `v2.0.1` release tag). The exact hash has been proposed to the requester; no response to that clarification is assumed.

Build the actual upstream runtime without changing tracked source. Inject only an independent test into the OpenAI extension test directory. The test starts an HTTP server bound to `127.0.0.1` on an ephemeral port and runs three isolated sessions:

1. **Normal control:** HTTP 200, harmless content marker, finish chunk, `[DONE]`. Require one request, a delivered reply, and the same persisted assistant text from a separate JVM.
2. **Retry control:** HTTP 429 on the first request, then the normal response. Require exactly two requests and the same delivered/persisted marker. This checks that the configured retry path is operative.
3. **DONE-only:** HTTP 200 with exactly `data: [DONE]\n\n`. Observe terminal signal, delivered messages, request count and fresh-read persisted output without assuming the bug reproduces.

Each session configures `maxAttempts=3`, uses the actual JDK HTTP transport, `OpenAIChatModel`, `ReActAgent.call`, and `JsonFileAgentStateStore`. Credentials and data are synthetic. The fresh-reader JVM deserializes the framework's saved state; it does not share the parent's in-memory state. No fallback model is configured, so this experiment makes no fallback-specific claim.

## Reproduce

Requirements: Git, Python 3.9+, JDK 17, Maven 3.9+. Set `JAVA_HOME` to your JDK. Initial Maven dependency retrieval needs network access; the actual model requests go only to the local stub. Do not set production credentials.

```sh
python run.py --source /path/to/isolated/agentscope-java --output /path/to/new/run
python verify.py /path/to/new/run
```

Use `--maven /absolute/path/to/mvn` (or `mvn.cmd` on Windows) if Maven is not on PATH. The source directory may be absent, in which case the runner clones the release; an existing checkout must match the exact commit and have no tracked changes. The output directory must not already exist. The runner uses empty Maven user/global settings, runs only `SablePilotTest`, and retains the build log.

Successful execution writes `provenance.json`, `evidence/summary.json`, per-case raw HTTP traces, fresh-read results, framework state files where written, and `SHA256SUMS.json`. The manifest covers every JSON evidence file except itself. It proves byte consistency, not third-party attestation or payment. Local `reader.args`, logs and build paths are excluded from the public evidence package.

## Classification

- **VERIFIED:** both controls pass, DONE-only completes without error, produces no delivered/persisted assistant output, and makes exactly one request despite the configured retry allowance.
- **NOT VERIFIED:** both controls pass, but the DONE-only observation does not meet all those conditions.
- **EVIDENCE GAP:** positive controls fail or execution cannot provide the required observations. A build failure is not a non-reproduction.

Evidence only applies to this exact revision, local synthetic responses, transport and call/persistence path. It does not establish production prevalence, provider behavior, severity, or behavior in all AgentScope versions. This is SABLE-001 zero-chunk completion, not SABLE-002 mid-stream replay.
