"""
Finite-difference solution of the 1-D wave equation on a string,
verifying v = sqrt(T/mu) for three (T, mu) combinations.

Supports Volume I, Chapter 2, Simulation exercise on the wave speed.

Dependencies:
  numpy

Usage:
  python wave_speed.py
"""

import math
import numpy as np


def wave_speed_from_simulation(tension: float, mu: float,
                               length: float = 1.0,
                               n_x: int = 401) -> float:
    """Solve d^2u/dt^2 = (T/mu) d^2u/dx^2 with a Gaussian initial pulse
    and return the measured wave speed by tracking the pulse peak."""
    c_theory = math.sqrt(tension / mu)
    dx = length / (n_x - 1)
    # CFL condition: dt <= dx / c
    dt = 0.4 * dx / c_theory
    n_steps = int(0.5 * length / c_theory / dt)

    x = np.linspace(0, length, n_x)
    # Initial condition: Gaussian pulse near x = 0.2
    sigma = 0.03
    u_prev = np.exp(-((x - 0.2) / sigma) ** 2)
    u_curr = u_prev.copy()
    u_next = np.zeros_like(u_curr)

    c2_dt2_dx2 = (tension / mu) * (dt / dx) ** 2

    # Track the peak position over time
    peaks = []
    times = []
    for step in range(n_steps):
        u_next[1:-1] = (2 * u_curr[1:-1] - u_prev[1:-1]
                        + c2_dt2_dx2 * (u_curr[2:] - 2 * u_curr[1:-1]
                                        + u_curr[:-2]))
        u_next[0] = 0
        u_next[-1] = 0
        peaks.append(x[np.argmax(u_curr)])
        times.append(step * dt)
        u_prev = u_curr
        u_curr = u_next.copy()

    # Linear fit to peak position vs time
    peaks = np.array(peaks)
    times = np.array(times)
    # Use only the middle portion where the pulse has cleanly separated
    mask = (times > 0.1 * times[-1]) & (times < 0.8 * times[-1])
    slope, _ = np.polyfit(times[mask], peaks[mask], 1)
    return float(slope)


def main() -> None:
    combos = [
        (10.0, 0.01),
        (40.0, 0.04),
        (90.0, 0.01),
    ]
    print(f"{'T (N)':>10} {'mu (kg/m)':>12} {'v measured (m/s)':>20} "
          f"{'v theory (m/s)':>18}")
    for T, mu in combos:
        v_meas = wave_speed_from_simulation(T, mu)
        v_theory = math.sqrt(T / mu)
        print(f"{T:10.2f} {mu:12.4f} {v_meas:20.4f} {v_theory:18.4f}")


if __name__ == "__main__":
    main()
