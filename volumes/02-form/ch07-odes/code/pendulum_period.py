"""
Numerical pendulum-period extraction across an amplitude grid.
Computes the period from zero-crossings of theta_dot, compares
against the small-angle prediction T_0 = 2*pi*sqrt(l/g) and the
first-correction prediction T_1 = T_0 * (1 + theta_0^2 / 16).

Reference for the exact period: T = (4/omega_0) * K(sin(theta_0/2)),
where K is the complete elliptic integral of the first kind.

Supports:
  - Volume II, Chapter 7, Project (the pendulum at large amplitudes)
  - Simulation exercise 6 (pendulum period extraction)

Dependencies:
  numpy (scipy optional, for the elliptic-integral cross-check)

Usage:
  python pendulum_period.py [--g 9.81 --l 1.0]
"""

import argparse
import math

import numpy as np


def pendulum_rhs(t: float, y: np.ndarray, g_over_l: float) -> np.ndarray:
    theta, omega = y
    return np.array([omega, -g_over_l * math.sin(theta)])


def rk4_step(f, t: float, y: np.ndarray, h: float) -> np.ndarray:
    k1 = f(t, y)
    k2 = f(t + h / 2.0, y + h * k1 / 2.0)
    k3 = f(t + h / 2.0, y + h * k2 / 2.0)
    k4 = f(t + h, y + h * k3)
    return y + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)


def extract_period(theta_history: np.ndarray, t_history: np.ndarray,
                   omega_history: np.ndarray) -> float:
    """Average period from negative-to-positive zero crossings of omega."""
    crossings = []
    for i in range(1, len(omega_history)):
        if omega_history[i - 1] < 0.0 and omega_history[i] >= 0.0:
            # linear interp
            frac = omega_history[i - 1] / (omega_history[i - 1] - omega_history[i])
            crossings.append(t_history[i - 1] + frac * (t_history[i] - t_history[i - 1]))
    if len(crossings) < 2:
        return float("nan")
    diffs = np.diff(crossings)
    return float(diffs.mean())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--g", type=float, default=9.81)
    parser.add_argument("--l", type=float, default=1.0)
    parser.add_argument("--h", type=float, default=0.001)
    args = parser.parse_args()

    g_over_l = args.g / args.l
    omega_0 = math.sqrt(g_over_l)
    T_0 = 2.0 * math.pi / omega_0

    amplitudes_deg = [5, 10, 20, 30, 45, 60, 75, 90]

    print(f"Small-angle period T_0 = {T_0:.4f} s")
    print()
    print(f"{'theta_0':>8}  {'T_num':>10}  {'T_1':>10}  {'T_0':>10}  "
          f"{'err_0 %':>10}  {'err_1 %':>10}")

    for amp_deg in amplitudes_deg:
        theta_0 = math.radians(amp_deg)
        T_1 = T_0 * (1.0 + theta_0**2 / 16.0)
        # integrate for enough periods
        T_span = 10.0 * T_1
        n_steps = int(round(T_span / args.h))
        y = np.array([theta_0, 0.0])
        ts = np.zeros(n_steps + 1)
        thetas = np.zeros(n_steps + 1)
        omegas = np.zeros(n_steps + 1)
        thetas[0] = y[0]
        omegas[0] = y[1]
        for i in range(n_steps):
            y = rk4_step(lambda t, yy: pendulum_rhs(t, yy, g_over_l),
                         ts[i], y, args.h)
            ts[i + 1] = ts[i] + args.h
            thetas[i + 1] = y[0]
            omegas[i + 1] = y[1]
        T_num = extract_period(thetas, ts, omegas)
        err_0 = (T_0 - T_num) / T_num * 100.0
        err_1 = (T_1 - T_num) / T_num * 100.0
        print(f"{amp_deg:>8d}  {T_num:>10.5f}  {T_1:>10.5f}  {T_0:>10.5f}  "
              f"{err_0:>10.3f}  {err_1:>10.3f}")


if __name__ == "__main__":
    main()
