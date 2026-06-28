"""Air-standard cycle efficiencies: Carnot, Otto, Diesel, Brayton.

Closed-form efficiency formulas for the ideal cycles of this chapter, plus a
small table-printing driver. Used in sections 3.1 to 3.4 and several exercises.
All temperatures in kelvin; ratios dimensionless.
"""

from __future__ import annotations


def carnot_efficiency(t_hot, t_cold):
    """Carnot efficiency 1 - T_c/T_h for reservoir temperatures in kelvin."""
    return 1.0 - t_cold / t_hot


def otto_efficiency(r, gamma=1.4):
    """Otto-cycle efficiency 1 - r^-(gamma-1), r = compression ratio."""
    return 1.0 - r ** (-(gamma - 1.0))


def diesel_efficiency(r, r_c, gamma=1.4):
    """Diesel-cycle efficiency.

    r   compression ratio V1/V2
    r_c cut-off ratio V3/V2
    """
    bracket = (r_c ** gamma - 1.0) / (gamma * (r_c - 1.0))
    return 1.0 - r ** (-(gamma - 1.0)) * bracket


def brayton_efficiency(r_p, gamma=1.4):
    """Brayton-cycle efficiency 1 - r_p^-((gamma-1)/gamma)."""
    return 1.0 - r_p ** (-(gamma - 1.0) / gamma)


def carnot_cop_cooling(t_cold, t_hot):
    """Carnot refrigeration COP = T_c / (T_h - T_c)."""
    return t_cold / (t_hot - t_cold)


def carnot_cop_heating(t_cold, t_hot):
    """Carnot heat-pump COP = T_h / (T_h - T_c)."""
    return t_hot / (t_hot - t_cold)


if __name__ == "__main__":
    print("Otto efficiency vs compression ratio (gamma=1.4)")
    for r in (8, 9, 10, 12):
        print(f"  r={r:2d}  eta={otto_efficiency(r):.3f}")

    print("Diesel efficiency, r=18, vs cut-off ratio")
    for r_c in (2.0, 2.5, 3.0):
        print(f"  r_c={r_c:.1f}  eta={diesel_efficiency(18, r_c):.3f}")

    print("Brayton efficiency vs pressure ratio")
    for r_p in (5, 12, 15, 30, 50):
        print(f"  r_p={r_p:2d}  eta={brayton_efficiency(r_p):.3f}")

    print("Carnot bounds")
    print(f"  560C boiler, 30C condenser: eta={carnot_efficiency(833, 303):.3f}")
    print(f"  heat-pump COP, 35C/-5C: {carnot_cop_heating(268, 308):.2f}")
