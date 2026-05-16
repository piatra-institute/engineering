# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Monte Carlo comparison to the log-quadrature approximation for a Fermi
decomposition with k independent factors.

The log-quadrature approximation says that for X = prod_i f_i with each f_i
log-normal with sigma sigma_i, the result is log-normal with sigma squared
equal to the sum of sigma_i squared.

This script verifies the approximation by Monte Carlo for k = 1, 3, 5, 7
factors at a per-factor sigma corresponding to a factor-of-1.5 working
uncertainty (one-sigma log-width log(1.5) ~ 0.405).
"""

from __future__ import annotations

import math

import numpy as np

RNG = np.random.default_rng(2026)
SAMPLES = 200_000
SIGMA = math.log(1.5)


def main() -> None:
    print(f"Per-factor sigma_log = log(1.5) = {SIGMA:.3f}")
    print(f"{'k':>3} {'predicted sigma_log':>22} {'empirical sigma_log':>22} {'factor 1-sigma':>16}")
    for k in (1, 3, 5, 7):
        x = RNG.normal(0.0, SIGMA, size=(SAMPLES, k))
        log_product = x.sum(axis=1)
        empirical = log_product.std(ddof=1)
        predicted = SIGMA * math.sqrt(k)
        factor = math.exp(empirical)
        print(f"{k:>3d} {predicted:>22.4f} {empirical:>22.4f} {factor:>15.2f}x")


if __name__ == "__main__":
    main()
