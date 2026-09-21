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
