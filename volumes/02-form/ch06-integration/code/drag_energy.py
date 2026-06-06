# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""
Aerodynamic drag energy over a measured drive cycle, by quadrature with
an error budget. Supports Volume II, Chapter 6, the drag-energy case
study and figure fig-drag-energy.

The instantaneous aerodynamic drag power dissipated by a vehicle moving
at speed v through still air is

    P(t) = 0.5 * rho * C_d * A * v(t)**3,

so the total drag energy over a drive cycle is the time integral

    E = int_0^T P(t) dt = 0.5 * rho * C_d * A * int_0^T v(t)**3 dt.

The drag coefficient C_d is weakly Reynolds-dependent across the cycle's
speed range; we model it as a mild ramp C_d(v) and integrate the full
v-dependent integrand to expose the difference from a constant-C_d
estimate.

Generates a 180 s speed trace at 1 Hz (urban-to-highway segment),
integrates the cubic-in-v drag-power integrand by the composite
trapezoidal rule, cross-checks by Simpson and by halving, and reports a
four-term error budget (speed-sensor scale, C_d uncertainty, frontal-
area uncertainty, air-density uncertainty).

Writes the trace to data/drag_trace.csv (columns: t_s, speed_mps,
drag_power_W, cumulative_energy_J).

Run directly with uv:
    uv run drag_energy.py
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np

# Physical constants and vehicle parameters (current as of 2026; these
# are representative of a mid-size passenger car).
RHO = 1.20          # air density, kg/m^3 (sea level, ~20 C)
C_D0 = 0.30         # baseline drag coefficient (dimensionless)
FRONTAL_AREA = 2.3  # frontal area A, m^2
DT = 1.0            # sampling interval, s


def speed_trace() -> np.ndarray:
    """A 181-sample (0..180 s) urban-to-highway speed profile in m/s.

    Built by linear interpolation between a handful of waypoints so the
    trace is reproducible and matches the figure.
    """
    t_pts = [0, 10, 25, 40, 55, 70, 85, 100, 115, 130, 145, 160, 175, 180]
    v_pts = [0, 5, 8, 6, 11, 9, 14, 22, 30, 33, 32, 33, 31, 28]
    t = np.arange(0, 181, DT)
    return np.interp(t, t_pts, v_pts)


def c_d(v: np.ndarray) -> np.ndarray:
    """Mildly speed-dependent drag coefficient.

    C_d falls slightly with Reynolds number across the speed range; we
    model a 5% drop from 0 to 35 m/s. The effect is small but it is the
    reason the constant-C_d estimate and the v-dependent integral differ.
    """
    return C_D0 * (1.0 - 0.05 * np.clip(v, 0, 35) / 35.0)


def drag_power(v: np.ndarray) -> np.ndarray:
    return 0.5 * RHO * c_d(v) * FRONTAL_AREA * v ** 3


def trapezoid(y: np.ndarray, dx: float) -> float:
    return dx * (0.5 * y[0] + y[1:-1].sum() + 0.5 * y[-1])


def simpson(y: np.ndarray, dx: float) -> float:
    n = len(y) - 1
    if n % 2:  # need an even number of panels; drop the last sample
        return simpson(y[:-1], dx) + 0.5 * dx * (y[-2] + y[-1])
    odd = y[1:-1:2].sum()
    even = y[2:-2:2].sum()
    return dx / 3.0 * (y[0] + 4 * odd + 2 * even + y[-1])


def main() -> None:
    t = np.arange(0, 181, DT)
    v = speed_trace()
    p = drag_power(v)

    # Total drag energy by trapezoidal rule.
    e_trap = trapezoid(p, DT)
    e_simp = simpson(p, DT)
    # Convergence by halving: integrate on every other sample.
    e_coarse = trapezoid(p[::2], 2 * DT)

    # Constant-C_d estimate, for comparison with the v-dependent C_d.
    p_const = 0.5 * RHO * C_D0 * FRONTAL_AREA * v ** 3
    e_const = trapezoid(p_const, DT)

    # Cumulative energy for the figure / data file.
    cum = np.concatenate(([0.0], np.cumsum(0.5 * (p[1:] + p[:-1]) * DT)))

    print(f"Drag energy (trapezoidal):     {e_trap/1e3:8.2f} kJ")
    print(f"Drag energy (Simpson):         {e_simp/1e3:8.2f} kJ")
    print(f"Drag energy (halved grid):     {e_coarse/1e3:8.2f} kJ")
    print(f"  trap-vs-Simpson difference:  {abs(e_trap-e_simp):8.2f} J "
          f"({abs(e_trap-e_simp)/e_trap*100:.3f}%)")
    print(f"  halving difference:          {abs(e_trap-e_coarse):8.2f} J "
          f"({abs(e_trap-e_coarse)/e_trap*100:.3f}%)")
    print(f"Constant-C_d estimate:         {e_const/1e3:8.2f} kJ "
          f"(+{(e_const-e_trap)/e_trap*100:.2f}% vs v-dependent)")

    # Error budget: relative uncertainties on each multiplicative factor.
    # The integrand is linear in rho, C_d, A and cubic in v, so a speed-
    # scale error u_v propagates as 3 u_v into the energy.
    u_rho = 0.03    # 3% air-density uncertainty (temperature, altitude)
    u_cd = 0.05     # 5% drag-coefficient uncertainty (yaw, surface state)
    u_area = 0.02   # 2% frontal-area uncertainty
    u_v_scale = 0.01  # 1% speed-sensor scale error -> 3% into energy
    u_speed = 3 * u_v_scale
    u_total = math.sqrt(u_rho**2 + u_cd**2 + u_area**2 + u_speed**2)
    print("\nError budget (relative, 1-sigma):")
    print(f"  air density rho:     {u_rho*100:5.1f}%")
    print(f"  drag coeff  C_d:     {u_cd*100:5.1f}%")
    print(f"  frontal area A:      {u_area*100:5.1f}%")
    print(f"  speed scale (x3):    {u_speed*100:5.1f}%  "
          f"(from {u_v_scale*100:.1f}% sensor scale, cubed weighting)")
    print(f"  combined (quadrature): {u_total*100:5.1f}%")
    print(f"  expanded (k=2):        {2*u_total*100:5.1f}%  "
          f"= +/- {2*u_total*e_trap/1e3:.2f} kJ")

    out = Path(__file__).resolve().parents[1] / "data" / "drag_trace.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["t_s", "speed_mps", "drag_power_W", "cumulative_energy_J"])
        for ti, vi, pi, ci in zip(t, v, p, cum):
            w.writerow([f"{ti:.0f}", f"{vi:.4f}", f"{pi:.4f}", f"{ci:.4f}"])
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
