# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""
Trapezoidal, Simpson, and three-point Gauss-Legendre quadrature
applied to I = int_0^1 exp(-x^2) dx.

Prints absolute error against n (number of function evaluations) for
each rule. The exact value is (sqrt(pi)/2) * erf(1) ~
0.7468241328124270.

Supports Volume II, Chapter 6:
  - Simulation exercise 1 (log-log convergence study).
  - Figure fig-quadrature-convergence.

Run directly with uv:
    uv run quadrature_convergence.py
"""

from __future__ import annotations

import math

import numpy as np


def integrand(x: np.ndarray) -> np.ndarray:
    return np.exp(-x * x)


def exact_value() -> float:
    return 0.5 * math.sqrt(math.pi) * math.erf(1.0)


def trapezoidal(f, a: float, b: float, n: int) -> float:
    """Composite trapezoidal rule on n subintervals (n + 1 evaluations)."""
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return float(h * (0.5 * y[0] + y[1:-1].sum() + 0.5 * y[-1]))


def simpson(f, a: float, b: float, n: int) -> float:
    """Composite Simpson rule on n subintervals (n even; n + 1 evaluations)."""
    if n % 2:
        raise ValueError("Simpson's rule requires even n.")
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return float(h / 3.0 * (y[0] + 4.0 * y[1:-1:2].sum()
                            + 2.0 * y[2:-1:2].sum() + y[-1]))


# Three-point Gauss-Legendre nodes and weights on [-1, 1].
_GL3_NODES = np.array([-math.sqrt(3.0 / 5.0), 0.0, math.sqrt(3.0 / 5.0)])
_GL3_WEIGHTS = np.array([5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0])


def gauss_legendre_3(f, a: float, b: float) -> float:
    """Three-point Gauss-Legendre on [a, b] (3 evaluations, exact to degree 5)."""
    mid = 0.5 * (a + b)
    half = 0.5 * (b - a)
    x = mid + half * _GL3_NODES
    return float(half * np.dot(_GL3_WEIGHTS, f(x)))


def gauss_legendre_composite(f, a: float, b: float, panels: int) -> float:
    """Composite three-point Gauss-Legendre with `panels` equal panels
    (3 * panels evaluations)."""
    edges = np.linspace(a, b, panels + 1)
    total = 0.0
    for i in range(panels):
        total += gauss_legendre_3(f, edges[i], edges[i + 1])
    return total


def main() -> None:
    I = exact_value()
    print(f"Exact value I = {I:.16f}")
    print(f"{'n':>6} {'trap err':>14} {'simp err':>14} {'gauss err':>14}")
    for k in range(1, 9):
        n = 2 ** k
        t_err = abs(trapezoidal(integrand, 0.0, 1.0, n) - I)
        s_err = abs(simpson(integrand, 0.0, 1.0, n) - I)
        # Gauss-Legendre on n//2 panels uses 3 * n/2 evaluations ~ 1.5 n.
        g_err = abs(gauss_legendre_composite(integrand, 0.0, 1.0,
                                             max(1, n // 4)) - I)
        print(f"{n:6d} {t_err:14.3e} {s_err:14.3e} {g_err:14.3e}")


if __name__ == "__main__":
    main()
