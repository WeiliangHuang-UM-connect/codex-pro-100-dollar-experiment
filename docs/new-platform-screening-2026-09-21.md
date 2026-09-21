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
