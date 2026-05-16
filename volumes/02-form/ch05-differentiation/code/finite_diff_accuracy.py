# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Finite-difference accuracy sweep for f(x) = exp(x) at x = 1.

Compares forward and central differences against the exact derivative
exp(1) over a logarithmic sweep of step sizes. Prints a table of
step size, forward error, central error. Reveals the V-shaped
bias-variance tradeoff: small h is dominated by round-off, large h
by truncation, with an optimum near h* ~ eps^(1/2) for forward
and h* ~ eps^(1/3) for central in double precision.

Used by: Section 5.7 (Numerical differentiation, bias-variance tradeoff)
and Simulation exercise on step-size sweep for f(x) = e^x.
"""
from math import exp


def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h


def central_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2.0 * h)


def main() -> None:
    f = exp
    x = 1.0
    true = exp(1.0)
    print(f"{'h':>10} {'fwd error':>14} {'central error':>16}")
    print("-" * 44)
    for k in range(0, 16):
        h = 10 ** (-k)
        ef = abs(forward_diff(f, x, h) - true)
        ec = abs(central_diff(f, x, h) - true)
        print(f"{h:>10.1e} {ef:>14.3e} {ec:>16.3e}")


if __name__ == "__main__":
    main()
