# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Demonstrate catastrophic cancellation in sin(x) - x + x^3/6.

The naive form loses about two decimal digits per decade of x; the
Taylor-stable form keeps all binary64 digits.

Used by section 16.2 second estimation and Estimation exercise 14.
"""
from __future__ import annotations

import math


def naive(x: float) -> float:
    return math.sin(x) - x + x ** 3 / 6.0


def stable(x: float) -> float:
    # sin(x) = x - x^3/6 + x^5/120 - ...
    # sin(x) - x + x^3/6 = x^5/120 - x^7/5040 + ...
    # use the leading two terms; safe for |x| <= 1.
    return x ** 5 / 120.0 - x ** 7 / 5040.0


def main() -> None:
    print(f"{'x':>10} | {'naive':>16} | {'stable':>16} | {'rel err naive':>14}")
    print("-" * 66)
    for k in range(0, 13):
        x = 10.0 ** -k
        n = naive(x)
        s = stable(x)
        rel = abs(n - s) / abs(s) if s != 0 else float("nan")
        print(f"{x:>10.2e} | {n:>16.6e} | {s:>16.6e} | {rel:>14.2e}")


if __name__ == "__main__":
    main()
