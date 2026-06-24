"""Prandtl-Meyer expansion and supersonic thin-airfoil (Ackeret) tools.

The Prandtl-Meyer function nu(M) gives the angle through which a sonic
flow must turn to reach Mach M by isentropic expansion:

    nu(M) = sqrt((g+1)/(g-1)) atan( sqrt((g-1)/(g+1)(M^2-1)) )
            - atan( sqrt(M^2 - 1) )

For a flow turning through an expansion angle dtheta from M1, solve
nu(M2) = nu(M1) + dtheta for M2.

The Ackeret linearised supersonic result for a flat plate at angle of
attack alpha (radians) gives Cl and the wave-drag Cd.

Used in Volume III, Chapter 13.
"""

from __future__ import annotations

import math


def prandtl_meyer(mach: float, gamma: float = 1.4) -> float:
    """Prandtl-Meyer angle nu(M) in radians for M >= 1."""
    if mach < 1.0:
        raise ValueError("Prandtl-Meyer function defined for M >= 1")
    g = gamma
    a = math.sqrt((g + 1.0) / (g - 1.0))
    b = math.sqrt((g - 1.0) / (g + 1.0) * (mach * mach - 1.0))
    return a * math.atan(b) - math.atan(math.sqrt(mach * mach - 1.0))


def mach_after_expansion(m1: float, turn: float, gamma: float = 1.4) -> float:
    """Mach number after isentropic expansion through angle turn (rad)."""
    target = prandtl_meyer(m1, gamma) + turn
    lo, hi = 1.0, 100.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if prandtl_meyer(mid, gamma) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def ackeret_flat_plate(mach: float, alpha: float) -> dict[str, float]:
    """Lift and wave-drag coefficients for a flat plate, Ackeret theory."""
    beta = math.sqrt(mach * mach - 1.0)
    cl = 4.0 * alpha / beta
    cd = 4.0 * alpha * alpha / beta
    return {"Cl": cl, "Cd_wave": cd, "L/D": cl / cd}


if __name__ == "__main__":
    print("nu(M=2) =", round(math.degrees(prandtl_meyer(2.0)), 3), "deg")
    m2 = mach_after_expansion(2.0, math.radians(10.0))
    print("M after 10 deg expansion from M=2:", round(m2, 4))
    res = ackeret_flat_plate(2.0, math.radians(3.0))
    print("flat plate M=2, alpha=3 deg:",
          {k: round(v, 4) for k, v in res.items()})
