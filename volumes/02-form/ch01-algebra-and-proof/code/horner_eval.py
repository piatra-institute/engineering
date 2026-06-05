# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Evaluate a polynomial by Horner's method and compare its operation
count and floating-point behaviour against the naive term-by-term sum.

Horner rewrites
    p(x) = a_n x^n + ... + a_1 x + a_0
as the nested form
    p(x) = (...((a_n x + a_{n-1}) x + a_{n-2}) x + ... ) x + a_0,
which uses n multiplications and n additions, against the naive form's
~2n multiplications (recomputing powers) or n extra storage. The nested
form is also better conditioned: it avoids forming large intermediate
powers x^k that the naive sum then cancels.

Supports Volume II, Chapter 1, section 1.1 (polynomials and the working
library) and the polynomial-evaluation worked example.

Usage:
  python horner_eval.py
"""

from __future__ import annotations


def horner(coeffs: list[float], x: float) -> float:
    """Evaluate sum_{k} coeffs[k] x^k with coeffs[0] the constant term.

    coeffs is ordered low-degree first: coeffs[i] multiplies x**i.
    """
    acc = 0.0
    for a in reversed(coeffs):
        acc = acc * x + a
    return acc


def naive(coeffs: list[float], x: float) -> float:
    """Evaluate the same polynomial term by term, recomputing powers."""
    total = 0.0
    for i, a in enumerate(coeffs):
        total += a * (x**i)
    return total


def horner_with_derivative(coeffs: list[float], x: float) -> tuple[float, float]:
    """Return (p(x), p'(x)) in one synthetic-division sweep.

    The derivative falls out of Horner for free: accumulate the running
    value and its running derivative together. This is the basis of the
    Newton-Horner root polish the reader meets in Chapter 16.
    """
    p = 0.0
    dp = 0.0
    for a in reversed(coeffs):
        dp = dp * x + p
        p = p * x + a
    return p, dp


def main() -> int:
    # p(x) = 1 + 6x + 15x^2 + 20x^3 + 15x^4 + 6x^5 + x^6 = (1+x)^6.
    coeffs = [1.0, 6.0, 15.0, 20.0, 15.0, 6.0, 1.0]
    for x in (0.05, 1.0, 2.0):
        h = horner(coeffs, x)
        n = naive(coeffs, x)
        exact = (1.0 + x) ** 6
        print(
            f"x={x:>5}: horner={h:.10f} naive={n:.10f} "
            f"(1+x)^6={exact:.10f}"
        )
        assert abs(h - exact) < 1e-9, "Horner disagrees with closed form"

    # Derivative check at x = 1: p(x) = (1+x)^6, p'(x) = 6(1+x)^5.
    p, dp = horner_with_derivative(coeffs, 1.0)
    assert abs(p - 2.0**6) < 1e-9
    assert abs(dp - 6.0 * 2.0**5) < 1e-9
    print(f"x=1: p={p:.1f} (=64), p'={dp:.1f} (=192) by synthetic sweep")
    print("Horner spot-checks pass.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
