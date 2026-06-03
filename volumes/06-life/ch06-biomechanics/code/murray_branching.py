# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Murray's law for cardiovascular branching: radii, areas, and velocities.

Murray (1926) derived the diameter constraint at a vascular bifurcation
by minimising the sum of metabolic maintenance cost (proportional to
the lumen volume) and the Poiseuille pumping work (inversely
proportional to d^4). The result for a symmetric bifurcation is

    d_parent^3 = d_1^3 + d_2^3,

so a symmetric daughter has d_d / d_p = 2^(-1/3) ~ 0.794. The optimal
bifurcation half-angle (each daughter) is theta with
cos(2 theta) = 2^(1/3) - 1, so theta ~ 37.5 deg.

This script tabulates the radius hierarchy of an n-generation symmetric
tree and computes the total cross-sectional area, blood velocity, and
Reynolds number at each generation, for a typical adult human
cardiovascular system.

Reference: Murray (1926); LaBarbera (1990); Sherman (1981).

Run: uv run murray_branching.py
"""
from __future__ import annotations
import math


def symmetric_ratio() -> float:
    return 2.0 ** (-1.0 / 3.0)


def symmetric_angle_deg() -> float:
    return 0.5 * math.degrees(math.acos(2.0 ** (1.0 / 3.0) - 1.0))


def hierarchy(d_root_m: float, Q_root_m3s: float, n_gens: int = 24,
              mu: float = 4e-3, rho: float = 1060.0) -> None:
    """Print radius, area, velocity, Reynolds for each generation."""
    ratio = symmetric_ratio()
    print(f"{'gen':>3} {'d (mm)':>9} {'n vessels':>10} {'A_tot (cm^2)':>13} "
          f"{'v (cm/s)':>9} {'Re':>9}")
    d = d_root_m
    for g in range(n_gens + 1):
        n = 2 ** g
        A_single = math.pi * (d / 2.0) ** 2
        A_tot = n * A_single
        v = Q_root_m3s / A_tot
        Re = rho * v * d / mu
        print(f"{g:>3} {d*1e3:9.4f} {n:>10d} {A_tot*1e4:13.2f} "
              f"{v*100:9.4f} {Re:9.4f}")
        d *= ratio


def main() -> None:
    print("Murray's law constants:")
    print(f"  d_daughter / d_parent (symmetric) = 2^(-1/3) = {symmetric_ratio():.4f}")
    print(f"  optimal symmetric half-angle      = {symmetric_angle_deg():.2f} deg")
    print()
    # Adult human: aorta diameter 25 mm, cardiac output 5 L/min = 8.33e-5 m^3/s
    d_root = 25e-3
    Q = 5.0 / 60.0 / 1000.0  # m^3/s
    print(f"Symmetric tree from aorta (d = {d_root*1e3:.1f} mm), Q = {Q*1e6:.0f} mL/s:\n")
    hierarchy(d_root, Q, n_gens=24)


if __name__ == "__main__":
    main()
