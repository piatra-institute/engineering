# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Generate Pascal's triangle to a stated row and write the binomial
coefficients to a CSV file.

The recurrence used is the same one the chapter proves by induction:
C(n+1, k) = C(n, k-1) + C(n, k), with C(n, 0) = C(n, n) = 1.

The script is integer-only; no floating-point arithmetic enters. The
recurrence is computed bottom-up with memoisation in a dictionary;
this exposes the recurrence rather than the closed form n!/(k!(n-k)!),
which is the point.

Supports Volume II, Chapter 1, Simulation exercises (recursive
binomial coefficient, five-card poker hand count, Collatz iteration
preamble) and the Pascal-triangle figure.

Usage:
  python binomial_table.py <max_n> <out_csv>

  python binomial_table.py 12 ../data/pascal_to_12.csv

Output:
  CSV with columns (n, k, binom_n_k). Rows for 0 <= n <= max_n,
  0 <= k <= n.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path


def binom(n: int, k: int, memo: dict[tuple[int, int], int]) -> int:
    """Integer binomial coefficient via Pascal's recurrence."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if (n, k) in memo:
        return memo[(n, k)]
    value = binom(n - 1, k - 1, memo) + binom(n - 1, k, memo)
    memo[(n, k)] = value
    return value


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    max_n = int(sys.argv[1])
    out_path = Path(sys.argv[2])
    out_path.parent.mkdir(parents=True, exist_ok=True)

    memo: dict[tuple[int, int], int] = {}
    with out_path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["n", "k", "binom_n_k"])
        for n in range(max_n + 1):
            for k in range(n + 1):
                writer.writerow([n, k, binom(n, k, memo)])

    # Spot-check three values the chapter cites.
    assert binom(52, 5, memo) == 2_598_960, "five-card poker count"
    assert binom(30, 15, memo) == 155_117_520, "C(30, 15)"
    assert binom(10, 5, memo) == 252, "central C(10, 5)"
    print(f"wrote {out_path} for n up to {max_n}; spot-checks pass.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
