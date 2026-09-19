#!/usr/bin/env python3
"""Merge a small, local set of CSV order exports without changing the inputs."""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from decimal import Decimal, localcontext
from pathlib import Path


COLUMNS = ["订单ID", "客户", "金额"]
OUTPUT_NAMES = ("clean.csv", "review.csv", "summary.json", "report.html")
AMOUNT_PATTERN = re.compile(r"[0-9]{1,16}(?:\.[0-9]{1,2})?\Z")
REASONS = {
    "COLUMN_COUNT": "列数与表头不一致",
    "MISSING_ORDER_ID": "订单ID为空",
    "MISSING_CUSTOMER": "客户为空",
    "INVALID_AMOUNT": "金额格式非法",
    "DUPLICATE_CONFLICT": "重复订单ID且内容冲突，整组待核对",
    "DUPLICATE_IDENTICAL": "重复订单ID且内容相同，整组待核对",
}


@dataclass
class Order:
    source_file: str
    source_line: int
    source_line_end: int
    raw_fields: list[str]
    order_id: str
    customer: str
    raw_amount: str
    amount: Decimal | None
    reasons: list[str] = field(default_factory=list)
    duplicate_group_size: int = 0


class TrackedLines:
    """Track the physical lines consumed by csv.reader, including quoted newlines."""

    def __init__(self, stream):
        self.stream = stream
        self.line_number = 0
        self.record_lines: list[tuple[int, str]] = []

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self.stream)
        self.line_number += 1
        self.record_lines.append((self.line_number, line))
        return line

    def start_record(self):
        self.record_lines.clear()

    def record_start(self):
        # Empty records are skipped by read_orders; preserve quoted newlines.
        return next(number for number, text in self.record_lines if text.rstrip("\r\n"))


def money(value: Decimal) -> str:
    return format(value, ".2f")


def parse_amount(value: str) -> Decimal | None:
    value = value.strip()
    if not AMOUNT_PATTERN.fullmatch(value):
        return None
    return Decimal(value).quantize(Decimal("0.01"))


def read_orders(path: Path) -> list[Order]:
    orders = []
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        lines = TrackedLines(stream)
        reader = csv.reader(lines, strict=True)
        try:
            headers = next(reader)
        except StopIteration:
            raise ValueError(f"输入文件为空：{path}") from None
        if len(headers) != len(COLUMNS) or set(headers) != set(COLUMNS):
            raise ValueError(f"表头必须恰好包含 {COLUMNS}（顺序不限）：{path}")
        while True:
            lines.start_record()
            try:
                cells = next(reader)
            except StopIteration:
                break
            if not cells:
                continue
            values = dict(zip(headers, cells))
            raw_amount = values.get("金额", "")
            order = Order(
                source_file=str(path),
                source_line=lines.record_start(),
                source_line_end=reader.line_num,
                raw_fields=cells,
                order_id=values.get("订单ID", "").strip(),
                customer=values.get("客户", "").strip(),
                raw_amount=raw_amount,
                amount=parse_amount(raw_amount),
            )
            if len(cells) != len(headers):
                order.reasons.append("COLUMN_COUNT")
            if not order.order_id:
                order.reasons.append("MISSING_ORDER_ID")
            if not order.customer:
                order.reasons.append("MISSING_CUSTOMER")
            if order.amount is None:
                order.reasons.append("INVALID_AMOUNT")
            orders.append(order)
    return orders


def signature(order: Order):
    # Equivalent numeric strings such as 8.0 and 8.00 are the same amount.
    amount = ("valid", money(order.amount)) if order.amount is not None else ("invalid", order.raw_amount.strip())
    structure = tuple(order.raw_fields) if "COLUMN_COUNT" in order.reasons else ()
    return order.customer, amount, structure


def write_csv(path: Path, headers: list[str], rows: list[dict]):
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def render_report(summary: dict, clean: list[dict], review: list[dict]) -> str:
    def escape(value):
        return html.escape(str(value), quote=True)

    def table(rows, fields):
        if not rows:
            return "<p>无记录。</p>"
        head = "".join(f"<th>{escape(name)}</th>" for name in fields)
        body = "".join("<tr>" + "".join(f"<td>{escape(row.get(name, ''))}</td>" for name in fields) + "</tr>" for row in rows)
        return f'<div class="scroll"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'

    counts = summary["counts"]
    amounts = summary["amount_reconciliation"]
    stats = "".join(f'<div class="card"><b>{value}</b><span>{label}</span></div>' for label, value in [
        ("输入记录", counts["input_rows"]), ("有效唯一订单", counts["clean_rows"]),
        ("待人工核对", counts["review_rows"]), ("重复ID组", counts["duplicate_groups"]),
    ])
    return f'''<!doctype html>
<html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>订单合并与核对 · 合成数据演示</title>
<style>
body{{font:16px/1.65 system-ui,"Microsoft YaHei",sans-serif;color:#17314d;background:#f4f7fb;margin:0}}
main{{max-width:1120px;margin:auto;padding:36px 24px}}h1{{font-size:30px;margin-bottom:8px}}h2{{margin-top:32px}}
.note{{color:#52667e}}.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:24px 0}}
.card,.box{{background:white;padding:20px;border:1px solid #dfe6ee;border-radius:12px}}
.card b{{display:block;font-size:30px}}.card span{{color:#52667e}}.scroll{{overflow:auto;background:white;border:1px solid #dfe6ee;border-radius:10px}}
table{{border-collapse:collapse;width:100%;font-size:14px}}th,td{{padding:12px;text-align:left;border-bottom:1px solid #e5ebf2;vertical-align:top}}
th{{background:#eaf0f7;white-space:nowrap}}td{{overflow-wrap:anywhere;min-width:72px}}code{{overflow-wrap:anywhere}}
</style><main>
<p class="note">作品样例 · 随附数据均为人工合成，无真实客户信息或业绩声明</p>
<h1>多表订单合并与核对</h1>
<p>有效且唯一的订单进入 clean.csv；每一条重复或异常记录进入 review.csv，并保留来源和原始字段。</p>
<div class="stats">{stats}</div>
<section class="box"><h2 style="margin-top:0">金额核对</h2>
<p>可解析输入金额 <strong>{escape(amounts['valid_input_amount'])}</strong><br>
= 有效唯一订单 <strong>{escape(amounts['clean_amount'])}</strong><br>
+ 待核对记录中的可解析金额 <strong>{escape(amounts['review_valid_amount'])}</strong></p>
<p>核对结果：{'一致' if amounts['balanced'] else '不一致'}。金额非法的 {counts['invalid_amount_rows']} 条记录未参与金额求和。
重复行金额保留在待核对金额中；输入金额合计不代表去重后的营业额。全部输入按同一币种处理。</p></section>
<h2>有效唯一订单（{counts['clean_rows']} 条）</h2>
{table(clean, ['订单ID','客户','金额','source_file','source_line'])}
<h2>待人工核对（{counts['review_rows']} 条）</h2>
{table(review, ['订单ID','客户','原始金额','规范金额','reason','duplicate_group_size','source_file','source_line','source_line_end'])}
<p class="note">行号从 1 开始，包含表头；跨行字段另存结束行号。完整原始字段和原因代码见 review.csv。未自动选取重复组中的任意一条记录。</p>
</main></html>'''


def merge_orders(input_paths: list[Path], output_dir: Path) -> dict:
    paths = [Path(path).resolve(strict=True) for path in input_paths]
    if not paths:
        raise ValueError("至少需要一个输入CSV文件")
    if len(paths) != len(set(paths)):
        raise ValueError("同一个输入文件不能重复提供")
    output_dir = Path(output_dir).resolve()
    if any((output_dir / name).resolve() in paths for name in OUTPUT_NAMES):
        raise ValueError("输出文件与原始输入重合，请更换输出目录")

    orders = [order for path in paths for order in read_orders(path)]
    groups = defaultdict(list)
    for order in orders:
        if order.order_id:
            groups[order.order_id].append(order)
    duplicates = [group for group in groups.values() if len(group) > 1]
    conflict_groups = 0
    for group in duplicates:
        conflict = len({signature(order) for order in group}) > 1
        conflict_groups += int(conflict)
        for order in group:
            order.reasons.append("DUPLICATE_CONFLICT" if conflict else "DUPLICATE_IDENTICAL")
            order.duplicate_group_size = len(group)

    clean_orders = [order for order in orders if not order.reasons]
    review_orders = [order for order in orders if order.reasons]
    clean, review = [], []
    for order in orders:
        common = {
            "订单ID": order.order_id, "客户": order.customer,
            "source_file": order.source_file, "source_line": order.source_line,
            "source_line_end": order.source_line_end,
        }
        if order.reasons:
            review.append({**common, "原始金额": order.raw_amount,
                "规范金额": money(order.amount) if order.amount is not None else "",
                "reason_codes": "|".join(order.reasons),
                "reason": "；".join(REASONS[reason] for reason in order.reasons),
                "duplicate_group_size": order.duplicate_group_size,
                "raw_fields_json": json.dumps(order.raw_fields, ensure_ascii=False),
            })
        else:
            clean.append({**common, "金额": money(order.amount)})

    with localcontext() as context:
        context.prec = max(28, len(str(len(orders))) + 20)
        valid_total = sum((order.amount for order in orders if order.amount is not None), Decimal("0.00"))
        clean_total = sum((order.amount for order in clean_orders), Decimal("0.00"))
        review_total = sum((order.amount for order in review_orders if order.amount is not None), Decimal("0.00"))
        balanced = valid_total == clean_total + review_total
    summary = {
        "demo_notice": "随附输入均为人工合成示例，不代表客户项目或收入。",
        "input_files": [str(path) for path in paths],
        "counts": {
            "input_files": len(paths), "input_rows": len(orders), "clean_rows": len(clean),
            "review_rows": len(review), "valid_amount_rows": sum(order.amount is not None for order in orders),
            "invalid_amount_rows": sum(order.amount is None for order in orders),
            "duplicate_groups": len(duplicates), "duplicate_rows": sum(map(len, duplicates)),
            "duplicate_conflict_groups": conflict_groups,
        },
        "amount_reconciliation": {
            "valid_input_amount": money(valid_total), "clean_amount": money(clean_total),
            "review_valid_amount": money(review_total), "balanced": balanced,
            "note": "金额均为十进制字符串；只统计可解析金额；重复行也计入输入及待核对金额，不能视为去重后的营业额。",
        },
        "row_reconciliation_balanced": len(orders) == len(clean) + len(review),
        "duplicate_policy": "相同ID的所有行均进入review.csv；不会自动选取或丢弃其中任何一行。",
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(output_dir / "clean.csv", [*COLUMNS, "source_file", "source_line", "source_line_end"], clean)
    write_csv(output_dir / "review.csv", ["订单ID", "客户", "原始金额", "规范金额", "reason_codes", "reason", "duplicate_group_size", "source_file", "source_line", "source_line_end", "raw_fields_json"], review)
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output_dir / "report.html").write_text(render_report(summary, clean, review), encoding="utf-8")
    return summary


def main():
    parser = argparse.ArgumentParser(description="合并本地CSV订单：唯一有效订单输出clean.csv，重复与异常输出review.csv。")
    parser.add_argument("--input", nargs="+", type=Path, required=True, help="输入CSV文件，可提供多个")
    parser.add_argument("--output", type=Path, default=Path("output"), help="输出目录，默认output")
    args = parser.parse_args()
    try:
        summary = merge_orders(args.input, args.output)
    except (ValueError, OSError, csv.Error) as error:
        parser.exit(2, f"处理失败：{error}\n")
    counts = summary["counts"]
    print(f"输入 {counts['input_rows']} 条；有效唯一 {counts['clean_rows']} 条；待核对 {counts['review_rows']} 条。")
    print(f"金额核对：{'一致' if summary['amount_reconciliation']['balanced'] else '不一致'}；输出：{args.output.resolve()}")


if __name__ == "__main__":
    main()
