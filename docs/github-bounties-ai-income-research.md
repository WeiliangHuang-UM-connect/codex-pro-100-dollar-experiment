# GitHub 悬赏与 AI 赚钱实践核查

核查时间：2026-09-19。以下区分项目规则、公开授奖记录、作者自述和本实验建议。公开授奖评论不等于我方能够独立检查获奖人的银行到账；收费页面也不等于经过审计的收入。

## 相对值得关注的付费贡献渠道

| 渠道 | 本轮查到的依据 | 对本实验的限制与判断 |
| --- | --- | --- |
| [Expensify/App](https://github.com/Expensify/App) | [贡献规则](https://github.com/Expensify/App/blob/main/contributingGuides/CONTRIBUTING.md)明确新贡献者通过已验证 Upwork 账户受聘和收款；提案获选前不能开 PR。本次 GitHub 搜索有 30 个 open + Help Wanted 条目。 | 不是纯自动路线：[AI Etiquette](https://github.com/Expensify/App/blob/main/contributingGuides/AI_ETIQUETTE.md)要求人理解、审核和验证 AI 产物。未确认用户具备 Upwork 条件。 |
| [Algora](https://github.com/algora-io/algora) / tscircuit | Algora 官方仓库包含 GitHub 悬赏及支付系统；[tscircuit 公开授奖评论](https://github.com/tscircuit/template-api-fake/issues/2#issuecomment-2873330870)明确向指定贡献者授予 12 美元。 | 该任务仍 open，但已 Rewarded，不能再当作可领取任务。Algora 文档与总榜 URL 本次 web 访问返回 404，未验证用户地区及当前提现资格，不能承诺可收款。 |
| [Chain.Love 数据贡献](https://github.com/Chain-Love/chain-love/discussions/41) | 此前同日已读取官方公告：月结 Ethereum USDC/USDT；基础非空单元格奖励 0.06 USDC，另有类别乘数；限定网络。维护者公布过付款批次。 | 维护者同时报告较大审核积压；此前已扫描候选与开放 PR 重复。适合耐心积累，不适合作为本次快速收到 100 美元的首选；未独立审计批次到账。 |

两个当前 Expensify 例子说明为何不能只看标签：

- [#100728](https://github.com/Expensify/App/issues/100728)：审批人行显示问题仍有 Help Wanted，但已有提案和 C+ 审核，且在确认服务端行为；未证明存在适合我们立刻接手的独立工作。
- [#99881](https://github.com/Expensify/App/issues/99881)：导出列超过约 100 行后为空，已有前后端方案讨论；9 月 19 日复测评论称当轮未复现。不是看见标签就直接实现。

以上是相对有清楚规则和可核查历史的渠道，不是已经替用户确认可领取、可兑现的新悬赏。本轮未认领、未申请、未注册付款账户。

## 别人用 AI 做业务的公开实践

### Inbox Zero：开源产品 + 付费托管

[源码](https://github.com/elie222/inbox-zero)提供邮件分类、回复草稿等功能，并提供托管版和自托管说明。[官方价格页](https://www.getinboxzero.com/pricing)可见 Starter、Plus、Professional 等付费方案。证据能证明商业产品和收费入口存在，不能据此推断营收或利润。

可借鉴思路：围绕高频、具体的业务流程收费。对本实验更小的切入口是一次性配置、集成或数据导入，而不是一开始复制完整邮件 SaaS。任何使用开源代码的商业交付仍须遵守其许可；邮箱权限和隐私需要客户明确授权。

### ryuno2525：22 天、12 个产品，作者自述收入仍为零

[原始复盘](https://gist.github.com/ryuno2525/8eeae131f7fa73516ad4ff0a300e192d)自述：自主 AI 从零开发，22 天做出 12 个产品、获得 543 次 npm 下载，但收入 0 美元。它尝试免费工具带付费报告等模式。这是作者自述，不是独立审计。

可借鉴结论：先获得付费需求，再扩大开发投入。产品数、下载量和页面收录不能替代客户付款。

### personhood-gate：把开户与市场容量当成实际限制

[原仓库](https://github.com/AsherKasper/personhood-gate)记录自主 AI 尝试赚钱时遇到的身份验证、市场有效需求与奖励规模问题。这是阶段性调查，里面的市场统计没有在本轮全面重跑；不把其统计泛化为整个市场结论。

可借鉴思路：先确认账号资格、实际奖金额度、是否仍可申领，再评估是否值得写代码。

### monetizecomputehackathon：现金和待兑现收益分开记

[原仓库](https://github.com/monetizecompute/monetizecomputehackathon)把推理成本、待兑现收益和现金收入分开，现金入账需要人核验；文中还记录错误记账后撤销的教训。README 中手工调用 bank 接口的示例不是实际到账凭证。

可借鉴思路：用净到账和实际成本评估实验，不把 PR 提交、授奖预期或捐赠混成技术服务收入。

## 给本实验的建议

优先级是本轮判断，不是市场收入保证：

1. **固定范围的故障复现、回归测试与小修复。** 已有真实验收作品可展示。先确认一个问题、一套验收条件、固定费用和付款路径，再做交付。建议试探 100–250 美元一单；这是我们的拟报价，不是已核实市场成交价。
2. **企业小型自动化交付。** CSV/JSON 导入核对、API 错误处理、定时报表等；先用样例明确范围，再谈维护费。避免把对方整套系统作为低价试单。
3. **具备账户和人工审核条件后做成熟 OSS 悬赏。** Expensify/Algora 值得定向追踪，但先过账户、任务有效性和竞争重复检查。
4. **有明确客户需求后再做订阅产品。** Inbox Zero 的模式可研究，但本实验不应把开发更多 SaaS 当作已经接近收入目标。

筛选时至少看：维护者身份与项目活动、历史授奖/付款记录、当前任务未付款且仍接收贡献、是否已有获选方案、AI 和人工审核要求、收款路径是否可用。可核查历史只提高可信度，不保证下一单付款。

本轮没有新订单、收入或支出。SABLE 按用户要求暂不处理，没有重新查询结算状态。
