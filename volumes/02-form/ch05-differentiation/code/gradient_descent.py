# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Gradient descent for the one-variable can-optimisation problem.

Minimises the surface area A(r) = 2 pi r^2 + 2 V / r for a fixed
volume V, using the analytical derivative A'(r) = 4 pi r - 2 V / r^2
and a constant step size. Demonstrates the optimisation archetype
(Section 5.6) in code, and the importance of step-size selection.

Used by: Section 5.6 (optimisation of one variable) and Simulation
exercise on gradient-descent convergence.
"""
import math


def A(r: float, V: float) -> float:
    return 2.0 * math.pi * r * r + 2.0 * V / r


def Aprime(r: float, V: float) -> float:
    return 4.0 * math.pi * r - 2.0 * V / (r * r)


def optimum_radius(V: float) -> float:
    return (V / (2.0 * math.pi)) ** (1.0 / 3.0)


def gradient_descent(V: float, r0: float, alpha: float, n: int) -> list[float]:
    rs = [r0]
    for _ in range(n):
        r = rs[-1]
        rs.append(r - alpha * Aprime(r, V))
    return rs


def main() -> None:
    V = 1.0  # arbitrary units (cubic units)
    r_star = optimum_radius(V)
    print(f"closed-form optimum r* = {r_star:.6f}")
    print(f"A(r*) = {A(r_star, V):.6f}\n")

    for alpha in (0.01, 0.03, 0.05, 0.10):
        rs = gradient_descent(V, r0=0.2, alpha=alpha, n=200)
        final = rs[-1]
        print(
            f"alpha = {alpha:>5.3f}  ->  r_final = {final:.6f}  "
            f"|r_final - r*| = {abs(final - r_star):.3e}  A = {A(final, V):.6f}"
        )

    # Illustrate divergence at too-large step (commented to keep output bounded)
    rs_div = gradient_descent(V, r0=0.2, alpha=0.30, n=10)
    print(f"\nalpha = 0.30 first 5 iterates (divergent): {[f'{x:.3f}' for x in rs_div[:6]]}")


if __name__ == "__main__":
    main()
