"""Normal-shock (Rankine-Hugoniot) relations for a perfect gas.

Given the upstream Mach number M1 > 1 and gamma, return the downstream
Mach number and the static and stagnation property ratios across the
shock.

    M2^2     = ((g-1)M1^2 + 2) / (2g M1^2 - (g-1))
    p2/p1    = 1 + 2g/(g+1) (M1^2 - 1)
    rho2/rho1= (g+1)M1^2 / ((g-1)M1^2 + 2)
    T2/T1    = (p2/p1)(rho1/rho2)
    p02/p01  = stagnation-pressure ratio (always < 1; entropy rises)

Used in Volume III, Chapter 13.
"""

from __future__ import annotations


def normal_shock(m1: float, gamma: float = 1.4) -> dict[str, float]:
    """Return downstream Mach and property ratios across a normal shock."""
    if m1 <= 1.0:
        raise ValueError("A normal shock requires supersonic upstream M1 > 1")
    g = gamma
    m1sq = m1 * m1
    m2sq = ((g - 1.0) * m1sq + 2.0) / (2.0 * g * m1sq - (g - 1.0))
    p_ratio = 1.0 + (2.0 * g / (g + 1.0)) * (m1sq - 1.0)
    rho_ratio = (g + 1.0) * m1sq / ((g - 1.0) * m1sq + 2.0)
    t_ratio = p_ratio / rho_ratio
    # stagnation-pressure ratio across the shock
    term1 = ((g + 1.0) * m1sq / ((g - 1.0) * m1sq + 2.0)) ** (g / (g - 1.0))
    term2 = ((g + 1.0) / (2.0 * g * m1sq - (g - 1.0))) ** (1.0 / (g - 1.0))
    p0_ratio = term1 * term2
    return {
        "M2": m2sq ** 0.5,
        "p2/p1": p_ratio,
        "rho2/rho1": rho_ratio,
        "T2/T1": t_ratio,
        "p02/p01": p0_ratio,
    }


if __name__ == "__main__":
    for m1 in (1.5, 2.0, 2.5, 3.0, 5.0):
        s = normal_shock(m1)
        print(
            f"M1={m1:4.1f}  M2={s['M2']:.4f}  p2/p1={s['p2/p1']:.3f}  "
            f"rho2/rho1={s['rho2/rho1']:.3f}  T2/T1={s['T2/T1']:.3f}  "
            f"p02/p01={s['p02/p01']:.4f}"
        )
