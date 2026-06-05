# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Fixed-point iteration a_{n+1} = cos(a_n) toward the Dottie number.

The map g(a) = cos(a) has a unique real fixed point a* = 0.739085...,
the Dottie number. Since |g'(a*)| = |sin(a*)| = 0.6736 < 1, the
iteration converges linearly. The iterates alternate above and below
a* (the cobweb spirals inward) because g'(a*) < 0. This script prints
the iterate, the signed error, and the empirical contraction ratio
error_{n+1}/error_n, which settles to about 0.674.
"""

import math

A_STAR = 0.7390851332151607  # unique real solution of a = cos a


def main() -> None:
    a = 1.0
    prev_err = a - A_STAR
    print(f"{'n':>3}  {'a_n':>16}  {'error':>14}  {'ratio':>10}")
    for n in range(0, 36):
        err = a - A_STAR
        ratio = err / prev_err if n > 0 and prev_err != 0 else float("nan")
        print(f"{n:>3d}  {a:>16.12f}  {err:>14.3e}  {ratio:>10.4f}")
        prev_err = err
        a = math.cos(a)


if __name__ == "__main__":
    main()
