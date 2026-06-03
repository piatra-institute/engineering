# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Bisection root finder, applied to two examples:

  1. The cubic p(x) = x^3 - 2 x - 5, whose real root sits near
     x = 2.094551 (the example Newton used to introduce his own
     method in De Analysi).
  2. The transcendental equation tan(x) = x in the interval
     (pi, 3 pi / 2), whose smallest positive root above pi is the
     first non-trivial solution that arises in waveguide cutoff
     calculations.

The script demonstrates the elementary root-finding loop the
chapter cites when motivating numerical methods (Volume II
Chapter 16 develops Newton, secant, and Brent in their proper
depth). Standard library only.

Supports Volume II, Chapter 2, Calculation exercises on roots and
Section 2.2's forward reference to numerical root finders.

Usage:
  python bisection_root.py
"""

from __future__ import annotations

import math
from typing import Callable


def bisect(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-10,
    max_iter: int = 200,
) -> tuple[float, int]:
    """Bisection root of f on [a, b]. Requires f(a) * f(b) < 0."""
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError(
            f"sign(f(a))={fa:.3e}, sign(f(b))={fb:.3e}; "
            "bisection requires opposite signs."
        )
    for n in range(max_iter):
        m = 0.5 * (a + b)
        fm = f(m)
        if abs(fm) < tol or 0.5 * (b - a) < tol:
            return m, n + 1
        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b), max_iter


def main() -> int:
    # Example 1: Newton's cubic.
    def p(x: float) -> float:
        return x * x * x - 2.0 * x - 5.0

    root1, n1 = bisect(p, 2.0, 3.0)
    print(f"x^3 - 2x - 5 = 0: root = {root1:.10f}  ({n1} iterations)")
    assert abs(root1 - 2.0945514815) < 1e-6, "Newton cubic root"

    # Example 2: tan(x) - x = 0, first root in (pi, 3 pi / 2).
    # The root sits near x = 4.4934.
    def q(x: float) -> float:
        return math.tan(x) - x

    # tan diverges at pi/2 + n pi; bracket just inside (pi, 3 pi / 2)
    # avoiding the asymptote.
    a = math.pi + 1e-6
    b = 1.5 * math.pi - 1e-6
    root2, n2 = bisect(q, a, b)
    print(f"tan(x) - x = 0:  root = {root2:.10f}  ({n2} iterations)")
    assert abs(root2 - 4.4934094579) < 1e-6, "transcendental root"

    print(
        "Bisection always converges when the bracket is honest. "
        "Convergence is linear (one bit per iteration); Newton's "
        "method (Volume II Chapter 16) is quadratic when it works "
        "and divergent when it doesn't."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
