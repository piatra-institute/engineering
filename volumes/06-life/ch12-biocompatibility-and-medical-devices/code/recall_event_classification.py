"""
Classify FDA medical-device recall events by class (I/II/III) and by
device category.

Vol VI Ch 12 sec 12.6; calculation exercise 4.

The companion data file `data/fda_recalls_by_class.csv` carries a
synthesised summary representative of FDA MAUDE / recall-database
counts for a recent fiscal year. The shape of the distribution
(Class II dominant, Class I a small share, Class III rare) is
representative; specific counts are illustrative.

References:
- web:v6c12-fda-maude-2024
- paper:v6c12-amato-recall-data-2014
- paper:v6c12-makary-recalls-2017
"""

from __future__ import annotations
import csv
from pathlib import Path
from collections import defaultdict


DATA_FILE = Path(__file__).parent.parent / "data" \
    / "fda_recalls_by_class.csv"


def load_recalls() -> list[dict]:
    with DATA_FILE.open() as fh:
        return list(csv.DictReader(fh))


def by_class(rows: list[dict]) -> dict[str, int]:
    out: dict[str, int] = defaultdict(int)
    for r in rows:
        out[r["class"]] += int(r["count"])
    return dict(out)


def by_category(rows: list[dict]) -> dict[str, int]:
    out: dict[str, int] = defaultdict(int)
    for r in rows:
        out[r["category"]] += int(r["count"])
    return dict(out)


def class_share(rows: list[dict]) -> dict[str, float]:
    counts = by_class(rows)
    total = sum(counts.values())
    return {c: n / total for c, n in counts.items()} if total else {}


def main() -> None:
    rows = load_recalls()
    print("Counts by class:")
    for c, n in sorted(by_class(rows).items()):
        print(f"  Class {c}: {n}")

    print()
    print("Counts by category (top 10):")
    cat = sorted(by_category(rows).items(),
                 key=lambda kv: kv[1], reverse=True)[:10]
    for cat_name, n in cat:
        print(f"  {cat_name}: {n}")

    print()
    print("Share by class:")
    for c, s in sorted(class_share(rows).items()):
        print(f"  Class {c}: {s:.3f}")


if __name__ == "__main__":
    main()
