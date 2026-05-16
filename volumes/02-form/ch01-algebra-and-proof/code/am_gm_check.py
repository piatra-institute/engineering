# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""
Empirical check of the arithmetic-mean / geometric-mean inequality.

For sample vectors of length n drawn from a stated non-negative
distribution, compute AM(x) = mean(x), GM(x) = exp(mean(log(x))),
and the ratio AM / GM. AM-GM guarantees this ratio is at least 1
for every sample; the script logs the empirical distribution of the
ratio and the fraction of samples that strictly exceed 1.

The script is the supporting tool for the simulation exercise that
asks the reader to observe AM-GM in practice across several n.

Usage:
  python am_gm_check.py <n_values_csv> <distribution> <samples> <out_csv>

  Example:
    python am_gm_check.py 2,5,10,50 exp 10000 ../data/am_gm_exp.csv

  distributions:
    exp     -- Exp(1)
    halfn   -- |N(0, 1)|
    uniform -- Uniform(0, 1)

Output:
  CSV with columns (n, sample, AM, GM, ratio). Console prints the
  per-n mean and standard deviation of the ratio, and the empirical
  fraction with ratio > 1 (must be 1.0 modulo ties).
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import numpy as np


def draw(rng: np.random.Generator, dist: str,
         n_samples: int, n: int) -> np.ndarray:
    if dist == "exp":
        return rng.exponential(scale=1.0, size=(n_samples, n))
    if dist == "halfn":
        return np.abs(rng.standard_normal(size=(n_samples, n)))
    if dist == "uniform":
        return rng.uniform(low=1e-9, high=1.0, size=(n_samples, n))
    raise ValueError(f"unknown distribution {dist!r}")


def main() -> int:
    if len(sys.argv) != 5:
        print(__doc__)
        return 2
    n_values = [int(s) for s in sys.argv[1].split(",")]
    dist = sys.argv[2]
    n_samples = int(sys.argv[3])
    out_path = Path(sys.argv[4])
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(seed=20260516)

    with out_path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["n", "sample", "AM", "GM", "ratio"])
        for n in n_values:
            x = draw(rng, dist, n_samples, n) + 1e-12  # avoid log(0)
            am = x.mean(axis=1)
            gm = np.exp(np.log(x).mean(axis=1))
            ratio = am / gm
            assert (ratio >= 1.0 - 1e-9).all(), (
                f"AM-GM violation at n={n}: min ratio {ratio.min()}")
            for i in range(n_samples):
                writer.writerow([n, i, float(am[i]), float(gm[i]),
                                 float(ratio[i])])
            print(f"n={n:>3d}  mean(ratio)={ratio.mean():.4f}  "
                  f"sd(ratio)={ratio.std():.4f}  "
                  f"fraction strict={(ratio > 1.0).mean():.4f}")

    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
