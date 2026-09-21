# 尝试清单

**2026-09-21 更正：SABLE 历史约定 250 美元、已验收未到账；原付款评论已改为历史／已取代模式说明，当前无新结算确认，用户已要求停止跟进。以下带日期记录保留当时观察，不代表现时付款承诺。详见[核查证据](../evidence/sable-status-2026-09-21.json)。**

核验日期为 2026-09-19。下表是当时的结果，不是对平台永久状态的判断。所有路线的本实验实际收入均为 0。

## 已执行到开发、提交或联系阶段

| 路线 | 实际动作 | 结果与下一步 |
| --- | --- | --- |
| BountyBook：5 USDC Dijkstra | 编写算法；通过平台公开用例及自编独立对照测试；完成钱包登录；四次真实认领与提交 | 四次均被拒绝；任务重新开放，未付款。停止对同一任务继续试错，不换钱包绕过次数限制。见[脱敏结果](../evidence/bountybook-attempts.json)。 |
| Ubiquity：75 + 37.50 美元任务 | 查明当前账户不具备协作者资格；经用户批准发送一次资格询问，披露 AI 辅助 | [询问已发布](https://github.com/ubiquity-os-marketplace/daemon-disqualifier/issues/135#issuecomment-5740218566)。截至最新日志没有回复或分配，未提交代码。 |
| LaborX：250 美元等值视频剪辑 | 核验需求并准备申请；用户批准后完成注册、内置浏览器登录与必填资料；实际发送 | **已成功提交**。My Jobs 显示完整申请文案、250 美元预算和 15 天工期；待买方回复。见[原任务](https://laborx.com/jobs/video-biography-edit-104737)及[提交观察记录](../evidence/laborx-application.json)。 |
| CSV 自动化服务样例 | 实现多表合并、金额核对、重复与异常保留、来源追踪；四个测试通过 | [样例代码](../examples/csv-orders)仅用于演示，不是客户交付或收入。 |
| LaborX CSV 固定范围服务 | 将现有样例整理成 120 USDC、3 天、一次修改的服务；上传原创合成数据封面，选择 Base USDC，经用户明确批准后发布 | 刷新页面后明确显示 Published；[服务页面](https://laborx.com/gigs/i-will-clean-merge-and-validate-csv-files-with-a-python-script-122168)与[具体文案](laborx-csv-gig-draft.md)。尚无客户、合同或收入。 |
| OpenCollective API 安全检查 | 克隆源码并阅读贡献约束；局部检查文件权限、导出与 PDF 获取逻辑 | 没找到可复现且符合条件的漏洞。未探测线上服务、未提交报告，也不能将局部检查描述为完整安全审计。 |

LaborX 申请范围：约 8 分钟视频、250 美元等值、素材和需求确认后 15 天、一次约定范围内修改、披露 AI 辅助，并询问通过平台托管以 Base USDC 结算。买方尚未同意；素材权利、具体风格及托管资金都未落实。

## 已核验但未进入交付的候选

| 候选 | 观察到的门槛或排除理由 | 来源 |
| --- | --- | --- |
| Chain.Love 数据贡献 | 月结、基础单元格奖励很低；扫描 594 个开放 PR、129 份相关补丁后，所选方向已有重叠。部分字段归自动化所有，不能拿来凑工作量。未提交 PR。 | [奖励讨论](https://github.com/Chain-Love/chain-love/discussions/41) |
| Claude builders 100 美元 hook | 大量竞争评论和既有交付，未投入重复开发。 | [任务](https://github.com/claude-builders-bounty/claude-builders-bounty/issues/3) |
| Invidious 小额修复 | 小任务已有竞争；项目对 AI 沟通和人工验证有明确限制，不适合本次全自主路线。 | [任务](https://github.com/iv-org/invidious/issues/1898)、[AI 规则](https://github.com/iv-org/invidious/blob/master/AI_POLICY.md) |
| Tenstorrent 500 美元 uint8 | 已指定其他贡献者，且需要本环境没有的硬件验证。 | [任务](https://github.com/tenstorrent/tt-metal/issues/56290) |
| Expensify | 需要已验证 Upwork 账户，先批准提案再开发。早期未确认账户；20:06 用户已确认 Upwork 验证并提供主页，仍需具体任务复现与方案审核。 | [贡献说明](https://github.com/Expensify/App/blob/main/contributingGuides/CONTRIBUTING.md) |
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
| BasedAgents | 官方说明有 Base USDC 任务，但付款需买方验收后签名；公开状态和任务接口本次均返回 HTTP 403，未能核实具体可接订单。没有安装凭证管理工具、注册或领任务。 | [官方机器说明](https://basedagents.ai/.well-known/agent.json) |
| 其他 Web3 候选 | 已关闭的任务、卖家的服务报价、不可提现积分、提示词泄露诱饵、要求无法证明的指定模型使用记录，均未当作可执行订单。 | 本地历史核验记录；未对无确切原始链接的条目补造引用 |

## 发布后的新增筛选

| 候选 | 实际核验与决定 |
| --- | --- |
| [CoinGecko bot reliability](https://laborx.com/jobs/enhance-coingecko-bot-reliability-96610) | 标价 300 美元，原截止日 2025-09-24；统一发送授权后已发一份 300 美元 / 5 天的条件申请，先确认需求仍在。My Jobs 核实提交；没有买方接受，未写交付代码。[文案](coingecko-reliability-application.md)。 |
| [Community Calendar Manager](https://laborx.com/jobs/community-calendar-manager-content-curator-104725) | 近期广告，实际每周 100 美元 BTC、持续至少 3 个月，需视频面试与人工持续值守；未承诺参与。 |
| [Data Operations & Product Engineer](https://laborx.com/jobs/data-operations-amp-product-engineer-102259) | 旧岗位，同一买方近期仍发需求。经用户批准已提交单独 150 美元 CSV 导入试单询问，My Jobs 核实完整申请及 3 天工期；尚未获买方接受或分配；[全文](data-import-pilot-application.md)。 |

另核查 [Need Flutter Developer](https://laborx.com/jobs/need-flutter-developer-103477)：70 美元，截止日 2026-07-10，缺具体修复项；未申请或承诺交付。

## 新渠道的资金与资格核验

| 渠道 | 实际结论 |
| --- | --- |
| [Open Bounty](https://openbounty.app/llms.txt) | 官方说明明确是公共测试网，不是主网真实付款服务；未注册或交付。 |
| [Handsel](https://github.com/Kairose-master/handsel/blob/main/docs/agent-integration.md) | 主网要求 0.00005 ETH gas 下限，认领另需 5% + 0.03 USDC 保证金；未充值或认领。 |
| [OpenWitness](https://www.openwitness.net/api/listings/guide) | 公开指南与列表接口本次 GET 返回 HTTP 403，未核实可接任务。 |
| [sum() 5 USDC 示例](https://github.com/priyanshudotsol/bounty-demo/issues/1) | 明确 Base Sepolia 测试网奖励，不能计作真实收入，未提交。 |
| [x402-mcp #495](https://github.com/kwizzlesurp10-ctrl/x402-mcp/issues/495)、[#496](https://github.com/kwizzlesurp10-ctrl/x402-mcp/issues/496) | 维护者的条款要求对方向其指定地址付钱，再由运营者交付，不能直接解读为给外部贡献者付悬赏；也已有他人提交。未付钱、认领或重复交付。 |
| [librarian-mcp JSONL](https://github.com/liana-banyan/librarian-mcp/issues/1) | 已有多份实现和待确认付款条件，未重复争抢或签署 grant。 |
| [SABLE #54](https://github.com/socksninja/sable-agent-reliability/issues/54) | 其他明确标价 250 美元的任务均已分配；向这项未分配、未确认预算的需求提交独立 250 美元方案，等待明确答复。[申请及证据](sable-verification-application.md)。 |

## 后续资格筛选

- [ArcNS #51](https://github.com/khenzarr/arcns/issues/51)：10 USDC、无保证金，但明确 human-only；未申请。
- [qtop #551](https://github.com/qtop/qtop/issues/551) 与 [#530](https://github.com/qtop/qtop/issues/530)：PoH、身份挑战及现场解释；#530 另有限定地区学生/研究人员要求，未建立用户资格，未认领。
- [Pinax #17](https://github.com/pinax-network/substreams-evm-extended/issues/17)：离线实现已有进展，实时访问仍暂停，未读到对应赏金承诺；未当作付费工作。
- [Opire 公共列表](https://app.opire.dev/home) 可读，但本用户的付款渠道和领取资格仍未验证。卡片金额不是到账保证。
- LaborX 的 `fix` 搜索返回 48 条，当前检查未找到新的、资格与付款都确认的短任务；没有批量申请旧广告。

## 证据层级

“看到一个广告” → “确认参与资格” → “得到任务/合同” → “提交并通过验收” → “实际到账”，每一步分开记。上表数量不等于投递量，更不等于成交量。


### SABLE 后续：买方确认与正式分配

2026-09-19T17:21:10+08:00 按用户邮件提示核查：[维护者确认](https://github.com/socksninja/sable-agent-reliability/issues/54#issuecomment-5740699385) 250 美元验收后付款，48 小时交付目标，允许 AI/Codex 辅助；Issue 已分配给本账号。指定 PayPal，收款可用性待用户确认。主实验未运行，实际到账 0。此前“预算未确认”是当时观察，不再代表当前状态。


### SABLE 已完成技术交付，等待验收

2026-09-19T17:43:54+08:00，本地真实 HTTP 复现程序完成，最终当前版本在 [Ubuntu CI](https://github.com/WeiliangHuang-UM-connect/codex-pro-100-dollar-experiment/actions/runs/35435203603) 成功。空流 1 请求 / 正常结束 / 无输出，两个正对照通过；由独立 JVM 检查持久化结果。已[正式提交买方验收](https://github.com/socksninja/sable-agent-reliability/issues/54#issuecomment-5740828522)。PayPal 未确认可用，USDC 替代方案已询问但未获同意；交付和 250 美元承诺均不算到账。


### SABLE 验收通过，进入结算

2026-09-19T17:50:49+08:00 核实[买方验收](https://github.com/socksninja/sable-agent-reliability/issues/54#issuecomment-5740835884)：250 美元固定费用应付；到账仍为 0。已询问私下联系渠道，PayPal 是原约定，Base USDC 尚未获批准。此前“待验收”是当时状态，现已被本次回复更新。


### 验收后的候选核查

2026-09-19 17:54：qmrkt 赏金已关闭，NSPG13 #894 未注资，DeskCrew 要求预付参赛费用，Collaborators 未核实到具体可接任务。无新增申请或到账；[来源与观察](../evidence/post-acceptance-screening.json)。


### SABLE 结算推进

2026-09-19T19:00:05+08:00：按用户明确指示，通过 Gmail 私下发送 PayPal 收款信息，已读取 SENT 记录核实；[GitHub 已告知](https://github.com/socksninja/sable-agent-reliability/issues/54#issuecomment-5741269484)。等待付款，未新增到账。


### SABLE 付款状态澄清

2026-09-19T19:11:22+08:00：用户报告 PayPal 显示付款，已按要求[询问买方付款方向及状态](https://github.com/socksninja/sable-agent-reliability/issues/54#issuecomment-5741344483)。尚无直接 PayPal 界面证据或到账证据，不将用户观察直接判定为转账错误。


### SABLE：付款方向已澄清

2026-09-19T19:18:00+08:00：[买方确认未发起付款或付款请求](https://github.com/socksninja/sable-agent-reliability/issues/54#issuecomment-5741369194)，250 美元仍应付。已在原私下邮件线程重申用户提供的收款邮箱，公开留言告知查收；尚未到账。


### 等待清单复查

2026-09-19 19:35，按用户要求复查 Ubiquity 与四项 LaborX 事项，均无新回复或订单。SABLE 本轮不处理；无新增对外申请或催问。详见[等待清单](waiting-list.md)。


### GitHub 付费贡献与 AI 业务研究

2026-09-19 19:38，新增[核查笔记](github-bounties-ai-income-research.md)。相对成熟渠道仍需满足身份、付款和人工审核条件；没有将历史授奖或他人收入自述记为本实验进展。没有新申请或收入。

### 新增 SQLite 任务条件申请

2026-09-19 19:53，在 LaborX 向 [SQLite API 买方](https://laborx.com/jobs/simple-server-to-serve-as-access-for-my-sqlite-database-103220)发送 50 美元 / 1 天条件申请，首先确认 6 月的旧需求是否仍有效。My Jobs 核实全文和金额工期；未获接受、未签合同或开发。详见[文案](sqlite-api-application.md)。本轮 GitHub 新候选筛选结果见[补充笔记](github-bounties-ai-income-research.md#本轮继续筛选2026-09-19-1953)。


### Upwork 资格更新及 Expensify / Gitpay 深筛

2026-09-19 20:06：用户确认 Upwork 已验证；读取 Expensify 规则并筛选 30 个开放 Help Wanted 条目及全部评论页。没有已复现、与现有方案实质不同且适合马上提交的候选，未发提案。Gitpay 的公开 API 查询 open + hasBounty 返回 0 项。详见[筛选记录](expensify-screening.md)；申请、收入与应收金额不变。


### Tenstorrent 官方付费任务询问

2026-09-19 20:14：向官方悬赏邮箱发送无专用硬件的小型测试/工具修复任务询问，附已验收作品并披露 AI 辅助；Gmail SENT 和正文已读回核实。尚无任务分配、金额批准或收入。[接洽记录](tenstorrent-inquiry.md)。Upwork 浏览器导航/控制超时，本轮没有提交 Upwork 申请。


### Upwork CSV→Airtable 申请草稿

2026-09-19 20:19：核实公开 100 美元岗位，准备[针对性文案与验收计划](upwork-csv-airtable-draft.md)。尚缺已登录申请页、付款验证与 Connects 核查；未提交，未支出。


### 2026-09-21 GitHub 继续筛选

用户暂时无法登录 Upwork，要求继续 GitHub 路线。核查 Expensify、JHipster、Algora、Tarsnap 和 Omi，发现既有实现、未批预算或非现金奖励等限制；未新增申请、PR 或收入。Omi 旧题面提到的部分缺失在当前源码中已经补上。见[完整排除依据](github-screening-2026-09-21.md)。


本日后续又核查 AsyncAPI、Mudlet、qmrkt 和旧 /book 委托；未找到当前可认领范围。具体分配、关闭或无法访问证据见[筛选附录](github-screening-2026-09-21.md#新增渠道复核)。未新增申请或收入。


本日后续：向已验收的 SABLE 原委托发出[结算澄清](https://github.com/socksninja/sable-agent-reliability/issues/54#issuecomment-5756005190)，请求明确原 250 美元费用和付款日期。发布与正文已核实；未收到新承诺或到账。


本日收尾核查 Omnigres（计划关闭）、Permify 和 Tailcall，见[具体证据](github-screening-2026-09-21.md)。既有执行障碍连续存在，目标已标记 blocked；有买方回复、可靠新付费入口或账户恢复后再推进。目标未完成。


### 2026-09-21 停止 SABLE 跟进

按用户明确指示不再联系或主动检查 SABLE，已移出主动等待清单并保留历史证据。停止跟进不视为到账或放弃历史费用；本轮转向其他机会。


### 2026-09-21 新增 AI 项目试单申请

向 LaborX 的 joe guru 发送独立 150 美元/3 天的单缺陷复现与修复提案，完整文案及报价已在 My Jobs 核实。先确认 7 月旧需求仍有效、具体范围、AI 资格和托管资金，尚无成交或到账。见[申请记录](ai-project-pilot-application.md)。


### 2026-09-21 Whisper 小额悬赏资格询问

向 [ivrit-ai #12](ivrit-streaming-inquiry.md)发出一次100 NIS悬赏的锁定、AI代理异步评审与国际PayPal收款询问，留言已回读核实。未取得分配或开始实现，不把币种误记为美元。目标工具已恢复 active，实际到账0。


### 2026-09-21 新平台与通知评估

完成[OnlyDust、IssueHunt与Mermail候选核查](new-platform-screening-2026-09-21.md)，未新增申请或收入。按用户通知检查ivrit新评论：另一位投稿者的草稿PR，不是维护者给我方的任务锁定或付款确认；继续等待。[证据](../evidence/ivrit-reply-assessment-2026-09-21.json)。
