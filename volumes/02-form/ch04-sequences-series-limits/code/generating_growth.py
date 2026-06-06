# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Recurrence solved by a generating function: a run-length-limited code.

A serial link forbids two consecutive zeros to keep clock recovery
locked. The number of valid binary words of length n is a_n, and the
case-split on the final symbol gives the recurrence

    a_n = a_{n-1} + a_{n-2},   a_0 = 1, a_1 = 2,

so a_n = F_{n+2}, the shifted Fibonacci numbers. The generating function

    A(x) = (1 + x) / (1 - x - x^2)

has its dominant pole at x = 1/phi, so a_n ~ C phi^n and the payload
capacity is log2(phi) ~ 0.694 bits per symbol.

This script runs the recurrence, the closed form, and the dominant-pole
asymptotic side by side, and writes log2(a_n) with the asymptotic line to
a CSV so fig-generating-growth can be checked.
"""

import csv
import math
from pathlib import Path

PHI = (1.0 + math.sqrt(5.0)) / 2.0
PSI = (1.0 - math.sqrt(5.0)) / 2.0
C = (1.0 + PHI) / math.sqrt(5.0)  # coefficient of phi^n in a_n
D = -(1.0 + PSI) / math.sqrt(5.0)  # coefficient of psi^n


def recurrence(n_max: int) -> list[int]:
    """a_n by direct recurrence with a_0 = 1, a_1 = 2."""
    a = [1, 2]
    for n in range(2, n_max + 1):
        a.append(a[-1] + a[-2])
    return a[: n_max + 1]


def closed_form(n: int) -> float:
    """a_n = C phi^n + D psi^n (equals F_{n+2})."""
    return C * PHI**n + D * PSI**n


def asymptotic(n: int) -> float:
    """Dominant-pole asymptotic a_n ~ C phi^n (drops the psi^n term)."""
    return C * PHI**n


def main() -> None:
    n_max = 12
    a = recurrence(n_max)

    print(" n   a_n(recur)   closed-form     C*phi^n      log2(a_n)")
    for n in range(n_max + 1):
        print(
            f"{n:>2d}   {a[n]:>9d}   {closed_form(n):>12.4f}   "
            f"{asymptotic(n):>10.4f}   {math.log2(a[n]):>9.4f}"
        )

    cap = math.log2(PHI)
    print(f"\nper-symbol capacity log2(phi) = {cap:.4f} bits")
    print(f"unconstrained capacity         = 1.0000 bits")
    print(f"rate penalty                   = {1.0 - cap:.4f} bits ({(1.0-cap)*100:.1f}%)")

    out = Path(__file__).resolve().parents[1] / "data" / "generating_growth.csv"
    with out.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["n", "a_n", "log2_a_n", "asymptotic_line"])
        intercept = math.log2(C)
        for n in range(n_max + 1):
            line = n * cap + intercept
            w.writerow([n, a[n], f"{math.log2(a[n]):.6f}", f"{line:.6f}"])
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
