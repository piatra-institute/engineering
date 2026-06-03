"""
Nernst and Goldman-Hodgkin-Katz (GHK) equilibrium-potential calculator.

Computes the equilibrium potential for a single ion species (Nernst) and
the resting potential for a membrane permeable to multiple species
(GHK).  Reproduces canonical mammalian values at 310 K.

Supports:
  - Volume VI, Chapter 1, Calculation exercises on resting potential.
  - Volume VI, Chapter 1, Derivation exercise on the Nernst equation.

Dependencies:
  numpy (only used for log; can be replaced with math.log).

Usage:
  python membrane_voltage_nernst.py
"""

import numpy as np

# Physical constants.
R = 8.31446  # J / (mol K)
F = 96485.0  # C / mol
T_BODY = 310.0  # K (37 deg C)


def nernst(c_out: float, c_in: float, z: int = 1,
           T: float = T_BODY) -> float:
    """Equilibrium potential in volts for an ion with charge z and
    extracellular concentration c_out, intracellular c_in.
    """
    if c_out <= 0.0 or c_in <= 0.0:
        raise ValueError("Concentrations must be positive.")
    return (R * T / (z * F)) * np.log(c_out / c_in)


def ghk(perm: dict[str, float],
        c_out: dict[str, float],
        c_in: dict[str, float],
        T: float = T_BODY) -> float:
    """Goldman-Hodgkin-Katz resting potential in volts.

    perm: relative permeability of each species.
    c_out, c_in: concentrations (same units; ratio is what matters).
    Only K+, Na+, and Cl- supported in the canonical case.
    """
    # Cl- enters the numerator and denominator with reversed sense.
    num = perm["K"] * c_out["K"] + perm["Na"] * c_out["Na"] \
        + perm["Cl"] * c_in["Cl"]
    den = perm["K"] * c_in["K"] + perm["Na"] * c_in["Na"] \
        + perm["Cl"] * c_out["Cl"]
    return (R * T / F) * np.log(num / den)


def main() -> None:
    # Canonical mammalian-cell concentrations (mM).
    c_out = {"K": 4.0, "Na": 145.0, "Cl": 110.0, "Ca": 1.0}
    c_in = {"K": 140.0, "Na": 10.0, "Cl": 10.0, "Ca": 1.0e-4}

    print("# Single-ion Nernst potentials at T = 310 K (mV):")
    for ion, z in [("K", +1), ("Na", +1), ("Cl", -1), ("Ca", +2)]:
        v_mv = 1.0e3 * nernst(c_out[ion], c_in[ion], z=z)
        print(f"  E_{ion:<3s} = {v_mv:+7.1f} mV")

    print()
    print("# Resting potential by GHK, with K-dominant permeability "
          "(P_K : P_Na : P_Cl = 1 : 0.04 : 0.45):")
    perm = {"K": 1.0, "Na": 0.04, "Cl": 0.45}
    v_rest = 1.0e3 * ghk(perm, c_out, c_in)
    print(f"  V_rest = {v_rest:+7.1f} mV")

    # Reduction check: setting Na and Cl permeabilities to zero recovers
    # the Nernst equation for potassium.
    perm_k_only = {"K": 1.0, "Na": 0.0, "Cl": 0.0}
    v_k_only = 1.0e3 * ghk(perm_k_only, c_out, c_in)
    e_k = 1.0e3 * nernst(c_out["K"], c_in["K"], z=+1)
    print(f"  GHK with K-only: {v_k_only:+7.1f} mV "
          f"(should match E_K = {e_k:+7.1f} mV)")


if __name__ == "__main__":
    main()
