# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Catastrophic cancellation in the direct Maclaurin series for e^{-x}.

Summing sum_n (-x)^n / n! for large positive x adds terms of
alternating sign whose magnitudes vastly exceed the tiny true value
e^{-x}. The required cancellation consumes all available double-
precision digits, and the computed sum is dominated by round-off,
sometimes returning a negative number or the wrong order of magnitude.
The stable route computes e^{+x} (all-positive series, no cancellation)
and takes the reciprocal. This script tabulates both for several x and
reports the relative error against math.exp(-x).
"""

import math


def exp_neg_direct(x: float, terms: int = 200) -> float:
    """Sum the Maclaurin series of e^{-x} directly: sum (-x)^n / n!."""
    total = 0.0
    term = 1.0  # (-x)^0 / 0!
    for n in range(terms):
        total += term
        term *= (-x) / (n + 1)
    return total


def exp_neg_stable(x: float, terms: int = 200) -> float:
    """Compute e^{+x} by the all-positive series, then reciprocate."""
    total = 0.0
    term = 1.0
    for n in range(terms):
        total += term
        term *= x / (n + 1)
    return 1.0 / total


def main() -> None:
    print(f"{'x':>5}  {'true e^-x':>14}  {'direct':>16}  "
          f"{'rel.err direct':>16}  {'stable':>14}  {'rel.err stable':>16}")
    for x in (5.0, 10.0, 20.0, 30.0, 40.0):
        true = math.exp(-x)
        d = exp_neg_direct(x)
        s = exp_neg_stable(x)
        rd = abs(d - true) / true
        rs = abs(s - true) / true
        print(f"{x:>5.0f}  {true:>14.6e}  {d:>16.6e}  {rd:>16.3e}  "
              f"{s:>14.6e}  {rs:>16.3e}")


if __name__ == "__main__":
    main()
