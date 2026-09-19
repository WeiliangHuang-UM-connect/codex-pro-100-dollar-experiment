# 证据与局限

本仓库是公开摘要，不是司法取证包，也不是完整原始会话备份。

| 事实 | 支持材料 | 局限 |
| --- | --- | --- |
| 一条 GitHub 资格询问确实发出 | [公开评论](https://github.com/ubiquity-os-marketplace/daemon-disqualifier/issues/135#issuecomment-5740218566) | 发出询问不代表获得资格或任务 |
| BountyBook 四次拒绝 | [脱敏响应](bountybook-attempts.json) | 来自本地保存的认证 API 响应摘录；外部读者不能靠这个文件单独证明服务器历史状态 |
| Dijkstra 本地算法测试 | [代码与独立测试](../examples/dijkstra) | 本地通过不等于平台验收 |
| CSV 合并与核对能力 | [代码和合成用例](../examples/csv-orders) | 不是商业客户作品或成交证明 |
| LaborX 具体买方需求 | [任务页](https://laborx.com/jobs/video-biography-edit-104737) | 页面可变，标价不是托管入金 |
| Google 注册可后接钱包 | [官方说明](https://laborx.com/blog/why-your-funds-are-safe-with-laborx)、[钱包功能说明](https://laborx.com/blog/release-1-6-0) | 文档较旧，当前菜单与账户绑定状态尚未实测 |

日期来自对话日期、当地执行时钟及 API 记录。BountyBook 时间戳转换为 UTC；日志默认北京时间。

公开 JSON 只保留任务 ID、提交次数、时间、验收错误、任务和付款状态，移除了执行地址与尝试 ID。没有发布 API token、cookie、签名、nonce、浏览器会话或本机用户路径。没有把第三方完整任务响应、网页源码和仓库副本打包进来。

`code-sha256.json` 记录公开示例与本地原稿的字节哈希。它能检测文件是否一致，不能独立证明代码曾被平台接受或产生收入。
