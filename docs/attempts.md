# 尝试清单

核验日期为 2026-09-19。下表是当时的结果，不是对平台永久状态的判断。所有路线的本实验实际收入均为 0。

## 已执行到开发、提交或联系阶段

| 路线 | 实际动作 | 结果与下一步 |
| --- | --- | --- |
| BountyBook：5 USDC Dijkstra | 编写算法；通过平台公开用例及自编独立对照测试；完成钱包登录；四次真实认领与提交 | 四次均被拒绝；任务重新开放，未付款。停止对同一任务继续试错，不换钱包绕过次数限制。见[脱敏结果](../evidence/bountybook-attempts.json)。 |
| Ubiquity：75 + 37.50 美元任务 | 查明当前账户不具备协作者资格；经用户批准发送一次资格询问，披露 AI 辅助 | [询问已发布](https://github.com/ubiquity-os-marketplace/daemon-disqualifier/issues/135#issuecomment-5740218566)。截至最新日志没有回复或分配，未提交代码。 |
| LaborX：250 美元等值视频剪辑 | 核验具体需求；准备申请；用户批准后点击 Send | 页面进入注册而非成功页。用户用 Google 注册；Google 登录可后接 MetaMask，但当前申请尚未确认送达。见[原任务](https://laborx.com/jobs/video-biography-edit-104737)。 |
| CSV 自动化服务样例 | 实现多表合并、金额核对、重复与异常保留、来源追踪；四个测试通过 | [样例代码](../examples/csv-orders)仅用于演示，不是客户交付或收入。 |
| OpenCollective API 安全检查 | 克隆源码并阅读贡献约束；局部检查文件权限、导出与 PDF 获取逻辑 | 没找到可复现且符合条件的漏洞。未探测线上服务、未提交报告，也不能将局部检查描述为完整安全审计。 |

LaborX 申请范围：约 8 分钟视频、250 美元等值、素材和需求确认后 15 天、一次约定范围内修改、披露 AI 辅助，并询问通过平台托管以 Base USDC 结算。买方尚未同意；素材权利、具体风格及托管资金都未落实。

## 已核验但未进入交付的候选

| 候选 | 观察到的门槛或排除理由 | 来源 |
| --- | --- | --- |
| Chain.Love 数据贡献 | 月结、基础单元格奖励很低；扫描 594 个开放 PR、129 份相关补丁后，所选方向已有重叠。部分字段归自动化所有，不能拿来凑工作量。未提交 PR。 | [奖励讨论](https://github.com/Chain-Love/chain-love/discussions/41) |
| Claude builders 100 美元 hook | 大量竞争评论和既有交付，未投入重复开发。 | [任务](https://github.com/claude-builders-bounty/claude-builders-bounty/issues/3) |
| Invidious 小额修复 | 小任务已有竞争；项目对 AI 沟通和人工验证有明确限制，不适合本次全自主路线。 | [任务](https://github.com/iv-org/invidious/issues/1898)、[AI 规则](https://github.com/iv-org/invidious/blob/master/AI_POLICY.md) |
| Tenstorrent 500 美元 uint8 | 已指定其他贡献者，且需要本环境没有的硬件验证。 | [任务](https://github.com/tenstorrent/tt-metal/issues/56290) |
| Expensify | 需要已验证 Upwork 账户，先批准提案再开发。本次没有对应账户条件。 | [贡献说明](https://github.com/Expensify/App/blob/main/contributingGuides/CONTRIBUTING.md) |
| Spare Cycles | 平台积分不能视为可提现现金。 | [仓库](https://github.com/mxx1111/spare-cycles) |
| 讯飞教程悬赏 | 维护者说明金额为占位，现金奖励未确认。 | [任务](https://github.com/iflytek/astronclaw-tutorial/issues/17) |
| AgenticCPS 1,000 元 | README 示例不是有效现金委托。 | [任务](https://github.com/zhuangpengLI/AgenticCPS/issues/1) |
| 支付宝 AI 付激励 | 资源包奖励不计为本实验现金收入，还依赖真实业务条件。 | [活动](https://aipay.alipay.com/incentive-mobile) |
| tscircuit / Algora | 一个标价任务对应仓库与 API 为 404；另一个任务大量 claim，未确认新参与者付款机会。 | [悬赏列表](https://algora.io/tscircuit/bounties) |
| Web3insight | 现金范围、收款方式、验收条件尚缺维护者确认。 | [讨论](https://github.com/web3insight-ai/web3insight/issues/32) |
| 程序员客栈 | 派单有签约认证要求；部分款项支持支付宝不能泛化成所有订单。准备草稿但未入驻或申请。 | [FAQ](https://support.proginn.com/qa/)、[签约要求](https://support.proginn.com/outsource/coder-sign/) |
| MoonBit 九月黑客松 | 官方说明的阶段支持需审核、入群和成果验收；不能当作保证收入。尚未报名，单个 500 元支持也未证明达成目标。 | [活动](https://moonbitlang.github.io/Hackathon2026/) |
| Arrow-air 750 美元里程碑 | 要求已有社区参与经历，未取得参与资格。 | [任务](https://github.com/Arrow-air/project-quiver/issues/252) |
| Memanto 100 美元 | 历史记录将其归为获胜者奖励、包含推广评分，未按固定付款工作推进。 | 本地记录仅保留名称与编号，完整原始链接未恢复；该条不作为读者可独立复核的确证。 |
| Movalabs | 评论中的高金额未付款陈述不能当作平台可靠付款证明。没有认领。 | [任务](https://github.com/Movalabs-crew/mova-store/issues/434) |
| Frantic | 本次看到的任务以付费服务测试、推广为主，另有登录条件，未注册或垫付。 | 依据本地保存的当时任务列表，未公开整份响应 |
| V2EX 设计与前端外包 | 有具体需求，但预算、加密货币付款和当前是否缺人均未确认；CSV 作品与该需求匹配度低。未联系。 | [原帖](https://www.v2ex.com/t/1240655) |
| 其他中文平台 | 部分已接单，部分需付费会员才能沟通，部分没有明确预算。未把服务商广告当作买方订单。 | [中文核验摘要](retrospective.md#找订单的成本) |
| MoltJobs | 声称支持 Base USDC 托管；当时官方接口访问失败，论坛报告不能代替独立核验。未找到已确认可接的技术买方任务。 | [平台](https://moltjobs.io/) |
| TaskBounty（公开仓库发布后的新尝试） | 官方宣传支持 USDC 和代码任务；实际 GET 任务接口返回 data 空数组，未筛选的浏览页也无匹配任务。未注册或提交。 | [任务 API](https://www.task-bounty.com/api/v1/tasks)、[任务页](https://www.task-bounty.com/browse)、[续跑证据](../evidence/continuation-2026-09-19.json) |
| 其他 Web3 候选 | 已关闭的任务、卖家的服务报价、不可提现积分、提示词泄露诱饵、要求无法证明的指定模型使用记录，均未当作可执行订单。 | 本地历史核验记录；未对无确切原始链接的条目补造引用 |

## 证据层级

“看到一个广告” → “确认参与资格” → “得到任务/合同” → “提交并通过验收” → “实际到账”，每一步分开记。上表数量不等于投递量，更不等于成交量。
