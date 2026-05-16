# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Collatz iteration runner.

The Collatz map sends n -> n/2 when n is even and n -> 3n + 1 when n
is odd. The Collatz conjecture states that the iteration reaches 1
from every positive integer. The conjecture is unproved as of 2026;
no finite simulation can settle it. The script computes, for every
starting value 1 <= n <= n_max, the number of steps to reach 1, and
writes (n, steps) to a CSV.

Supports Volume II, Chapter 1, Simulation exercise on Collatz, and
the chapter's running point that empirical demonstration is not
proof.

Usage:
  python collatz_run.py <n_max> <out_csv>

  python collatz_run.py 100000 ../data/collatz_to_1e5.csv

Output:
  CSV with columns (n, steps). The script prints the maximum step
  count and the starting value that achieves it.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path


def collatz_steps(n: int, cache: dict[int, int]) -> int:
    steps = 0
    m = n
    path = []
    while m != 1:
        if m in cache:
            steps += cache[m]
            break
        path.append(m)
        if m % 2 == 0:
            m //= 2
        else:
            m = 3 * m + 1
        steps += 1
    for offset, p in enumerate(reversed(path)):
        cache[p] = steps - (len(path) - 1 - offset)
    return steps


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    n_max = int(sys.argv[1])
    out_path = Path(sys.argv[2])
    out_path.parent.mkdir(parents=True, exist_ok=True)

    cache: dict[int, int] = {1: 0}
    max_steps = 0
    max_n = 1
    with out_path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["n", "steps"])
        for n in range(1, n_max + 1):
            s = collatz_steps(n, cache)
            writer.writerow([n, s])
            if s > max_steps:
                max_steps = s
                max_n = n

    print(f"wrote {out_path}; max steps = {max_steps} at n = {max_n}")
    print("simulation is not a proof of the Collatz conjecture.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
