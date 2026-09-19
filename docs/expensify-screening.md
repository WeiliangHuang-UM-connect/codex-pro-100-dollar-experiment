# Expensify 现金悬赏筛选

查询时间：2026-09-19 20:06（Asia/Shanghai）。这是候选评估，不是接单或交付记录。

## 资格和实际流程

用户已确认拥有完成身份验证的 Upwork 账户；随后已提供公开个人主页链接；本实验尚未独立查看账户或验证提现。公开页面读取工具未能访问该链接，这不证明账户有问题。[官方贡献规则](https://github.com/Expensify/App/blob/main/contributingGuides/CONTRIBUTING.md)要求新贡献者经 Upwork 受聘、付款，GitHub 方案获选后再办理聘用，不能提前开 PR。发布到生产后还有至少 7 天回归观察期，新贡献者一次只做一单。投入调查时间本身不保证报酬。

[AI Etiquette](https://github.com/Expensify/App/blob/main/contributingGuides/AI_ETIQUETTE.md)允许 AI 辅助，但要求人理解、审核和验证产物。[MelvinBot 流程](https://github.com/Expensify/App/blob/main/contributingGuides/HOW_TO_WORK_WITH_MELVINBOT.md)优先审核其机器人提案；外部方案需有实质差异。当前没有待用户审核的成熟提案，也没有声称完成人工审核。

## 本轮候选结论

精确搜索 `repo:Expensify/App is:issue is:open label:"Help Wanted"` 返回 30 项。取得各项全部评论页，再按审核意见、既有方案和测试条件筛选。不是对 30 项源代码逐一复现，也不是对付款记录的独立审计。

| 任务 | 可核查现状 | 当前判断 |
| --- | --- | --- |
| [#99450 搜索混入刚创建的费用](https://github.com/Expensify/App/issues/99450) | [审核者仍在评估](https://github.com/Expensify/App/issues/99450#issuecomment-5578540536)；已有参与者提交测试和浏览器验证说明 | 技术方向贴近能力，但未发现有依据的不同方案；不能复制已有提案抢单 |
| [#99927 工作区引导任务未完成](https://github.com/Expensify/App/issues/99927) | [内部工程师要求重新评审](https://github.com/Expensify/App/issues/99927#issuecomment-5694055839)，已有多种方案和测试分支 | 可研究，尚无差异化方案或本实验复现证据 |
| [#99763 收据伙伴邀请页底部留白](https://github.com/Expensify/App/issues/99763) | 曾选中方案，因提交早于 Help Wanted 重新评审；[审核者表示相似提案过多](https://github.com/Expensify/App/issues/99763#issuecomment-5686398293) | 表面小修复；实际涉及原生安全区、Uber for Business 连接及重复方案，暂不投入 |
| [$250 #96419 保存搜索后合计未出现](https://github.com/Expensify/App/issues/96419) | [审核者认为已选方案可以实现](https://github.com/Expensify/App/issues/96419#issuecomment-5221412568)，仍等内部审核 | 不作为空缺新单 |
| [$250 #96135 通勤扣除距离单位](https://github.com/Expensify/App/issues/96135) | [审核者等待内部输入](https://github.com/Expensify/App/issues/96135#issuecomment-5694009167)，涉及服务端持久化和单位语义 | 需求决策未定，不能只改显示标签 |
| [#100728 审批人行缺失](https://github.com/Expensify/App/issues/100728) | [Melvin 方案已获初步认可，但服务端行为待确认](https://github.com/Expensify/App/issues/100728#issuecomment-5723486385) | 已有先行方案和实现前阻碍 |
| [$250 #97013 里程收据错误](https://github.com/Expensify/App/issues/97013) | [审核者建议原贡献者继续已有工作](https://github.com/Expensify/App/issues/97013#issuecomment-5697830614) | 不当作无人接手 |
| [#98674 草稿重现](https://github.com/Expensify/App/issues/98674)、[$250 #91581 自动退出](https://github.com/Expensify/App/issues/91581) | 审核者近期均认为无法复现并建议关闭 | 不凭旧标题开发 |

另排除 Skip Payment/HOLD 项及依赖受限后端、特殊设备或尚未具备测试条件的工作。上述是本次投入优先级判断，不表示所有其他参与者均不能接单。标题未列金额的任务未擅自写成 250 美元。

## 下一步可执行条件

Upwork 公开主页已取得，可用于后续聘用资料。公开发提案之前，需要用测试账户复现、确认与已有方案的实质差异、准备所需平台验证，并让用户实际审阅 AI 辅助产物。当前未满足这些条件，因此没有对外发送占位申请。

相比先花大量时间竞争已有方案的小修复，本实验仍更适合利用已验收的故障复现作品争取固定范围的测试/排错委托。此为投入判断，尚无新增买方或成交。
