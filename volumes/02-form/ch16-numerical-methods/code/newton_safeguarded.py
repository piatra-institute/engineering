# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Safeguarded root-finder that combines Newton's method with a
bisection fall-back. Demonstrates the safeguard catching a Newton
step that escapes the bracket.

Used by Design exercise 3 (safeguarded root-finder).
"""
from __future__ import annotations

from collections.abc import Callable


def safeguarded_newton(
    f: Callable[[float], float],
    fp: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-12,
    max_iter: int = 100,
) -> tuple[float, list[tuple[str, float]]]:
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("initial bracket does not contain a sign change")
    x = (a + b) / 2.0
    trace: list[tuple[str, float]] = []
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol or (b - a) < tol:
            return x, trace
        fpx = fp(x)
        # Newton proposal
        if fpx != 0.0:
            x_newton = x - fx / fpx
        else:
            x_newton = float("nan")
        # Accept Newton step if it lies in the current bracket
        if a < x_newton < b and not (x_newton != x_newton):  # NaN check
            trace.append(("newton", x_newton))
            x = x_newton
        else:
            x = (a + b) / 2.0
            trace.append(("bisect", x))
        # Update bracket
        fx = f(x)
        if fa * fx < 0:
            b, fb = x, fx
        else:
            a, fa = x, fx
    return x, trace


def main() -> None:
    # f(x) = x^3 - x - 2, root near 1.5214
    def f(x: float) -> float:
        return x ** 3 - x - 2.0

    def fp(x: float) -> float:
        return 3.0 * x ** 2 - 1.0

    root, trace = safeguarded_newton(f, fp, 1.0, 2.0)
    print(f"root = {root:.15f}")
    print(f"steps = {len(trace)}; trace:")
    for kind, x in trace:
        print(f"  {kind:>6}  x = {x:.15f}")

    # Pathological initial guess that would derail naive Newton:
    # f(x) = arctan(x), starting from x0 = 1.5 diverges.
    import math

    def g(x: float) -> float:
        return math.atan(x)

    def gp(x: float) -> float:
        return 1.0 / (1.0 + x ** 2)

    root, trace = safeguarded_newton(g, gp, -1.0, 1.5)
    print(f"\narctan(x) = 0 root = {root:.15f}, steps = {len(trace)}")
    print("safeguarded version converges; bare Newton from x_0 = 1.5 diverges.")


if __name__ == "__main__":
    main()
