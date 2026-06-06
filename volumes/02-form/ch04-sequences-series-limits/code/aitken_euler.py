# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Convergence acceleration of slowly convergent series.

Two transforms turn a slowly convergent series into a fast one by
modelling the tail rather than summing it:

  - Aitken's Delta^2 process, which assumes a geometric tail
    S_n ~ S + A r^n and eliminates A and r from three partial sums.
  - Euler's transform of an alternating series, which sums the
    forward differences of the term magnitudes with a 2^-(k+1)
    weight.

This script runs both on the Leibniz series for pi/4 and the
alternating series for log 2, and reports the term count each route
needs for six-decimal accuracy. It also writes the per-step error of
the raw, Aitken, and Euler estimates for pi/4 to a CSV so the figure
fig-acceleration can be checked.
"""

import csv
import math
from pathlib import Path

TARGET = 5e-7  # six-decimal accuracy threshold


def leibniz_partials(n_terms: int) -> list[float]:
    """Partial sums of pi/4 = 1 - 1/3 + 1/5 - 1/7 + ..."""
    partials = []
    s = 0.0
    for k in range(n_terms):
        s += (-1.0) ** k / (2 * k + 1)
        partials.append(s)
    return partials


def log2_partials(n_terms: int) -> list[float]:
    """Partial sums of log 2 = 1 - 1/2 + 1/3 - 1/4 + ..."""
    partials = []
    s = 0.0
    for k in range(n_terms):
        s += (-1.0) ** k / (k + 1)
        partials.append(s)
    return partials


def aitken(seq: list[float]) -> list[float]:
    """Aitken Delta^2 acceleration of a sequence."""
    out = []
    for n in range(len(seq) - 2):
        d1 = seq[n + 1] - seq[n]
        d2 = seq[n + 2] - 2 * seq[n + 1] + seq[n]
        if d2 == 0.0:
            out.append(seq[n + 2])
        else:
            out.append(seq[n] - d1 * d1 / d2)
    return out


def euler_alternating(terms: list[float]) -> float:
    """Euler transform of sum (-1)^n a_n given the a_n (positive)."""
    # forward differences Delta^k a_0
    total = 0.0
    diffs = list(terms)
    for k in range(len(terms)):
        total += ((-1.0) ** k) / (2 ** (k + 1)) * diffs[0]
        diffs = [diffs[j + 1] - diffs[j] for j in range(len(diffs) - 1)]
        if not diffs:
            break
    return total


def first_within(seq: list[float], true: float) -> int:
    for i, v in enumerate(seq):
        if abs(v - true) < TARGET:
            return i + 1
    return -1


def main() -> None:
    pi4 = math.pi / 4
    ln2 = math.log(2)

    raw_pi = leibniz_partials(40)
    aitk_pi = aitken(raw_pi)
    aitk_pi2 = aitken(aitk_pi)

    print("pi/4 acceleration:")
    print(f"  raw terms for 6 decimals:     {first_within(raw_pi, pi4)}")
    print(f"  Aitken (once):                {first_within(aitk_pi, pi4)}")
    print(f"  Aitken (iterated twice):      {first_within(aitk_pi2, pi4)}")

    # Euler transform of log 2 with increasing term counts
    print("log 2 acceleration (Euler transform):")
    for n in (4, 6, 8, 10, 12):
        a = [1.0 / (k + 1) for k in range(n)]
        est = euler_alternating(a)
        print(f"  {n:>2d} Euler terms: estimate {est:.10f}  err {abs(est-ln2):.2e}")

    # write per-step error for the figure
    out = Path(__file__).resolve().parents[1] / "data" / "acceleration_compare.csv"
    with out.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["n_terms", "raw_err", "aitken_err", "euler_err"])
        for n in range(2, 15):
            raw = leibniz_partials(n)
            raw_err = abs(raw[-1] - pi4)
            ak = aitken(raw)
            ak_err = abs(ak[-1] - pi4) if ak else float("nan")
            a = [1.0 / (2 * k + 1) for k in range(n)]
            eu_err = abs(euler_alternating(a) - pi4)
            w.writerow([n, f"{raw_err:.3e}", f"{ak_err:.3e}", f"{eu_err:.3e}"])
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
