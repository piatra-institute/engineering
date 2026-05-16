# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""General Fermi-decomposition calculator with Monte Carlo error propagation.

Each branch is a triple (low, nominal, high) treated as roughly log-symmetric
about the nominal. The script samples each factor log-uniformly between low
and high, multiplies, and reports the 5th/50th/95th percentiles of the
product distribution.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(2026)
SAMPLES = 100_000


def sample(low: float, high: float, n: int) -> np.ndarray:
    """Log-uniform sampling between low and high."""
    return np.exp(RNG.uniform(np.log(low), np.log(high), size=n))


def fermi_estimate(factors: list[tuple[str, float, float, float]], ops: list[str]) -> None:
    """factors: list of (name, low, nominal, high). ops: per-factor '*' or '/'."""
    product = np.ones(SAMPLES)
    for (name, low, _nom, high), op in zip(factors, ops):
        x = sample(low, high, SAMPLES)
        product = product * x if op == "*" else product / x
    p5, p50, p95 = np.percentile(product, [5, 50, 95])
    print(f"5th  pct: {p5:.3g}")
    print(f"50th pct: {p50:.3g}")
    print(f"95th pct: {p95:.3g}")
    print(f"90% band ratio (p95/p5): {p95 / p5:.2f}x")


def demo_world_plastic() -> None:
    """World plastic production per year (Fermi 40 reference)."""
    print("World plastic production per year (kg)")
    fermi_estimate(
        [
            ("World population", 7.5e9, 8.0e9, 8.2e9),
            ("Per-capita annual plastic use (kg)", 30, 50, 80),
        ],
        ["*", "*"],
    )


if __name__ == "__main__":
    demo_world_plastic()
