# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "numpy",
# ]
# ///
"""
High-dimensional volume concentration in the unit ball and the unit
cube. Supports the failure-section discussion and the simulation
exercise that compares the analytical inscribed-ball ratio to a
Monte Carlo estimate.

For each dimension n in a user-supplied list, the script reports:
  - the analytical fraction of n-ball volume in the outer shell of
    relative thickness epsilon, 1 - (1 - epsilon)^n;
  - the analytical ratio V_n(1) / 2^n, where V_n is the n-ball volume;
  - a Monte Carlo estimate of the inscribed-ball ratio using N
    uniform samples in the cube [-1, 1]^n.

Usage:
    python volume_concentration.py

Writes a CSV table to ../data/volume_concentration.csv if the data
directory exists; prints the same table to stdout otherwise.
"""

from __future__ import annotations
import csv
from math import lgamma, log, pi, exp
from pathlib import Path

import numpy as np


def shell_fraction(n: int, epsilon: float) -> float:
    """Fraction of n-ball volume in the outer shell of width epsilon * R."""
    return 1.0 - (1.0 - epsilon) ** n


def ball_cube_ratio(n: int) -> float:
    """Analytical ratio V_n(1) / 2^n for the unit ball / unit cube."""
    # V_n(1) = pi^(n/2) / Gamma(n/2 + 1)
    log_v = (n / 2.0) * log(pi) - lgamma(n / 2.0 + 1.0)
    log_ratio = log_v - n * log(2.0)
    return exp(log_ratio)


def monte_carlo_ratio(n: int, n_samples: int, rng: np.random.Generator) -> float:
    """Estimate V_n(1) / 2^n by counting cube samples inside the unit ball."""
    pts = rng.uniform(-1.0, 1.0, size=(n_samples, n))
    inside = np.sum(np.sum(pts * pts, axis=1) <= 1.0)
    return inside / n_samples


def main() -> None:
    epsilons = [0.01, 0.05, 0.10]
    dimensions = [2, 3, 5, 10, 20, 50, 100, 500, 1000]
    rng = np.random.default_rng(seed=20260516)
    n_samples = 50_000

    header = ["n", "shell_eps001", "shell_eps005", "shell_eps010",
              "ball_cube_analytical", "ball_cube_monte_carlo"]
    rows: list[list[float]] = []
    for n in dimensions:
        shell = [shell_fraction(n, e) for e in epsilons]
        analytical = ball_cube_ratio(n)
        # Monte Carlo is only meaningful up to about n = 20 with
        # 50k samples; in higher dimensions every sample misses the
        # ball and the estimate is zero.
        mc = monte_carlo_ratio(n, n_samples, rng) if n <= 20 else 0.0
        rows.append([n, *shell, analytical, mc])

    # Stdout
    fmt = "{:>5}  {:>12}  {:>12}  {:>12}  {:>20}  {:>20}"
    print(fmt.format(*header))
    for row in rows:
        n = row[0]
        rest = [f"{v:.4g}" for v in row[1:]]
        print(fmt.format(n, *rest))

    # Optional CSV emission to ../data/
    data_dir = Path(__file__).parent.parent / "data"
    if data_dir.is_dir():
        out = data_dir / "volume_concentration.csv"
        with out.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(header)
            for row in rows:
                w.writerow(row)
        print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
