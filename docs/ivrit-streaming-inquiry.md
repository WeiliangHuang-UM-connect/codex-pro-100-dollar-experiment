# ivrit-ai Whisper 流式分析：资格与付款询问

状态：**已发出并回读核实；尚未分配、未开发、未验收、未到账。**

- 任务：[ivrit-py #12](https://github.com/ivrit-ai/ivrit-py/issues/12)。题面金额 **100 NIS**，不记为 100 美元。
- [官方规则](https://github.com/ivrit-ai/ivrit-py#bounty-rules)：先讨论并获得两周锁定；合并 PR 才支付；AI 可用但须解释实现，评审可能现场进行。
- 开放且无 assignee；创建于 2025-11-17。最新代码提交为 [2026-07-27](https://github.com/ivrit-ai/ivrit-py/commit/76cac007abbf3e4ab2bea9fc28495d583d8a7926)，不描述为近期活跃招聘。
- 未确认支付渠道、国际收款资格、资金托管、付款时间及完全异步评审资格。
- 技术范围只提出 CPU 小规模可复现分析；模型、合法可用的音频样例与验收指标需先确认，没有声称希伯来语人工评判经历。
- [已发留言](https://github.com/ivrit-ai/ivrit-py/issues/12#issuecomment-5756155596)，时间 2026-09-21T06:12:47Z；作者及全文回读一致。

## 已发文案

Hi @yairl — before claiming #12, could you confirm whether the advertised 100 NIS bounty is still available to reserve, whether it can be paid through PayPal to an international contributor after merge, and whether entirely asynchronous written review is acceptable for AI-agent-led work on behalf of this account's owner?

The proposed scope is a reproducible CPU probe of repeated transcribe() calls over overlapping audio windows, with word-confidence/stability measurements, focused analysis-helper tests, and a short report. I would first agree the model, permitted audio fixtures and acceptance criteria, then request the two-week lock under your rules. No availability, reservation or payment route is assumed, and I have not started implementation.

## 下一步条件

维护者确认任务、资格与支付方式后再锁定范围和实现。评审若需要用户本人讲解或现场参与，再明确告知所需协助；不虚构已经具备人工评审承诺。不重复催问，收到实际通知或用户查询后再检查。


## 2026-09-21 新通知评估

本轮定位到的GitHub新通知对应[spike-token的留言](https://github.com/ivrit-ai/ivrit-py/issues/12#issuecomment-5756227832)：另一位投稿者提交了[草稿PR #31](https://github.com/ivrit-ai/ivrit-py/pull/31)。该PR尚未合并且没有评审，Issue未分配。没有维护者给本账号的锁定或付款确认，继续等待。不能把竞争投稿当成接单成功，也不能据此认定诈骗。[核查摘要](../evidence/ivrit-reply-assessment-2026-09-21.json)。
