# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Empirical standard deviation of x + y for correlated normals.

Demonstrates how positive correlation amplifies and negative correlation
reduces the standard deviation of a sum, matching the formula
u^2(x+y) = u^2(x) + u^2(y) + 2 rho u(x) u(y).
"""

import numpy as np

RNG = np.random.default_rng(42)
N = 10_000


def correlated_normals(rho: float, n: int = N) -> tuple[np.ndarray, np.ndarray]:
    u = RNG.standard_normal(n)
    v = RNG.standard_normal(n)
    x = u
    y = rho * u + np.sqrt(1 - rho**2) * v
    return x, y


def main() -> None:
    print(f"{'rho':>6}  {'empirical sd(x+y)':>20}  {'analytical':>12}")
    for rho in (-0.5, 0.0, 0.5, 0.9, 0.99):
        x, y = correlated_normals(rho)
        z = x + y
        analytical = np.sqrt(1 + 1 + 2 * rho)
        print(f"{rho:>6.2f}  {z.std(ddof=1):>20.4f}  {analytical:>12.4f}")


if __name__ == "__main__":
    main()
