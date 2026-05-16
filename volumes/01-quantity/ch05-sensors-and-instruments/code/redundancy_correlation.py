# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Standard uncertainty of the mean of three correlated sensors.

For three sensors with equal standard deviation sigma and pairwise
correlation rho, the standard uncertainty of the mean is

    u(bar y) / sigma = sqrt((1 + 2 rho) / 3).

The script reports the ratio over a grid of rho, and Monte Carlo
verifies the closed-form expression. The Air France 447 case is the
illustration: independent in design, correlated in failure.

Companion to Simulation exercise 4 and the failure section.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(seed=11)
N_SENSORS = 3
N_SAMPLES = 200_000


def closed_form(rho: float) -> float:
    return float(np.sqrt((1.0 + 2.0 * rho) / N_SENSORS))


def monte_carlo(rho: float) -> float:
    # Build covariance matrix sigma = 1 with off-diagonal rho
    cov = np.full((N_SENSORS, N_SENSORS), rho)
    np.fill_diagonal(cov, 1.0)
    samples = RNG.multivariate_normal(np.zeros(N_SENSORS), cov, size=N_SAMPLES)
    means = samples.mean(axis=1)
    return float(np.std(means, ddof=1))


def main() -> None:
    print(f"{'rho':>6}  {'closed-form':>12}  {'Monte Carlo':>12}")
    for rho in (0.0, 0.5, 0.9, 0.99, 1.0):
        cf = closed_form(rho)
        mc = monte_carlo(rho)
        print(f"{rho:>6.2f}  {cf:>12.4f}  {mc:>12.4f}")
    print()
    print("At rho = 1 the three sensors deliver no precision benefit "
          "relative to a single sensor.")


if __name__ == "__main__":
    main()
