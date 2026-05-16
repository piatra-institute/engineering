"""
Numerical verification of the Buckingham-pi result for the simple
pendulum: T * sqrt(g/L) = 2*pi (small-amplitude limit).

Integrates the linear pendulum ODE for 10 (L, g) combinations and
checks T * sqrt(g/L) against the analytical value.

Dependencies:
  numpy

Usage:
  python pendulum_pi.py
"""

import math
import numpy as np


def linear_pendulum_period(length: float, gravity: float,
                           amplitude: float = 0.05) -> float:
    """Integrate the small-amplitude pendulum and return the period
    measured from zero-crossings."""
    omega2 = gravity / length
    omega = math.sqrt(omega2)
    # Use a high-resolution leapfrog over ~5 periods
    t_max = 5.0 * 2.0 * math.pi / omega
    dt = t_max / 50000
    theta = amplitude
    theta_dot = 0.0
    t = 0.0
    crossings = []
    prev_sign = 1
    while t < t_max:
        theta_dotdot = -omega2 * theta
        theta_dot += theta_dotdot * dt
        theta += theta_dot * dt
        t += dt
        sign = 1 if theta >= 0 else -1
        if sign != prev_sign:
            crossings.append(t)
            prev_sign = sign
    # Period = 2 * average gap between consecutive zero-crossings
    if len(crossings) < 2:
        raise RuntimeError("not enough zero crossings")
    gaps = np.diff(crossings)
    return float(2 * gaps.mean())


def main() -> None:
    rng = np.random.default_rng(seed=20260516)
    combos = []
    for _ in range(10):
        L = rng.uniform(0.1, 10.0)
        g = rng.uniform(3.0, 30.0)
        combos.append((L, g))

    print(f"{'L (m)':>10} {'g (m/s^2)':>12} {'T (s)':>10} "
          f"{'T*sqrt(g/L)':>14} {'expected 2pi':>14}")
    for L, g in combos:
        T = linear_pendulum_period(L, g)
        pi_value = T * math.sqrt(g / L)
        print(f"{L:10.4f} {g:12.4f} {T:10.4f} {pi_value:14.6f} "
              f"{2.0 * math.pi:14.6f}")


if __name__ == "__main__":
    main()
