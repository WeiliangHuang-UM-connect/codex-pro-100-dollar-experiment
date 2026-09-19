# 证据与局限

本仓库是公开摘要，不是司法取证包，也不是完整原始会话备份。

| 事实 | 支持材料 | 局限 |
| --- | --- | --- |
| 一条 GitHub 资格询问确实发出 | [公开评论](https://github.com/ubiquity-os-marketplace/daemon-disqualifier/issues/135#issuecomment-5740218566) | 发出询问不代表获得资格或任务 |
| BountyBook 四次拒绝 | [脱敏响应](bountybook-attempts.json) | 来自本地保存的认证 API 响应摘录；外部读者不能靠这个文件单独证明服务器历史状态 |
| Dijkstra 本地算法测试 | [代码与独立测试](../examples/dijkstra) | 本地通过不等于平台验收 |
| CSV 合并与核对能力 | [代码和合成用例](../examples/csv-orders) | 不是商业客户作品或成交证明 |
| LaborX 具体买方需求 | [任务页](https://laborx.com/jobs/video-biography-edit-104737) | 页面可变，标价不是托管入金 |
| LaborX 申请已成功提交 | [提交观察记录](laborx-application.json)，登录后 My Jobs 的对应申请卡片 | 属于助手观察摘要；该账号私有页面不对外公开，也不证明买方已经接受 |
| Google 注册可后接钱包 | [官方说明](https://laborx.com/blog/why-your-funds-are-safe-with-laborx)、[钱包功能说明](https://laborx.com/blog/release-1-6-0) | 文档较旧，当前菜单与账户绑定状态尚未实测 |
| 发布后继续核验新路线 | [续跑记录](continuation-2026-09-19.json)、[TaskBounty 公开任务 API](https://www.task-bounty.com/api/v1/tasks) | 公开列表为空只代表查询时可见结果，不代表永久无任务 |

日期来自对话日期、当地执行时钟及 API 记录。BountyBook 时间戳转换为 UTC；日志默认北京时间。

公开 JSON 只保留任务 ID、提交次数、时间、验收错误、任务和付款状态，移除了执行地址与尝试 ID。没有发布 API token、cookie、签名、nonce、浏览器会话或本机用户路径。没有把第三方完整任务响应、网页源码和仓库副本打包进来。

`code-sha256.json` 记录公开示例与本地原稿的字节哈希。它能检测文件是否一致，不能独立证明代码曾被平台接受或产生收入。


- [SABLE 交付记录](sable-delivery.json)：正式提交评论、固定交付版本与 CI 成功记录；不代表验收或到账。
- [SABLE 原始机器证据](../deliverables/sable-001/observed-run)：合成数据、真实本地 HTTP 调用和独立 JVM 读回结果，含 SHA-256 清单。


### SABLE 验收

[sable-acceptance.json](sable-acceptance.json) 记录买方验收、250 美元应付和私下结算渠道询问的公开来源。应付金额未计入实际到账。
