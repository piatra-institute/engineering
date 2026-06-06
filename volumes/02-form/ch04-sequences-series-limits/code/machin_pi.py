# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Compute pi to ten decimals by Machin's formula, with an error budget.

  pi/4 = 4 arctan(1/5) - arctan(1/239)

Each arctangent is an alternating series arctan(x) = sum (-1)^k
x^(2k+1)/(2k+1), converging geometrically at rate x^2. The script
applies the truncation budget of the case study: each arctangent is
summed until the next-term bound falls below an allotted tolerance,
then the two are combined. It prints each term, the running sum, the
truncation point, and the empirical error against a high-precision
reference, and writes the budget table to data/machin_pi_budget.csv.
"""

import csv
import math
from pathlib import Path

PI_REF = 3.14159265358979323846
PER_SERIES_TOL = 5e-12  # allotment per arctangent term bound


def arctan_budget(x: float, weight: float) -> tuple[float, int, list]:
    """Sum arctan(x) until next-term bound < PER_SERIES_TOL/weight.

    Returns (value, terms_used, rows) where rows logs each term.
    Summed smallest-first is unnecessary here (terms already shrink),
    so we accumulate directly and report the bound at each step.
    """
    tol = PER_SERIES_TOL / weight
    rows = []
    s = 0.0
    k = 0
    while True:
        term = (-1.0) ** k * x ** (2 * k + 1) / (2 * k + 1)
        s += term
        next_bound = x ** (2 * k + 3) / (2 * k + 3)
        rows.append((k, abs(term), s, next_bound))
        if next_bound < tol:
            break
        k += 1
    return s, k + 1, rows


def main() -> None:
    a5, n5, rows5 = arctan_budget(1.0 / 5.0, weight=4.0)
    a239, n239, rows239 = arctan_budget(1.0 / 239.0, weight=1.0)

    pi_over_4 = 4 * a5 - a239
    pi = 4 * pi_over_4

    print(f"arctan(1/5)   = {a5:.15f}   ({n5} terms)")
    print(f"arctan(1/239) = {a239:.15f}   ({n239} terms)")
    print(f"pi/4          = {pi_over_4:.15f}")
    print(f"pi            = {pi:.15f}")
    print(f"reference     = {PI_REF:.15f}")
    print(f"abs error     = {abs(pi - PI_REF):.3e}")

    out = Path(__file__).resolve().parents[1] / "data" / "machin_pi_budget.csv"
    with out.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["series", "k", "term_magnitude", "partial_sum", "next_term_bound"])
        for k, t, s, b in rows5:
            w.writerow(["arctan_1_5", k, f"{t:.3e}", f"{s:.15f}", f"{b:.3e}"])
        for k, t, s, b in rows239:
            w.writerow(["arctan_1_239", k, f"{t:.3e}", f"{s:.15f}", f"{b:.3e}"])
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
