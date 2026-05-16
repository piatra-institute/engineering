# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Alternating-harmonic partial sums vs log 2; verifies the
alternating-series error bound.

S_N = sum_{n=1}^{N} (-1)^{n+1}/n converges to log 2 = 0.693147...
The alternating-series test guarantees |S - S_N| <= b_{N+1} =
1/(N+1). The script prints S_N at N = 10, 100, 1000, 10000, the
true gap, and the bound 1/(N+1).
"""

import math


def alt_harmonic(n: int) -> float:
    s = 0.0
    sign = 1.0
    for k in range(1, n + 1):
        s += sign / k
        sign = -sign
    return s


def main() -> None:
    target = math.log(2.0)
    print(f"target log 2 = {target:.10f}")
    print(f"{'N':>10}  {'S_N':>14}  {'|S - S_N|':>14}  {'1/(N+1) bound':>14}")
    for n in (10, 100, 1_000, 10_000):
        sn = alt_harmonic(n)
        gap = abs(target - sn)
        bound = 1.0 / (n + 1)
        print(f"{n:>10d}  {sn:>14.10f}  {gap:>14.2e}  {bound:>14.2e}")


if __name__ == "__main__":
    main()
