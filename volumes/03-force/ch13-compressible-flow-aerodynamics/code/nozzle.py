"""Converging-diverging nozzle design and off-design analysis.

Two services:
  1. design(): given a target exit Mach number, return the exit-to-throat
     area ratio from the area-Mach relation, and the choked mass flow per
     unit throat area for given stagnation conditions.
  2. mach_from_area(): invert the area-Mach relation to recover the Mach
     number on the subsonic or supersonic branch for a given A/A*.

Used in Volume III, Chapter 13.
"""

from __future__ import annotations

import math


def area_ratio(mach: float, gamma: float = 1.4) -> float:
    """A/A* from the area-Mach relation."""
    g = gamma
    t = 1.0 + 0.5 * (g - 1.0) * mach * mach
    exp = (g + 1.0) / (2.0 * (g - 1.0))
    return (1.0 / mach) * ((2.0 / (g + 1.0)) * t) ** exp


def mach_from_area(ar: float, gamma: float = 1.4,
                   supersonic: bool = True) -> float:
    """Invert A/A* = ar by bisection on the requested branch."""
    if ar < 1.0:
        raise ValueError("A/A* must be >= 1")
    if abs(ar - 1.0) < 1e-12:
        return 1.0
    if supersonic:
        lo, hi = 1.0 + 1e-6, 50.0
    else:
        lo, hi = 1e-6, 1.0 - 1e-6
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        f = area_ratio(mid, gamma) - ar
        # area_ratio is decreasing on subsonic branch, increasing on supersonic
        if supersonic:
            if f < 0:
                lo = mid
            else:
                hi = mid
        else:
            if f < 0:
                hi = mid
            else:
                lo = mid
    return 0.5 * (lo + hi)


def choked_mass_flux(p0: float, t0: float, gamma: float = 1.4,
                     r_gas: float = 287.0) -> float:
    """Choked mass flow per unit throat area, kg/(s m^2)."""
    g = gamma
    exp = (g + 1.0) / (2.0 * (g - 1.0))
    return (p0 / math.sqrt(t0)) * math.sqrt(g / r_gas) * (2.0 / (g + 1.0)) ** exp


if __name__ == "__main__":
    for me in (2.0, 3.0, 5.0):
        print(f"M_e={me}: A_e/A* = {area_ratio(me):.3f}")
    # design check: exit area ratio 4.0 -> supersonic root
    print("A/A*=4.0 supersonic M =", round(mach_from_area(4.0), 3))
    print("A/A*=4.0 subsonic  M =", round(mach_from_area(4.0, supersonic=False), 3))
    flux = choked_mass_flux(500e3, 400.0)
    print(f"choked mass flux at p0=500 kPa, T0=400 K: {flux:.2f} kg/(s m^2)")
