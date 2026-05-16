# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Density-from-mass-and-volume uncertainty propagation.

Computes density rho = m / V and propagates its standard uncertainty
two ways:

    (1) the analytical product-of-powers rule from Chapter 4,
    (2) a Monte Carlo simulation with Gaussian inputs.

The two agree in the small-relative-uncertainty regime; when the
relative uncertainty of either input approaches 10 percent or more,
the Monte Carlo estimate is the more honest one.
"""

from __future__ import annotations

import math

import numpy as np

RNG = np.random.default_rng(207)
N_SAMPLES = 200_000

# Worked example: a metal sample suspected to be aluminium or brass.
# Mass in grams, volume in millilitres (== cm^3).
M_NOM, M_SD = 138.5, 0.5   # grams
V_NOM, V_SD = 17.4, 0.6    # millilitres


def main() -> None:
    rho_nom = M_NOM / V_NOM  # g/cm^3

    # Analytical: product-of-powers, exponents (+1) on m, (-1) on V
    rel_m = M_SD / M_NOM
    rel_V = V_SD / V_NOM
    rel_rho_lin = math.sqrt(rel_m**2 + rel_V**2)
    u_rho_lin = rho_nom * rel_rho_lin

    # Monte Carlo
    m = RNG.normal(M_NOM, M_SD, size=N_SAMPLES)
    V = RNG.normal(V_NOM, V_SD, size=N_SAMPLES)
    # Filter out non-physical negative-volume draws (rare but safe)
    mask = V > 0
    rho_mc = m[mask] / V[mask]

    print(f"nominal density          : {rho_nom:.4f}  g/cm^3")
    print(f"relative u(m)            : {rel_m:.4f}")
    print(f"relative u(V)            : {rel_V:.4f}")
    print(f"linear-propagation u(rho): {u_rho_lin:.4f}  g/cm^3")
    print(f"Monte Carlo mean rho     : {rho_mc.mean():.4f}  g/cm^3")
    print(f"Monte Carlo sd rho       : {rho_mc.std(ddof=1):.4f}  g/cm^3")
    print(f"ratio (MC / linear)      : {rho_mc.std(ddof=1) / u_rho_lin:.4f}")

    # Identification table for common metals (rho in g/cm^3)
    references = {
        "aluminium":     2.70,
        "iron / steel":  7.85,
        "brass":         8.50,
        "copper":        8.96,
        "lead":         11.34,
    }
    print()
    print("Identification (mean +- 2 sd vs reference densities):")
    lo = rho_nom - 2 * u_rho_lin
    hi = rho_nom + 2 * u_rho_lin
    for name, ref in references.items():
        compatible = "yes" if lo <= ref <= hi else "no"
        print(f"  {name:14s} {ref:5.2f}   in [{lo:.2f}, {hi:.2f}]?  {compatible}")


if __name__ == "__main__":
    main()
