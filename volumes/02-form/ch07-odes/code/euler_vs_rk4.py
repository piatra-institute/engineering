"""
Compare forward Euler and classical RK4 on the test problem
y' = -y, y(0) = 1, exact solution y(t) = e^{-t}.

Supports:
  - Volume II, Chapter 7, Simulation exercise 1 (Euler vs RK4 scaling)
  - The step-size error analysis worked example in the chapter

Dependencies:
  numpy

Usage:
  python euler_vs_rk4.py [--t-final 1.0]

Output:
  A table of |y_num - y_exact| at t = t_final for both methods,
  across a geometric sequence of step sizes. The expected scaling
  is O(h) for forward Euler and O(h^4) for RK4.
"""

import argparse
import math

import numpy as np


def forward_euler(f, t0: float, y0: float, h: float, n_steps: int) -> float:
    """Advance the scalar IVP y' = f(t, y) from (t0, y0) by n_steps."""
    t, y = t0, y0
    for _ in range(n_steps):
        y = y + h * f(t, y)
        t = t + h
    return y


def rk4(f, t0: float, y0: float, h: float, n_steps: int) -> float:
    """Classical fourth-order Runge--Kutta, scalar IVP."""
    t, y = t0, y0
    for _ in range(n_steps):
        k1 = f(t, y)
        k2 = f(t + h / 2.0, y + h * k1 / 2.0)
        k3 = f(t + h / 2.0, y + h * k2 / 2.0)
        k4 = f(t + h, y + h * k3)
        y = y + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        t = t + h
    return y


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t-final", type=float, default=1.0)
    args = parser.parse_args()

    t_final = args.t_final
    y_exact = math.exp(-t_final)
    f = lambda t, y: -y

    step_sizes = [0.5, 0.1, 0.05, 0.01, 0.005, 0.001]

    print(f"{'h':>10}  {'|err Euler|':>14}  {'|err RK4|':>14}  "
          f"{'Euler/h':>12}  {'RK4/h^4':>14}")
    for h in step_sizes:
        n_steps = int(round(t_final / h))
        y_e = forward_euler(f, 0.0, 1.0, h, n_steps)
        y_r = rk4(f, 0.0, 1.0, h, n_steps)
        err_e = abs(y_e - y_exact)
        err_r = abs(y_r - y_exact)
        print(f"{h:>10.4f}  {err_e:>14.3e}  {err_r:>14.3e}  "
              f"{err_e/h:>12.3e}  {err_r/h**4:>14.3e}")


if __name__ == "__main__":
    main()
