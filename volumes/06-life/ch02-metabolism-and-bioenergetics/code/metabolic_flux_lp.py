"""
Flux balance analysis (FBA) on a toy six-reaction, four-metabolite
network as a linear program.

The network is the one drawn in fig-mfa-toy-network.tex:
   v1: ext -> A    (substrate uptake; bounded above by uptake limit)
   v2: A -> B
   v3: B -> C
   v4: B -> D
   v5: D -> C
   v6: C -> ext    (biomass; objective)

At steady state S v = 0 for all internal metabolites. The LP
maximises v6 subject to box constraints on each reaction.

Dependencies: standard library only (uses scipy.optimize.linprog if
available, falls back to a manual two-vertex analytic solution for
the toy network).

Usage:
    python metabolic_flux_lp.py

Supports Vol VI Chapter 2, Section 2.4 (metabolic flux analysis) and
the simulation exercise on FBA of a toy network.
"""

from __future__ import annotations


def fba_toy(
    v1_max: float = 10.0,
    v4_max: float = 8.0,
    v5_max: float = 8.0,
) -> dict[str, float]:
    """Solve the toy FBA LP analytically.

    Decision variables v = (v1, v2, v3, v4, v5, v6) >= 0.
    Mass balance:
      v1 - v2 = 0
      v2 - v3 - v4 = 0
      v3 + v5 - v6 = 0
      v4 - v5 = 0

    From these, v1 = v2, v4 = v5, and v6 = v3 + v5 = v2 = v1.
    So the biomass flux equals the substrate uptake, capped by v1_max
    and by the more restrictive of v4_max / v5_max (which equal each
    other in the constraint v4 = v5).

    For the toy problem the optimum is v6 = min(v1_max, v3_max + v5_max).
    """
    v1 = v1_max
    # Distribute B-flux: v2 = v1 = v3 + v4; with v4 = v5 capped at v5_max.
    v4 = min(v4_max, v5_max, v1 / 2.0)
    v3 = v1 - v4
    v5 = v4
    v6 = v3 + v5
    return {
        "v1": v1, "v2": v1, "v3": v3, "v4": v4, "v5": v5, "v6": v6,
        "objective_biomass": v6,
    }


def try_linprog_solve(
    v1_max: float = 10.0,
    v4_max: float = 8.0,
    v5_max: float = 8.0,
) -> dict[str, float] | None:
    """Solve with scipy.optimize.linprog if installed.

    Returns None if scipy is not available.
    """
    try:
        import numpy as np
        from scipy.optimize import linprog
    except ImportError:
        return None

    # min c^T v with -v6 (since linprog minimises)
    c = np.array([0, 0, 0, 0, 0, -1.0])
    # Equality constraints S v = 0
    S = np.array([
        [1, -1, 0, 0, 0, 0],     # A
        [0,  1, -1, -1, 0, 0],   # B
        [0,  0, 1, 0, 1, -1],    # C
        [0,  0, 0, 1, -1, 0],    # D
    ])
    b_eq = np.zeros(4)
    bounds = [(0, v1_max), (0, None), (0, None),
              (0, v4_max), (0, v5_max), (0, None)]
    result = linprog(c, A_eq=S, b_eq=b_eq, bounds=bounds, method="highs")
    if not result.success:
        return None
    v = result.x
    return {
        "v1": v[0], "v2": v[1], "v3": v[2], "v4": v[3], "v5": v[4],
        "v6": v[5], "objective_biomass": v[5],
    }


def main() -> None:
    print("Analytic FBA on the toy network (uptake 10, branch caps 8):")
    sol = fba_toy(v1_max=10.0, v4_max=8.0, v5_max=8.0)
    for k, v in sol.items():
        print(f"  {k}: {v:.2f}")

    sol2 = try_linprog_solve(v1_max=10.0, v4_max=8.0, v5_max=8.0)
    if sol2 is not None:
        print()
        print("scipy.linprog verification:")
        for k, v in sol2.items():
            print(f"  {k}: {v:.2f}")
    else:
        print()
        print("scipy not available; skipping linprog verification.")


if __name__ == "__main__":
    main()
