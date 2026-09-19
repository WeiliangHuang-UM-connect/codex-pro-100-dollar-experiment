import csv
import hashlib
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

from merge_orders import merge_orders, parse_amount


ROOT = Path(__file__).resolve().parent


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


class MergeOrdersTests(unittest.TestCase):
    def test_conflicts_amounts_and_original_bytes(self):
        inputs = [ROOT / "samples" / "orders_a.csv", ROOT / "samples" / "orders_b.csv"]
        before = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in inputs}
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder)
            summary = merge_orders(inputs, output)
            clean = read_csv(output / "clean.csv")
            review = read_csv(output / "review.csv")
            self.assertEqual([row["订单ID"] for row in clean], ["0001", "0005", "0006", "0007"])
            self.assertEqual(len(review), 9)
            conflict = [row for row in review if row["订单ID"] == "0002"]
            self.assertEqual({row["原始金额"] for row in conflict}, {"19.90", "20.00"})
            self.assertTrue(all("DUPLICATE_CONFLICT" in row["reason_codes"] for row in conflict))
            self.assertEqual({(Path(row["source_file"]).name, row["source_line"]) for row in conflict}, {("orders_a.csv", "3"), ("orders_b.csv", "2")})
            identical = [row for row in review if row["订单ID"] == "0003"]
            self.assertEqual(len(identical), 2)
            self.assertTrue(all("DUPLICATE_IDENTICAL" in row["reason_codes"] for row in identical))
            invalid_pair = [row for row in review if row["订单ID"] == "0004"]
            self.assertEqual(len(invalid_pair), 2)
            self.assertTrue(all("DUPLICATE_CONFLICT" in row["reason_codes"] for row in invalid_pair))
            amounts = summary["amount_reconciliation"]
            self.assertEqual(amounts["valid_input_amount"], "1000000000081.81")
            self.assertEqual(amounts["clean_amount"], "1000000000012.41")
            self.assertEqual(amounts["review_valid_amount"], "69.40")
            self.assertTrue(amounts["balanced"])
            self.assertTrue(summary["row_reconciliation_balanced"])
            self.assertEqual(summary["counts"]["invalid_amount_rows"], 2)
            self.assertEqual(summary["counts"]["duplicate_conflict_groups"], 2)
            self.assertTrue((output / "report.html").is_file())
        self.assertEqual(before, {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in inputs})

    def test_exact_decimal_and_rejected_formats(self):
        self.assertEqual(parse_amount("0.1") + parse_amount("0.2"), Decimal("0.30"))
        for text in ["NaN", "Infinity", "1e3", "-1", "1,000", "1.001", ""]:
            with self.subTest(text=text):
                self.assertIsNone(parse_amount(text))

    def test_malformed_rows_and_multiline_source_are_preserved(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "synthetic.csv"
            path.write_text('订单ID,客户,金额\n\n0100,"测试\n客户",0.10\n0101,测试客户,2.00,多余列\n0102,测试客户\n', encoding="utf-8")
            output = Path(folder) / "output"
            summary = merge_orders([path], output)
            clean, review = read_csv(output / "clean.csv"), read_csv(output / "review.csv")
            self.assertEqual((clean[0]["source_line"], clean[0]["source_line_end"]), ("3", "4"))
            self.assertEqual([row["source_line"] for row in review], ["5", "6"])
            self.assertIn("多余列", review[0]["raw_fields_json"])
            self.assertTrue(all("COLUMN_COUNT" in row["reason_codes"] for row in review))
            self.assertEqual(summary["counts"]["input_rows"], 3)

    def test_input_output_collision_is_rejected_without_changes(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "clean.csv"
            path.write_text("订单ID,客户,金额\n0001,测试客户,0.10\n", encoding="utf-8")
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, "输出文件与原始输入重合"):
                merge_orders([path], Path(folder))
            self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
