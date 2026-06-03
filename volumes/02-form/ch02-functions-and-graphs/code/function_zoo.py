# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Tabulate five elementary functions on a shared horizontal range and
write the values to a CSV file.

The five are: a linear function (y = x/2), a quadratic (y = x^2 / 8),
an exponential (y = 0.2 exp(0.6 x)), a natural logarithm (y = ln(x +
1)), and a sinusoid (y = 1.5 + sin x). The point is comparison of
scaling behaviour on a single eye-friendly range. The CSV the script
writes can be cross-checked against the function-zoo figure.

Supports Volume II, Chapter 2, Section 2.1 reading and the
function-zoo figure (fig:vol02:ch02:function-zoo).

Usage:
  python function_zoo.py <x_min> <x_max> <n_points> <out_csv>

  python function_zoo.py 0 6 200 ../data/function_zoo.csv
"""

from __future__ import annotations

import csv
import math
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 5:
        print(__doc__)
        return 2
    x_min = float(sys.argv[1])
    x_max = float(sys.argv[2])
    n = int(sys.argv[3])
    out_path = Path(sys.argv[4])
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for i in range(n + 1):
        x = x_min + (x_max - x_min) * i / n
        rows.append(
            {
                "x": x,
                "linear": 0.5 * x,
                "quadratic": (x * x) / 8.0,
                "exponential": 0.2 * math.exp(0.6 * x),
                "logarithm": math.log(x + 1.0),
                "sinusoid": 1.5 + math.sin(x),
            }
        )

    with out_path.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "x",
                "linear",
                "quadratic",
                "exponential",
                "logarithm",
                "sinusoid",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    # Spot-checks: at x = 0 the linear and quadratic are 0, the
    # exponential is 0.2, the logarithm is 0, and the sinusoid is
    # 1.5.
    assert math.isclose(rows[0]["linear"], 0.0)
    assert math.isclose(rows[0]["quadratic"], 0.0)
    assert math.isclose(rows[0]["exponential"], 0.2)
    assert math.isclose(rows[0]["logarithm"], 0.0)
    assert math.isclose(rows[0]["sinusoid"], 1.5)
    print(f"wrote {out_path} with {n + 1} rows; spot-checks pass.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
