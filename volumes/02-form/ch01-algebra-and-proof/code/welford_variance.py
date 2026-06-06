# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Welford's single-pass running mean and variance, compared against the
naive sum-of-squares single-pass identity on a badly-scaled stream.

The naive single-pass form uses the exact-over-the-reals identity
    sum (x_i - xbar)^2 = sum x_i^2 - (sum x_i)^2 / n,
which subtracts two large, nearly equal quantities for data clustered
far from zero, and suffers catastrophic cancellation; the computed
variance can come out negative. Welford's update forms each correction
from a residual (x_n - xbar_{n-1}) of the order of the data spread, and
is well conditioned.

Supports Volume II, Chapter 1, section 1.4 (case study: a numerically
stable running variance, derived and verified) and section 1.1
(catastrophic cancellation).

Usage:
  python welford_variance.py
"""

from __future__ import annotations

import csv
import random
from pathlib import Path


def welford(xs: list[float]) -> tuple[float, float]:
    """Return (mean, sample_variance) by Welford's incremental update."""
    mean = 0.0
    m2 = 0.0  # running sum of squared deviations, M_n in the text
    for n, x in enumerate(xs, start=1):
        delta = x - mean
        mean += delta / n
        delta2 = x - mean
        m2 += delta * delta2
    var = m2 / (len(xs) - 1) if len(xs) > 1 else 0.0
    return mean, var


def naive_single_pass(xs: list[float]) -> tuple[float, float]:
    """Return (mean, sample_variance) by the sum-of-squares identity.

    Numerically dangerous when the data are clustered far from zero.
    """
    n = len(xs)
    s = sum(xs)
    s2 = sum(x * x for x in xs)
    mean = s / n
    # The cancellation lives in this subtraction:
    var = (s2 - s * s / n) / (n - 1) if n > 1 else 0.0
    return mean, var


def two_pass(xs: list[float]) -> tuple[float, float]:
    """Return (mean, sample_variance) by the well-conditioned two-pass form."""
    n = len(xs)
    mean = sum(xs) / n
    var = sum((x - mean) ** 2 for x in xs) / (n - 1) if n > 1 else 0.0
    return mean, var


def main() -> int:
    rng = random.Random(20260606)
    rows = []
    # Sweep the cluster offset: spread fixed at 1e-3, offset grows.
    spread = 1.0e-3
    for offset in (0.0, 1.0e2, 1.0e4, 1.0e6, 1.0e8):
        xs = [offset + spread * rng.gauss(0.0, 1.0) for _ in range(10_000)]
        _, v_welford = welford(xs)
        _, v_naive = naive_single_pass(xs)
        _, v_truth = two_pass(xs)  # reference, well conditioned
        rel_err_welford = abs(v_welford - v_truth) / v_truth
        rel_err_naive = abs(v_naive - v_truth) / v_truth
        rows.append(
            {
                "cluster_offset": f"{offset:.0e}",
                "var_two_pass": f"{v_truth:.6e}",
                "var_welford": f"{v_welford:.6e}",
                "var_naive_single_pass": f"{v_naive:.6e}",
                "rel_err_welford": f"{rel_err_welford:.3e}",
                "rel_err_naive": f"{rel_err_naive:.3e}",
            }
        )
        print(
            f"offset={offset:.0e}: truth={v_truth:.4e} "
            f"welford rel.err={rel_err_welford:.2e} "
            f"naive rel.err={rel_err_naive:.2e}"
        )
        # Welford must track the well-conditioned two-pass form closely.
        assert rel_err_welford < 1e-6, "Welford lost accuracy unexpectedly"

    out = Path(__file__).resolve().parents[1] / "data" / "welford-vs-naive.csv"
    with out.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out}")
    print("Welford spot-checks pass.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
