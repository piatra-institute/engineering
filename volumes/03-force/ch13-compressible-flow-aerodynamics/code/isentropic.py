"""Isentropic flow relations for a calorically perfect gas.

Given a Mach number M and the ratio of specific heats gamma, return the
ratios of stagnation to static temperature, pressure, and density, plus
the area ratio A/A* from the area-Mach relation.

Reference relations (gamma = 1.4 for air):
    T0/T   = 1 + (g-1)/2 * M^2
    p0/p   = (T0/T)^(g/(g-1))
    rho0/r = (T0/T)^(1/(g-1))
    A/A*   = (1/M) * [ (2/(g+1)) (1 + (g-1)/2 M^2) ]^((g+1)/(2(g-1)))

Used in the worked examples and exercises of Volume III, Chapter 13.
"""

from __future__ import annotations


def isentropic_ratios(mach: float, gamma: float = 1.4) -> dict[str, float]:
    """Return stagnation-to-static ratios and the area ratio at given Mach."""
    if mach <= 0:
        raise ValueError("Mach number must be positive")
    g = gamma
    t0_over_t = 1.0 + 0.5 * (g - 1.0) * mach * mach
    p0_over_p = t0_over_t ** (g / (g - 1.0))
    rho0_over_rho = t0_over_t ** (1.0 / (g - 1.0))
    exponent = (g + 1.0) / (2.0 * (g - 1.0))
    a_over_astar = (1.0 / mach) * ((2.0 / (g + 1.0)) * t0_over_t) ** exponent
    return {
        "T0/T": t0_over_t,
        "p0/p": p0_over_p,
        "rho0/rho": rho0_over_rho,
        "A/Astar": a_over_astar,
    }


def critical_ratios(gamma: float = 1.4) -> dict[str, float]:
    """Return the sonic (M=1) static-to-stagnation ratios."""
    g = gamma
    return {
        "Tstar/T0": 2.0 / (g + 1.0),
        "pstar/p0": (2.0 / (g + 1.0)) ** (g / (g - 1.0)),
        "rhostar/rho0": (2.0 / (g + 1.0)) ** (1.0 / (g - 1.0)),
    }


if __name__ == "__main__":
    for m in (0.3, 0.8, 1.0, 2.0, 3.0):
        r = isentropic_ratios(m)
        print(
            f"M={m:4.1f}  T/T0={1/r['T0/T']:.4f}  p/p0={1/r['p0/p']:.4f}  "
            f"rho/rho0={1/r['rho0/rho']:.4f}  A/A*={r['A/Astar']:.4f}"
        )
    print("critical:", {k: round(v, 4) for k, v in critical_ratios().items()})
