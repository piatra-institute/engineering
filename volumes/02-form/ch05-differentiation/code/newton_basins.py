# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Basins of attraction and divergence for Newton's iteration.

For g(x) = x^3 - 2x - 5 (one real root near 2.0945) the iteration
converges from a wide bracket but can be flung far by a near-zero
derivative. For g(x) = arctan(x) (root at 0) the iteration diverges
when started outside a finite basin. This script sweeps starting
points and reports, for each, whether the iteration converges within
a tolerance in a fixed number of steps and the iterate count.

Used by: Section 5.4 (Newton's-method divergence) and the
Newton-divergence figure.
"""
from math import atan


def newton(g, gp, x0: float, tol: float = 1e-12, nmax: int = 50):
    x = x0
    for k in range(1, nmax + 1):
        d = gp(x)
        if d == 0.0:
            return None, k  # flat derivative; iteration undefined
        x_new = x - g(x) / d
        if abs(x_new - x) < tol:
            return x_new, k
        x = x_new
        if abs(x) > 1e6:
            return None, k  # diverged
    return None, nmax


def sweep(name, g, gp, starts):
    print(f"\n{name}")
    print(f"{'x0':>8} {'result':>14} {'steps':>6}")
    for x0 in starts:
        root, k = newton(g, gp, x0)
        tag = f"{root:.8f}" if root is not None else "diverged"
        print(f"{x0:>8.3f} {tag:>14} {k:>6d}")


def main() -> None:
    sweep(
        "g(x) = x^3 - 2x - 5 (root ~ 2.0945)",
        lambda x: x**3 - 2.0 * x - 5.0,
        lambda x: 3.0 * x**2 - 2.0,
        [-3.0, -1.0, 0.0, 0.5, 0.8, 1.0, 2.0, 5.0],
    )
    sweep(
        "g(x) = arctan(x) (root = 0)",
        atan,
        lambda x: 1.0 / (1.0 + x * x),
        [0.5, 1.0, 1.3, 1.39, 1.4, 1.5, 2.0],
    )
    print("\nFor arctan, the basin of attraction is roughly |x0| < 1.39;")
    print("starting outside it the iterates overshoot and run away.")


if __name__ == "__main__":
    main()
