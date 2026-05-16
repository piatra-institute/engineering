# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Partial sums of the harmonic series at decades, vs log N + gamma.

The harmonic partial sum H_N = 1 + 1/2 + ... + 1/N has the
asymptotic expansion H_N = log N + gamma + 1/(2N) - 1/(12 N^2)
+ O(1/N^4), where gamma is the Euler-Mascheroni constant. This
script prints H_N at N = 10^k for k = 1..6 and compares to the
asymptotic log N + gamma.
"""

import math

EULER_GAMMA = 0.57721566490153286060

def harmonic(n: int) -> float:
    """Sum 1/1 + 1/2 + ... + 1/n. Naive but exact to float precision."""
    s = 0.0
    for k in range(1, n + 1):
        s += 1.0 / k
    return s


def main() -> None:
    print(f"{'N':>10}  {'H_N':>14}  {'log N + gamma':>14}  {'difference':>14}")
    for k in range(1, 7):
        n = 10**k
        hn = harmonic(n)
        asymp = math.log(n) + EULER_GAMMA
        print(f"{n:>10d}  {hn:>14.6f}  {asymp:>14.6f}  {hn - asymp:>14.2e}")


if __name__ == "__main__":
    main()
