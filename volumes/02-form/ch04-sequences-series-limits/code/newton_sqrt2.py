# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Newton's iteration for sqrt(2) starting from a_0 = 1.

The iteration a_{n+1} = a_n - (a_n^2 - 2) / (2 a_n) = (a_n + 2/a_n) / 2
converges quadratically to sqrt(2). The residual a_n^2 - 2
approximately squares at each step. The script tabulates a_n and the
residual for n = 0, 1, ..., 6.
"""

import math


def main() -> None:
    a = 1.0
    print(f"{'n':>3}  {'a_n':>22}  {'residual a_n^2 - 2':>22}")
    for n in range(7):
        residual = a * a - 2.0
        print(f"{n:>3d}  {a:>22.16f}  {residual:>22.3e}")
        a = (a + 2.0 / a) / 2.0
    # Final reference
    print(f"\nreference sqrt(2) = {math.sqrt(2.0):.16f}")


if __name__ == "__main__":
    main()
