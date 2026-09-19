# SABLE 独立验证付费申请（买方已确认并分配）

[已发评论](https://github.com/socksninja/sable-agent-reliability/issues/54#issuecomment-5740676507)。SABLE 的 #86–#91 任务已有其他受派者，其中 #86 的维护者明确确认 250 美元及 PayPal 收款；不代表本申请已有预算。

本次向尚未分配的 #54 提出独立验证方案，报价 250 美元、范围和分配确认后 48 小时，优先询问 Base USDC。该需求原本没有已确认的付费承诺，因此必须等待预算、AI 辅助资格、任务分配和收款渠道确认。尚未执行主实验。

核对发现其当前链接的 THIRD_PARTY_REPRO_CHECKLIST.md 讲 SABLE-002 流中重试，与 #54 的 SABLE-001 空流不同；申请明确区分。

## 后续确认

[维护者回复](https://github.com/socksninja/sable-agent-reliability/issues/54#issuecomment-5740699385)确认 250 美元验收后付款、48 小时、AI/Codex 辅助符合资格，Issue 已分配给本账号。指定 PayPal，用户收款可用性尚未确认。前面的预算未确认段落保留为申请时的历史记录。实际到账 0 美元。

目标截止时间按买方 2026-09-19 09:14:01 UTC 回复推算为 2026-09-21 17:14:01（Asia/Shanghai）。v2.0.1 发布标签解析为 51d10ecfddadc45fb2173ff161e40e7bcf48d0be；精确版本尚需对齐，主实验尚未执行。

## 完整申请

Would you consider funding this still-unassigned zero-chunk case as a separate independent verification pilot? I see #86-#91 are already assigned and am not claiming those tasks.

Proposed scope: pin AgentScope-Java 2.0.1 (and the exact source revision agreed with you); use a local OpenAI-compatible stub for a DONE-only HTTP 200 stream plus a normal-content control; record request/retry counts, terminal signal and persisted assistant output; fresh-read the harmless output from a separate process; deliver a reproducible harness, raw machine-readable evidence, SHA-256 manifest and a scoped VERIFIED / NOT VERIFIED / EVIDENCE GAP report. No production endpoint, credential or paid model call would be needed.

One scope detail: the current THIRD_PARTY_REPRO_CHECKLIST.md describes SABLE-002 mid-stream replay, while this issue concerns SABLE-001 zero-chunk completion. I would test the latter directly rather than treat the linked replay test as evidence for it.

My proposal is US$250 fixed with a 48-hour delivery target after assignment and the exact acceptance boundary are confirmed. Please confirm whether this separate task has budget, whether disclosed Codex/AI-assisted implementation and testing are eligible, and the supported payout rail. USDC on Base is preferred; if PayPal is the only option, please state that before we agree terms. No receiving credentials/details need to be posted publicly.

This is an application and scope inquiry, not a claim of reproduction or completion; I would begin the main execution after your confirmation.


## 技术交付

已完成并[提交验收](https://github.com/socksninja/sable-agent-reliability/issues/54#issuecomment-5740828522)。完整 [REPORT.md](../deliverables/sable-001/REPORT.md) 及固定版本 CI、14 个 JSON 证据文件均已公开。目标问题在测试边界内 VERIFIED。尚未获买方验收或收到款项。
