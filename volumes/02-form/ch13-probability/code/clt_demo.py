#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""
Central Limit Theorem demonstration: standardised sample means of
Exp(1) random variables at n = 1, 5, 30, 100. Computes histograms
and writes them as a long-format CSV for downstream plotting.

Supports the Simulation exercise on CLT convergence.

Dependencies:
    numpy

Usage:
    uv run clt_demo.py
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np


N_VALUES = (1, 5, 30, 100)
N_TRIALS = 10_000
N_BINS = 40


def standardised_means(n: int, n_trials: int, rng: np.random.Generator) -> np.ndarray:
    """Sample n_trials standardised sample means of Exp(1)."""
    samples = rng.exponential(scale=1.0, size=(n_trials, n))
    means = samples.mean(axis=1)
    # Exp(1) has mean 1 and variance 1; sigma/sqrt(n) is the SE.
    return (means - 1.0) / (1.0 / np.sqrt(n))


def summarise(arr: np.ndarray) -> dict[str, float]:
    return {
        "mean": float(arr.mean()),
        "std": float(arr.std(ddof=1)),
        "skew": float(((arr - arr.mean()) ** 3).mean()
                      / (arr.std(ddof=0) ** 3)),
        "min": float(arr.min()),
        "max": float(arr.max()),
    }


def main() -> None:
    rng = np.random.default_rng(2026)
    out_path = Path("../data/clt_histograms.csv").resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"CLT convergence demo: Exp(1), {N_TRIALS:,} trials per n.\n")
    print(f"{'n':>6} {'mean':>10} {'std':>10} {'skew':>10}")

    rows: list[tuple[int, float, int]] = []
    for n in N_VALUES:
        z = standardised_means(n, N_TRIALS, rng)
        stats = summarise(z)
        print(
            f"{n:>6d} {stats['mean']:>10.4f} {stats['std']:>10.4f}"
            f" {stats['skew']:>10.4f}"
        )
        # Histogram with fixed range for comparability
        counts, edges = np.histogram(z, bins=N_BINS, range=(-4.0, 4.0))
        centres = 0.5 * (edges[:-1] + edges[1:])
        for c, k in zip(centres, counts):
            rows.append((n, float(c), int(k)))

    with out_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "bin_centre", "count"])
        writer.writerows(rows)

    print(f"\nWrote histograms to {out_path}")
    print(
        "Expected: standard deviation near 1 for all n; skewness shrinking"
        " from large positive at n=1 toward 0 as n increases."
    )


if __name__ == "__main__":
    main()
