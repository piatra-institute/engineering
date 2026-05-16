# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Monte Carlo of y = x1 - x2 for correlated normals.

Verifies the correlated-difference formula
u_c^2(y) = u^2(x1) + u^2(x2) - 2 rho u(x1) u(x2),
which captures the common-mode cancellation exploited by comparator
measurements in metrology.
"""

import numpy as np

RNG = np.random.default_rng(99)
N = 100_000


def correlated_normals(rho: float, n: int = N) -> tuple[np.ndarray, np.ndarray]:
    u = RNG.standard_normal(n)
    v = RNG.standard_normal(n)
    x1 = u
    x2 = rho * u + np.sqrt(1 - rho**2) * v
    return x1, x2


def main() -> None:
    print(f"{'rho':>6}  {'empirical sd(x1-x2)':>22}  {'analytical':>12}")
    for rho in (0.0, 0.5, 0.9, 0.99):
        x1, x2 = correlated_normals(rho)
        diff = x1 - x2
        analytical = np.sqrt(1 + 1 - 2 * rho)
        print(f"{rho:>6.2f}  {diff.std(ddof=1):>22.4f}  {analytical:>12.4f}")


if __name__ == "__main__":
    main()
