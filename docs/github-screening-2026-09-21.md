# GitHub 悬赏筛选 — 2026-09-21

用户暂时无法登录 Upwork，明确要求继续寻找 GitHub 悬赏。本轮没有新申请、PR、获批委托或收入；以下是当次核验结果。

| 候选 | 核验结果与决定 |
| --- | --- |
| [Expensify #100728](https://github.com/Expensify/App/issues/100728#issuecomment-5723486385) | 审核者已认可既有提案方向，尚需确认服务端 AddMembersToWorkspace 行为。没有另发重复方案。 |
| [Expensify #99927](https://github.com/Expensify/App/issues/99927#issuecomment-5694055839) | 多份提案在审，已有贡献者提供测试分支；本轮没有独立复现或差异化方案。 |
| [JHipster 官方悬赏](https://www.jhipster.tech/bug-bounties/) | 规则要求赏金标签、核心成员合并和 OpenCollective 报销，说明 PayPal 结算；主仓库开放赏金标签查询为空。页面较旧，未把通用规则当成具体新委托。 |
| [Control Center #174](https://github.com/jhipster/jhipster-control-center/issues/174) | $500 旧任务，已有多个实现和回归测试；近期多次可用性询问没有维护者新确认。不追加同类询问或实现。 |
| [Vue #482](https://github.com/jhipster/jhipster-vuejs/issues/482) / [#431](https://github.com/jhipster/jhipster-vuejs/issues/431) | $100 旧任务。前者有维护者批准的接手记录；后者维护者指出上游 Sonar 问题。没有确认当前剩余付费范围。 |
| [Algora / tscircuit](https://algora.io/tscircuit/bounties) | 浏览器 Open 显示 10 条，但 dsn-converter #54 重复出现多个金额，不能算 10 个独立订单。该题 236 claims；jlcsearch #92 有 103 claims。历史完成数不是本实验收款证据。 |
| [pgstrap #2](https://github.com/seveibar/pgstrap/issues/2) | 平台仍列 $30，但近期已有多份实现、测试和申请；没有复制贡献。 |
| [Tarsnap 规则](https://www.tarsnap.com/bugbounty.html) | 小于 $100 的奖励仅为 Tarsnap 账户额度；$100 起可选美元支票。当前未建立支票收款条件，也没有原创合格漏洞，故没有将小额代码修补作为现金路线。 |
| [Omi 贡献规则](https://github.com/BasedHardware/omi/blob/main/docs/doc/developer/Contribution.mdx) | 允许 AI 辅助并要求实际验证；一般贡献奖励包含设备与转录额度，不等于现金。Paid Bounty 标签仅返回三个设备功能任务；未建立硬件验证条件。 |
| [Omi #6792](https://github.com/BasedHardware/omi/issues/6792) | Spotify 播放列表问题已有贡献者复现及集成仓库 PR #5，提出的 $10 尚未获维护者批准。本轮不重复提案。 |
| [Omi #5097](https://github.com/BasedHardware/omi/issues/5097) | $100 来自第三方评论，不是已核验维护者预算；已有他人询问实际资助者和范围。未据此开发。 |
| [Omi #11680](https://github.com/BasedHardware/omi/issues/11680) | 原题涉及缺失删除队列和重试风暴。本轮只读源码，发现主分支已加入队列存在性探测和失败记录退避；未检查生产、执行删除或声称仍能复现。没有提出重复修复报价。 |

Omi 源码观察：`backend/utils/cloud_tasks.py` blob `39188249e7b4efcf1bc6f6c823c38058ef13ee7f` 的配置验证调用 `assert_account_deletion_queue_exists`；`backend/database/users.py` blob `59328c6fd7b39c0f979eba2e146a6b96f9ce663c` 的待重试筛选使用失败时间与 `deletion_wipe_retry_delay`。这些仅证明相应代码已存在，不证明线上故障已解决或整个实现无误。没有读取生产数据。

近期标题搜索还返回大量自动汇总帖和贡献者自报赏金建议；未将标题金额记为批准预算。上述工作是筛选，不是新交付。Upwork 草稿仍未发送；原等待清单不变，到账仍为 0。


## 新增渠道复核

- [AsyncAPI 官方规则](https://www.asyncapi.com/docs/community/010-contribution-guidelines/microgrant-program)优先维护者，分配后才接受对应任务贡献。开放标签查询返回四项：[website#5704](https://github.com/asyncapi/website/issues/5704)、[parser-js#1203](https://github.com/asyncapi/parser-js/issues/1203)、[optimizer#306](https://github.com/asyncapi/optimizer/issues/306)已分配；[training#65](https://github.com/asyncapi/training/issues/65#issuecomment-4717602707)虽然仍 open，但原轮次已完成且发票获确认，未当作新任务。
- [Mudlet](https://github.com/Mudlet/Mudlet/issues)：本次分别查询开放 bounty-100、bounty-200、bounty-50、bounty-120，均为空；未推断其他标签或未来任务情况。
- [qmrkt/contracts#5](https://github.com/qmrkt/contracts/issues/5)：原有每个合格漏洞 100 USDC 的承诺，但当前 issue 已关闭且 [PR #9](https://github.com/qmrkt/contracts/pull/9)已合并。没有作为开放悬赏继续研究，也未核实其他人的实际收款。
- [maxstern.org /book 旧 gist](https://gist.github.com/Mxcks/f0dcbf6ac8a7c3f5c0195d704b9458ac)：索引出现 $150–200，实时 gist 及评论 API 均为 404，预算、分配和付款状态不可核验。不据摘要开发或发送申请。

本轮没有新申请或交付。尚无已获分配、可直接开发的新付费范围；现有申请需要外部回复。到账仍为 0。


## Archestra 定向核查

通过[官方贡献文档](https://archestra.ai/docs/contributing)确认仓库，再以 GitHub API 读取两条第三方列表线索：

- [#3556 Notion connector](https://github.com/archestra-ai/archestra/issues/3556)：维护者曾出价 $100，当前已关闭、分配给他人且带 Rewarded 标签；[PR #3555](https://github.com/archestra-ai/archestra/pull/3555)已合并。不当作仍开放任务。
- [#3378 Schedule triggers](https://github.com/archestra-ai/archestra/issues/3378)：维护者曾出价 $500，当前已关闭且正文指定贡献者；原 [PR #3432](https://github.com/archestra-ai/archestra/pull/3432)已关闭未合并。不据此推断任务重新开放。

官方贡献规则要求先完成 onboarding，允许 AI 辅助但需审查和测试，禁止对已经分配的悬赏提交竞争 PR 或 attempt。本轮无申请。


## Omnigres 计划关闭

[官方 Bounties wiki](https://github.com/omnigres/omnigres/wiki/Bounties)顶部明确表示悬赏计划已关闭，其余说明仅为历史记录。未根据旧金额标签申请或开发。


## Permify 与 Tailcall 收尾核查

| 候选 | 来源与当前结论 |
| --- | --- |
| Permify #837 | [任务](https://github.com/Permify/permify/issues/837)已被维护者关闭为 completed，历史 $250 不是新任务。 |
| Permify CLI #2 | [任务](https://github.com/Permify/permify-cli/issues/2)仍 open，主分支有功能缺口，但[官方 Algora 板](https://algora.io/Permify/bounties)显示 Open 0 / Completed 13。[分配规则](https://github.com/Permify/permify-cli/issues/2#issuecomment-1846793379)要求先取得确认，当前没有新分配或预算确认。 |
| Tailcall 移动 Lighthouse #217 | [任务](https://github.com/tailcallhq/tailcallhq.github.io/issues/217)已于 2026-07-13 关闭、not_planned；Algora 仍列为 open，不能单靠挂牌判断。 |
| Tailcall rust-grpc #44 | [原任务](https://github.com/tailcallhq/rust-grpc/issues/44)仍 open/unassigned，有[历史 $50 出价](https://github.com/tailcallhq/rust-grpc/issues/44#issuecomment-2506754276)；[当前挂牌](https://algora.io/tailcallhq/bounties)仍在。开价后的可用性询问未见维护者回复，main 最后提交为 2024-12-03；[最新 #86](https://github.com/tailcallhq/rust-grpc/pull/86)仍无评审。当前受理与付款资格未核实，不认定已获委托，也不断言悬赏撤销。 |

旧 Algora 机器人付款文档链接目前无法访问，未确认本人的澳门收款资格或支付轨道。存在其他提案并不是自动排除条件；本轮实际缺少的是当前受理、分配或可兑现预算的证据。没有新增申请或 PR。
