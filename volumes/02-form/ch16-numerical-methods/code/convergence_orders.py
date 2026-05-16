# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Compute iteration-error traces for bisection, secant, and Newton on
f(x) = cos(x) - x = 0 and verify the convergence rates.

Used by Simulation exercise 1.
"""
from __future__ import annotations

import math


def bisection(a: float, b: float, n: int) -> list[float]:
    xs: list[float] = []
    fa = math.cos(a) - a
    for _ in range(n):
        c = (a + b) / 2.0
        xs.append(c)
        fc = math.cos(c) - c
        if fa * fc < 0:
            b = c
        else:
            a, fa = c, fc
    return xs


def newton(x0: float, n: int) -> list[float]:
    xs = [x0]
    x = x0
    for _ in range(n):
        x = x - (math.cos(x) - x) / (-math.sin(x) - 1.0)
        xs.append(x)
    return xs


def secant(x0: float, x1: float, n: int) -> list[float]:
    xs = [x0, x1]
    f0 = math.cos(x0) - x0
    f1 = math.cos(x1) - x1
    for _ in range(n):
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        xs.append(x2)
        x0, x1 = x1, x2
        f0, f1 = f1, math.cos(x2) - x2
    return xs


def main() -> None:
    # Reference root computed by SciPy-grade precision (40-iteration bisection):
    xstar = bisection(0.0, 1.0, 60)[-1]
    print(f"reference root x* = {xstar:.15f}")
    print()

    print(f"{'k':>3} | {'bisection err':>16} | {'secant err':>16} | {'newton err':>16}")
    print("-" * 60)
    bis = bisection(0.0, 1.0, 12)
    sec = secant(0.0, 1.0, 10)
    new = newton(0.5, 6)
    rows = max(len(bis), len(sec), len(new))
    for k in range(rows):
        b_err = abs(bis[k] - xstar) if k < len(bis) else float("nan")
        s_err = abs(sec[k] - xstar) if k < len(sec) else float("nan")
        n_err = abs(new[k] - xstar) if k < len(new) else float("nan")
        print(f"{k:>3} | {b_err:>16.6e} | {s_err:>16.6e} | {n_err:>16.6e}")


if __name__ == "__main__":
    main()
