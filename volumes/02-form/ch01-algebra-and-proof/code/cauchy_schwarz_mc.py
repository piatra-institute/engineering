# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""
Monte-Carlo verification of the Cauchy-Schwarz inequality.

For N random pairs of vectors (u, v) in R^d drawn from a standard
normal distribution, compute <u, v>^2 and ||u||^2 ||v||^2 and confirm
that the first is at most the second. The ratio R = <u, v>^2 /
(||u||^2 ||v||^2) is the squared cosine of the angle between u and
v; under the standard normal in d dimensions it concentrates around
1/d, well below the bound 1.

Supports Volume II, Chapter 1, Simulation exercise on numerical
Cauchy-Schwarz.

Usage:
  python cauchy_schwarz_mc.py <d> <N> <out_csv>

  python cauchy_schwarz_mc.py 10 1000 ../data/cauchy_schwarz_d10.csv

Output:
  CSV with columns (trial, inner_sq, norm_u_sq_norm_v_sq, ratio).
  The script also prints the maximum ratio observed, which should be
  strictly below 1, and the mean ratio, which should be close to 1/d.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import numpy as np


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        return 2
    d = int(sys.argv[1])
    n_trials = int(sys.argv[2])
    out_path = Path(sys.argv[3])
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(seed=20260516)
    u = rng.standard_normal(size=(n_trials, d))
    v = rng.standard_normal(size=(n_trials, d))

    inner_sq = (np.sum(u * v, axis=1)) ** 2
    norm_uv = np.sum(u * u, axis=1) * np.sum(v * v, axis=1)
    ratio = inner_sq / norm_uv

    with out_path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["trial", "inner_sq", "norm_u_sq_norm_v_sq", "ratio"])
        for i in range(n_trials):
            writer.writerow([i, float(inner_sq[i]), float(norm_uv[i]),
                             float(ratio[i])])

    assert ratio.max() <= 1.0, (
        f"Cauchy-Schwarz violation: max ratio {ratio.max()} > 1")
    print(f"wrote {out_path}; max ratio = {ratio.max():.6f} (must be <= 1)")
    print(f"mean ratio = {ratio.mean():.6f}; expected ~ 1/d = {1/d:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
