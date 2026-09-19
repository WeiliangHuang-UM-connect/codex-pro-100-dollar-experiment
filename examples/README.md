# 可复现实例

需要 Python 3.10+，仅用标准库。源码由本次实验生成，样例数据全部合成。

## Dijkstra

```sh
cd examples/dijkstra
python -m unittest -v test_additional
```

四个测试方法覆盖边界、输入不变、非法权重、路径重建，并通过固定种子的 30 张随机图与独立 Floyd–Warshall 结果比较。平台公开用例曾在原工作区运行通过，但本仓库不复制第三方完整题面和测试文件。

## CSV 订单核对

```sh
cd examples/csv-orders
python -m unittest -v
python merge_orders.py --input samples/orders_a.csv samples/orders_b.csv --output output
```

生成 clean.csv、review.csv、summary.json 和可离线打开的 report.html。13 行合成数据中，4 行为有效唯一记录，9 行需核对；金额核对包含重复行，不是去重后营收。详细规则见[说明](csv-orders/README.md)。

测试和生成报告不代表客户验收。输出目录没有随仓库提交，可在本机重新生成。
