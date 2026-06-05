#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""
First-order (delta-method) error propagation vs Monte Carlo, on the
resistor power-dissipation example of section 13.3.

P = I^2 * R, with I ~ N(2.0, 0.05^2) A and R ~ N(50, 1^2) ohm,
the two measured independently.

Delta method:
    Var(P) ~ (dP/dI)^2 Var(I) + (dP/dR)^2 Var(R)
           = (2 I R)^2 sigma_I^2 + (I^2)^2 sigma_R^2,  at the means.

The Monte Carlo estimate samples I and R and computes P for each draw,
which captures the second-order curvature the delta method drops.

Supports the worked example on propagating uncertainty into power
dissipation and the discussion of when the linearisation fails.

Dependencies:
    numpy.

Usage:
    uv run error_propagation.py
"""

from __future__ import annotations

import numpy as np

SEED = 2026


def delta_method(mu_i: float, sd_i: float, mu_r: float, sd_r: float):
    """Return (mean_P, sd_P) from the first-order delta method."""
    mean_p = mu_i**2 * mu_r
    dpdi = 2.0 * mu_i * mu_r
    dpdr = mu_i**2
    var_p = dpdi**2 * sd_i**2 + dpdr**2 * sd_r**2
    return mean_p, np.sqrt(var_p)


def monte_carlo(mu_i, sd_i, mu_r, sd_r, n=2_000_000, seed=SEED):
    """Return (mean_P, sd_P) from a Monte Carlo propagation."""
    rng = np.random.default_rng(seed)
    i = rng.normal(mu_i, sd_i, n)
    r = rng.normal(mu_r, sd_r, n)
    p = i**2 * r
    return float(p.mean()), float(p.std(ddof=1))


def main() -> None:
    mu_i, sd_i = 2.0, 0.05
    mu_r, sd_r = 50.0, 1.0

    d_mean, d_sd = delta_method(mu_i, sd_i, mu_r, sd_r)
    m_mean, m_sd = monte_carlo(mu_i, sd_i, mu_r, sd_r)

    print("Resistor power dissipation P = I^2 R")
    print(f"  I ~ N({mu_i}, {sd_i}^2) A,  R ~ N({mu_r}, {sd_r}^2) ohm\n")
    print(f"{'method':>14} {'mean P (W)':>14} {'sd P (W)':>12} {'rel. sd':>10}")
    print(f"{'delta':>14} {d_mean:>14.3f} {d_sd:>12.3f} {d_sd/d_mean:>10.4f}")
    print(f"{'monte carlo':>14} {m_mean:>14.3f} {m_sd:>12.3f} {m_sd/m_mean:>10.4f}")
    print(
        "\nReading: the delta method gives sd_P ~ 10.8 W (about 5.4%),"
        " driven mostly by the current term because P depends on I^2."
        " The Monte Carlo result agrees closely here because the input"
        " uncertainties are small relative to the means; for larger input"
        " spread or a more sharply curved transfer function the two"
        " diverge and the Monte Carlo value is the honest one."
    )


if __name__ == "__main__":
    main()
