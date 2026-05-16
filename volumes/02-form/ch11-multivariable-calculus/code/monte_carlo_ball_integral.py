# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "numpy",
# ]
# ///
"""
Monte Carlo integration of f(x, y, z) = x^2 + y^2 + z^2 over the
unit ball in R^3. Supports the Simulation exercise that compares
the Monte Carlo estimate with confidence interval to the analytical
answer 4 pi / 5 obtained by spherical coordinates.

For each sample size N in a user-supplied list, the script reports
the Monte Carlo estimate, the standard error, and the 95% confidence
interval.

Usage:
    python monte_carlo_ball_integral.py
"""

from __future__ import annotations
import math

import numpy as np


def sample_in_cube(n_samples: int, rng: np.random.Generator) -> np.ndarray:
    """Uniform samples in [-1, 1]^3."""
    return rng.uniform(-1.0, 1.0, size=(n_samples, 3))


def estimate(n_samples: int, rng: np.random.Generator) -> tuple[float, float]:
    """Return (estimate, standard error) of the integral over the unit ball.

    Method: sample uniformly in the enclosing cube of side 2 (volume 8),
    keep only samples inside the unit ball (||x|| <= 1), and estimate
    the integral as (cube volume) * (fraction inside) * (mean of f
    inside). The variance is propagated as the sample variance of f
    on the inside-ball samples weighted by the inside fraction.
    """
    pts = sample_in_cube(n_samples, rng)
    radii_sq = np.sum(pts * pts, axis=1)
    inside_mask = radii_sq <= 1.0
    inside_radii_sq = radii_sq[inside_mask]
    n_inside = len(inside_radii_sq)
    if n_inside == 0:
        return 0.0, 0.0
    f_on_inside = inside_radii_sq  # f = x^2 + y^2 + z^2 = ||x||^2
    cube_volume = 8.0
    p_inside = n_inside / n_samples
    integral = cube_volume * p_inside * f_on_inside.mean()
    # Standard error: variance of (cube_volume * I_inside(x) * f(x))
    # over the cube; estimate by the sample of (8 * I * f).
    weighted = np.zeros(n_samples)
    weighted[inside_mask] = cube_volume * f_on_inside
    se = float(weighted.std(ddof=1) / math.sqrt(n_samples))
    return float(integral), se


def main() -> None:
    analytical = 4.0 * math.pi / 5.0
    rng = np.random.default_rng(seed=20260516)
    sample_sizes = [10_000, 100_000, 1_000_000]
    print(f"analytical answer: 4 pi / 5 = {analytical:.6f}\n")
    header = f"{'N':>10} {'estimate':>12} {'std error':>12} {'95% CI':>30}"
    print(header)
    print("-" * len(header))
    for n in sample_sizes:
        est, se = estimate(n, rng)
        lo, hi = est - 1.96 * se, est + 1.96 * se
        print(f"{n:>10} {est:>12.6f} {se:>12.6f} {f'[{lo:.4f}, {hi:.4f}]':>30}")


if __name__ == "__main__":
    main()
