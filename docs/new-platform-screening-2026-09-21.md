# 新平台筛选（2026-09-21）

## OnlyDust

[现行条款](https://www.onlydust.com/terms)第5.3节明确资助为酌情决定，不承诺逐任务补偿；[Fellowship说明](https://docs.onlydust.com/contributors-hiya/onlydust-fellowship)依据贡献历史选拔。适合作为长期贡献路线评估，当前没有本人的任务预算或资助批准，不把历史教程中的“做PR就领钱”当现行付款安排。未注册或申请资助。

## IssueHunt

[官方首页](https://issuehunt.io/)说明奖励可经银行/PayPal处理；[公开项目列表](https://issuehunt.io/programs)区分Bug Bounty和无奖励承诺的VDP。

具体读取 [New Innovations coffee API](https://issuehunt.io/programs/d219fa72-0aec-4e5b-9130-73d1e22192d9)：

- 奖励：Informational 0–5,000 JPY；Low 5,000–10,000；Medium 10,000–30,000；High 30,000–100,000；Critical 100,000–300,000。金额是严重度区间，不是已获奖励。
- 公开范围为该移动端咖啡服务的指定生产REST API，不包括任意关联系统。
- 需要满足年龄、关联关系及地区等资格并同意平台/项目条款。项目禁止影响服务、接触他人账号、提取他人隐私或仅提交未经分析的扫描结果。
- 当前只有规则核查，没有目标测试、账号注册、漏洞发现或报告；没有提现资格或奖励保证。

## Mermail 开发竞赛

[官方项目页](https://superteam.fun/earn/listing/build-and-demo-a-mermail-agent-skill/)仍显示开放投稿、Global。Sponsor评论将截止日更新至2026-10-07 13:59 UTC（北京时间21:59），预计10月11日宣布结果。

总奖池500 USDC，第一名250、第二名100，其余三个名次各50。核查时139份投稿；列表的27是评论数，不能误记为竞争作品数。

要求英文SKILL.md公开PR、2–5分钟真实运行演示视频发布到X并标记官方账号，以及所用AI客户端说明。属于按质量等条件评奖的竞赛，并非每个合格交付都会付费。没有提交或获奖。


### Mermail 实施门槛与当前进度

[免费计划](https://docs.mermail.app/resources/plans.md)提供1个inbox、1个API key、每周期1,000 credits和10 RPM。[认证说明](https://docs.mermail.app/api-reference/authentication.md)规定workspace在登录Console时创建，不能匿名经API新建workspace；API key或OAuth仍然必需。创建隔离inbox据[官方说明](https://docs.mermail.app/ai/agent-email-inbox.md)消耗10 credits。Free quota是服务额度，不是收入；并不需要钱包交易来演示inbox。

已只读克隆[官方技能仓库](https://github.com/Nudgen-Marketing/mermail-skills)，基线commit `269a711bf683845d75009df4984bf25eee83b0bd`，读取贡献、作者、安全及测试要求。拟研究“把指定测试邮件生成脱敏可重放回归样例”的小范围技能，尚未编写代码或提交PR。现有收件工具已有官方所有者，实施前需选择不重复工具所有权的扩展/路由方式，遵守贡献路径；真实演示还需要账户授权，完整参赛还需X视频和平台提交。未发起注册、API调用或对外推广。

2026-09-21 后续：用户确认两个账号都没有，故降为备选。没有继续投入实现或注册；这项竞赛不能替代已确认的付费任务。本地基线 npm test 因 Windows CRLF 与校验器要求 LF 不匹配而失败，未修改仓库。该检查不算投稿或有偿交付。

## 恢复后的新入口核查

2026-09-21 14:39（北京时间），公开来源只读核查；没有对外申请或付款。

| 来源 | 可核实结果与决定 |
| --- | --- |
| [GitWork](https://gitwork.io/) | 官网仅显示项目暂停。此前第三方推荐不能当作当前可用平台。 |
| [DeskCrew 当前任务 API](https://deskcrew.io/api/arena/contests) | 返回1项开放任务 ticket381；bountyUsd=1、netRewardUsd=0.85、toolPriceUsd=0.06、winner-take-all、payoutNetwork=algorand、tool-fee-not-refundable。平台自报历史付款未经本轮链上独立核实。未进入付费竞争。 |
| [Rocket Pool 第41轮](https://dao.rocketpool.net/t/round-41-gmc-call-for-bounty-applications-deadline-is-october-7/4045) | 征集新的悬赏定义，10月7日截止、10月25日预计宣布结果；此页不是已获批任务清单，不投未经研究的泛化资助申请。 |
| [Mova Store #440](https://github.com/Movalabs-crew/mova-store/issues/440) | 开放issue列表仅一条他人的1,190 USDC结算请求，无评论；文字不是支付证明，也不是我方可承接任务。贡献规则要求先在GrantFox申请并获确认。 |
| [Lilly #577](https://github.com/Lilly-Protocol/lily-sdk/issues/577) | 他人已合并工作的90美元结算请求；其中另一作者发了无关草稿PR，原作者明确说明此处只处理付款。未联系或实现。 |
| [Vista #61](https://github.com/Mantitup-Org/vista/issues/61) | 有缺陷征集范围，未列现金金额；现有评论已询问现金/署名奖励之别，没有维护者付款答复。本轮不再叠加同样问题，也不据此指控欺诈。 |
| [MisakaNet #1942](https://github.com/Ikalus1988/MisakaNet/issues/1942#issuecomment-5754457260) | Opire机器人明确称尚无奖励；安装器/验证要求更新不代表资金获批。[#1945](https://github.com/Ikalus1988/MisakaNet/issues/1945#issuecomment-5750905802)则已有维护者实现。未运行安装器、提交或索酬。 |

GrantFox的[奖励规则](https://docs.grantfox.xyz/key-concepts/rewards.md)明确：贡献通过验收不保证付款，OSS奖励通常活动结束后评审，受预算、维护者推荐和平台审批影响，可能减少或拒绝。[申请流程](https://docs.grantfox.xyz/user-manual-guides/oss-contributions-guide/contributor-guide/applying-to-issues.md)要求被选中分配后开工。[钱包规则](https://docs.grantfox.xyz/key-concepts/wallets-and-payments.md)要求Stellar钱包可接收相应资产、设置USDC trustline且不依赖memo。未注册或设置钱包；不能把GitHub金额标签、合并数量或索款总额当作平台确认应付金额。

搜索工具说明：第一次gh search组合查询返回空列表，随后改用GitHub search/issues API取得候选；不据第一次空结果断言没有开放任务。以上结论只覆盖列明来源，不代表所有市场机会已穷尽。
