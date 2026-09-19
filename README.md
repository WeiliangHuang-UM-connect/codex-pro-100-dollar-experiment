# 如何两天内烧完 Codex Pro 赚 100 刀

一份持续更新的真实实验记录：让 AI 自主寻找工作、完成交付，并尝试收到至少 100 美元。

**截至 2026-09-19，已核实到账：0 美元。目标未完成。**

最新进展：**SABLE 技术交付已获[买方明确验收](https://github.com/socksninja/sable-agent-reliability/issues/54#issuecomment-5740835884)，250 美元固定费用现已应付。** 记为应收未收，实际到账仍为 0。买方已确认尚未发起付款或付款请求；已在原私下邮件线程再次明确 PayPal 收款邮箱，等待实际转账。详见[交付报告](deliverables/sable-001/REPORT.md)和[验收证据](evidence/sable-acceptance.json)。

另已获用户批准并在 LaborX **公开发布 [120 USDC 的 CSV 自动化服务](https://laborx.com/gigs/i-will-clean-merge-and-validate-csv-files-with-a-python-script-122168)**；刷新后平台状态为 Published。收款选项为 Base USDC，尚无客户或到账。具体范围见[服务文案](docs/laborx-csv-gig-draft.md)。

后续进展：[150 美元数据导入试单申请](docs/data-import-pilot-application.md)已获用户批准并成功提交，My Jobs 显示完整文案、150 美元和 3 天工期；旧岗位是否仍有需求、是否接受独立试单，仍需买方确认。

标题来自实验发起者的推文选题。“两天”和“烧完 Pro”尚未由完整起止时间、额度快照或账单证实；“赚 100 刀”是目标，不是结果。本仓库不会把标价、申请、测试通过或平台返回 submitted 算成收入。

## 先看结果

| 项目 | 可核实状态 |
| --- | --- |
| 收入目标 | 累计实际到账至少 100 美元 |
| 已核实到账 | **0 美元** |
| 买方已确认的有偿委托 | 1：SABLE 已验收，250 美元应收未收；PayPal 收款资料已私下发送 |
| 真实平台交付尝试 | BountyBook 同一个 5 USDC 任务，4 次提交、4 次拒绝 |
| 已发出的资格询问 | GitHub 1 条，等待维护者回复 |
| LaborX 250 美元等值申请 | 已成功提交并在 My Jobs 核实；待买方回复，未成交 |
| LaborX 120 USDC 服务 | 已获批公开发布，平台状态 Published；未成交 |
| 新增直接支付支出 | 0；现有订阅及模型消耗未计价 |
| 是否完全无人介入 | 否，用户设置钱包、登录账户并确认具体对外申请 |

另已自动提交 [300 美元 Python 脚本修复申请](docs/coingecko-reliability-application.md)，明确先核实过期需求是否仍存在。19:53 新增 [50 美元 SQLite API 条件申请](docs/sqlite-api-application.md)，同样先确认旧需求和托管付款；当前 LaborX 共 4 份已核实提交的申请，均未确认成交。

最新进展：[SABLE 维护者已确认](https://github.com/socksninja/sable-agent-reliability/issues/54#issuecomment-5740699385) **250 美元验收后付款**并分配任务，允许 AI/Codex 辅助，48 小时交付目标。指定 PayPal，用户收款资料已私下发送；现已明确验收，250 美元应付但尚未到账。详见[申请与后续](docs/sable-verification-application.md)。

最新筛选未增加申请：ArcNS 仅限人类任务、qtop 身份及现场验证要求等已记录在[尝试清单](docs/attempts.md)。此筛选发生在 SABLE 确认回复被检查之前。

验收后的[候选筛选](evidence/post-acceptance-screening.json)未新增可执行订单；到账和应收金额未变化。

待回复事项集中在[等待清单](docs/waiting-list.md)。 9 月 19 日 19:35 按用户要求复查其余五项，均无新回复或订单；本轮未查询 SABLE。提交后继续寻找其他机会，收到查询或实际回复通知时再检查。

新增：[GitHub 悬赏与别人用 AI 做业务的核查](docs/github-bounties-ai-income-research.md)，包含可核查依据、账户门槛和适用路线。

20:06 更新：用户确认 Upwork 已完成验证；进一步[筛选 Expensify 的 30 个开放悬赏条目](docs/expensify-screening.md)，仍需解决任务竞争、复现和人工审核条件。本轮没有新申请或收入。

20:14 新增[Tenstorrent 官方付费任务询问](docs/tenstorrent-inquiry.md)，请求可用 CPU 环境完成的小型测试/工具修复任务；邮件已发送并核实，尚未获得任务或预算。

## 阅读顺序

- [推文串草稿](docs/thread-draft.md)：可直接取材，但尚未发到社交平台。
- [完整尝试清单](docs/attempts.md)：做了什么、卡在哪里、有没有提交。
- [过程复盘](docs/retrospective.md)：登录、协议、资格和成交的实际阻碍。
- [后续日志](docs/journal.md)：新尝试与状态变化按日期追加。
- [账本](data/ledger.json)：收入、支出和缺失指标。
- [脱敏证据](evidence/README.md)：原始来源、错误摘录与证据局限。
- [可运行代码](examples/README.md)：Dijkstra 与合成 CSV 清洗样例。
- [可承接的工作](SERVICES.md)：本实验的公开接单入口。

## 这次实际推进到哪里

1. 核验现金悬赏、开源任务、中文接单平台及加密货币任务；不少候选已有接手人、奖励不是现金，或存在账号与参与资格门槛。
2. 用户自行设置 MetaMask；完成地址格式检查与登录交接。钱包可用与订单可接是两件需要分别验证的事。
3. 为 BountyBook 的 5 USDC Dijkstra 任务完成算法及测试。钱包登录成功后，向平台实际提交了四次。两次返回代码行数错误，两次返回读取 undefined 的内部异常；没有验收或付款。
4. 向 Ubiquity 维护者发送一条获用户批准的资格询问，涉及标价 75 美元和 37.50 美元的两个任务。尚无授权分配。
5. 在 LaborX 找到 250 美元等值的 8 分钟人物传记剪辑需求，准备并获批申请。Chrome 控制故障后，用户改在 Codex 内置浏览器用同一账号登录；补齐必填资料后，申请已成功提交并核实。
6. 准备了一份 CSV 多表合并与异常核对演示，用于展示真实可交付能力。样例数据全部合成，没有客户成交记录。

## 更新与核验规则

每次有实质变化，更新后续日志、相关任务状态和账本，再提交 Git 记录。记录失败和撤回，不抹去旧判断；没有变化时不制造“新进展”。本仓库没有配置定时任务，更新发生在后续实际执行期间。

收入只在存在可核实到账证据后登记；USDC/USDT 先记代币数量和网络，不凭报价认定已收到美元。订阅成本、模型用量、人工耗时单独记录，缺失项保持 null，不按零处理。

公开内容来自本次对话、本地执行记录和注明来源的公开页面。平台规则与任务状态可能变化；历史核验不是当前参与资格的保证。

## 发布范围

这是经过整理的公开复盘，不是原始会话或工作目录的全量上传。未上传登录凭证、钱包私钥或助记词、个人收款地址、账户会话数据、完整第三方网页和无关研究项目。对外询问链接本身公开显示 GitHub 作者身份。
