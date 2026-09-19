# Upwork CSV→Airtable 申请草稿（未发送）

观察时间：2026-09-19 20:19（Asia/Shanghai）。

[岗位：Python Workflow Automation Specialist](https://www.upwork.com/freelance-jobs/apply/Python-Workflow-Automation-Specialist_~022095503358934989865/)

公开页信息：100 美元固定价，Worldwide，客户需要 CSV 处理、字段映射、校验及 Airtable 更新；申请数 20–50，面试 0。这些数字可能变化，不能代替登录后的可申请状态、付款验证和 Connects 核查。尚未提交、受聘或收款。

## 拟填写内容

- 报价：100 美元固定价；这是岗位预算下的申请价，不是净到账预计。
- 工期：双方确认 CSV 样例、字段映射、匹配规则和运行方式、且里程碑托管资金落实后 3 天。
- 交付：Python 源码、配置示例、测试、运行说明、逐行异常报告；包含一轮约定范围内修改。
- 范围：单个 CSV→单个 Airtable 表的处理/更新流程。若实际任务包含多表关联、额外数据源或长期运维，应先对齐完整要求再决定报价，不能默默缩小客户需求。

## Cover letter

Hello,

The key to a dependable CSV-to-Airtable workflow is agreeing on the record-matching key and handling invalid or ambiguous rows before changing any records.

I would deliver a Python script with configurable field mapping, a dry-run preview, row-level validation errors, and a run summary. Updates would use the agreed unique key; unmatched rows, duplicate keys and blank-field handling would follow rules we confirm together. API calls would be batched and rate-limited, with bounded retries and explicit reporting of partial failures. Re-running the same file should not create unintended duplicates.

For the listed $100, I propose one CSV-to-one-table workflow, source code, tests, setup instructions and one in-scope revision, delivered within three days after the sample, mapping and funded milestone are agreed. Please share a redacted CSV sample, target field types, the matching key, approximate row count and desired run frequency so I can confirm that this covers the full requirement.

A runnable synthetic CSV reconciliation sample is available here:
https://github.com/WeiliangHuang-UM-connect/codex-pro-100-dollar-experiment/tree/main/examples/csv-orders
It demonstrates validation and traceable exception handling; it does not yet connect to Airtable.

Implementation and testing would use Codex assistance, with test results and any remaining limits documented. Credentials would stay in your environment and out of the source repository.

## 交付前拟验证内容

以下是拟验收计划，不是已通过测试：

1. 用约定样例验证字段映射、前导零 ID、日期/金额类型和空值规则。
2. 预览模式不发写请求；重复键与多记录匹配不能静默选择某条记录。
3. 测试正常批次、HTTP 429、验证错误、连接失败和部分批次成功；运行失败返回明确非零状态及结果汇总，不无限重试。
4. 客户允许的测试表进行端到端更新；重复输入按约定规则不产生额外记录。失败后的重跑需核对已成功批次，不声称外部 API 提供整文件原子事务。
5. token 由客户在自己环境中配置；仅授予必要 base/读写权限，日志不得包含 token。生产表更新另以客户确认的数据范围为准。

技术依据：[Airtable 请求限额](https://support.airtable.com/articles/7735693959-managing-api-call-limits-in-airtable)支持批量更新且有按 base 的速率约束；需分别处理短期限流与套餐月度额度。[PAT 权限说明](https://support.airtable.com/articles/9934989703-creating-personal-access-tokens)允许限定 scope 和 base。未连接客户数据，未申请或创建任何 token。

## 尚缺条件

登录 Upwork 后核实：岗位仍可申请、客户付款验证与招聘活动、所需 Connects、账户可用余额和最终显示的服务费。用户已确认账户通过身份验证并提供公开主页；这些不能替代已登录申请页。没有购买 Connects、Boost 或其他服务。
