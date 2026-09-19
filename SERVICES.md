# 公开接单入口

本实验正在尝试获得真实、范围明确的小型委托。当前可展示的服务是 **CSV 数据清洗与自动化**，可运行样例在 [examples/csv-orders](examples/csv-orders)。

可讨论的交付包括：统一表头的多表合并、重复与金额异常检查、保留来源行号、可复现脚本与离线报告。样例是合成演示，没有虚构客户或商业履历。

如果有这类需求，可[新建 GitHub Issue](https://github.com/WeiliangHuang-UM-connect/codex-pro-100-dollar-experiment/issues/new?template=service-request.yml)，只描述需求和脱敏结构。请勿在公开 Issue 上传真实客户数据、账户信息或其他秘密。

本次试单参考报价为 120 USDC，最终价格、范围、工期、修改次数和支付安排需双方明确后才成立。优先讨论双方同意的加密货币结算；不会因读者创建 Issue 自动形成合同，也不要求为了沟通先转币。交付使用 AI 辅助，由实验发起者对约定成果负责。

上述 CSV 服务目前尚无成交。另一个故障复现委托 SABLE 已验收，250 美元应收未收；本实验已核实到账仍为 0。

同一服务已在 [LaborX 发布](https://laborx.com/gigs/i-will-clean-merge-and-validate-csv-files-with-a-python-script-122168)，平台标价 120 USDC，选定 Base 网络。完整固定范围与交付条件见[服务文案](docs/laborx-csv-gig-draft.md)。发布本身不代表成交。


## 故障复现与回归测试

可展示的实际作品是 [SABLE-001 Java SDK 独立验证](deliverables/sable-001/REPORT.md)，已经买方验收，付款尚未收到。交付包含固定源码版本、可运行复现器、正常与重试对照、独立 JVM 持久化核对、公开 CI 和机器可读证据。其结论仅适用于报告写明的版本与测试边界。

可以讨论同类的单问题复现或回归测试委托：先约定版本、环境、可运行样例、验收检查、费用和付款方式，再确定是否承接。不会把现有作品泛化为对任何系统都能保证修复，也不会在未知需求下承诺完整安全审计。使用 AI 辅助并明确记录实际执行的验证。
