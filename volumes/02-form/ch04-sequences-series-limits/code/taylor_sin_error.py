# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Empirical truncation error for the Taylor polynomial of sin at 0.

Tabulates |sin x - T_n(x)| for n = 1, 3, 5, 7, 9 against the
Lagrange remainder bound |x|^{n+1}/(n+1)! at x = 0.5, 1.0, 1.5, 2.0.
The bound uses M_{n+1} = 1 since |sin^{(k)}| <= 1 everywhere.
"""

import math


def taylor_sin(x: float, order: int) -> float:
    """Maclaurin polynomial of sin to given odd order. Order in {1,3,5,7,9}."""
    s = 0.0
    sign = 1.0
    for k in range(0, (order + 1) // 2):
        power = 2 * k + 1
        s += sign * (x**power) / math.factorial(power)
        sign = -sign
    return s


def main() -> None:
    xs = (0.5, 1.0, 1.5, 2.0)
    orders = (1, 3, 5, 7, 9)

    header = "x".rjust(8) + "  order".rjust(8) + "  empirical err".rjust(16) + "  Lagrange bound".rjust(16)
    print(header)
    for x in xs:
        for n in orders:
            empirical = abs(math.sin(x) - taylor_sin(x, n))
            bound = x**(n + 1) / math.factorial(n + 1)
            print(f"{x:>8.2f}  {n:>6d}  {empirical:>16.3e}  {bound:>16.3e}")


if __name__ == "__main__":
    main()
