"""
Nernst potential and proton-motive force calculations.

For a cell or organelle that maintains an asymmetric distribution of
an ion across a membrane, the equilibrium electrical potential
difference is given by the Nernst equation. For the proton gradient
across the mitochondrial inner membrane, both the electrical and the
chemical components contribute to the proton-motive force.

Dependencies: standard library only.

Usage:
    python nernst_membrane_potential.py

Supports Vol VI Chapter 2, Section 2.2 (oxidative phosphorylation /
chemiosmosis) and the derivation exercise on PMF -> ATP coupling.
"""

from __future__ import annotations

import math

R = 8.314          # J / (mol K)
F = 96_485.0       # C / mol
T = 310.0          # K, body temperature


def nernst(c_out: float, c_in: float, z: int = 1, T_K: float = T) -> float:
    """Nernst equilibrium potential (V), inside-relative-to-outside,
    for an ion of charge z with c_out outside and c_in inside.

    Standard convention: positive value if positive charge accumulates
    outside relative to inside.
    """
    return (R * T_K) / (z * F) * math.log(c_out / c_in)


def proton_motive_force(
    delta_psi_mV: float = -150.0,
    delta_pH: float = 0.75,
    T_K: float = T,
) -> dict[str, float]:
    """Proton-motive force across mitochondrial inner membrane.

    Convention: matrix is negative and alkaline relative to the
    intermembrane space.
        delta_psi: membrane potential (mV), matrix-side relative to IMS
        delta_pH:  pH_matrix - pH_IMS  (typically ~0.5-1.0)
    PMF (mV) = delta_psi - (2.303 R T / F) * delta_pH.
    """
    chemical_mV = -(2.303 * R * T_K / F) * delta_pH * 1000
    pmf_mV = delta_psi_mV + chemical_mV
    dG_per_proton_kJ = (F * pmf_mV * 1e-3) / 1000.0   # convert to kJ/mol
    return {
        "delta_psi_mV": delta_psi_mV,
        "chemical_component_mV": chemical_mV,
        "pmf_mV": pmf_mV,
        "dG_per_proton_kJ_mol": dG_per_proton_kJ,
    }


def atp_synthase_coupling(
    pmf_kJ_per_proton: float,
    dG_atp_kJ: float = -55.0,
) -> dict[str, float]:
    """Minimum proton stoichiometry per ATP synthesised at ATP synthase.

    The synthase couples n protons (flowing down the PMF gradient) to
    one ATP synthesised (free energy +|dG_atp|). Thermodynamics requires
    n * |pmf| >= |dG_atp|. Returns the minimum n and the typical n.
    """
    n_min = abs(dG_atp_kJ) / abs(pmf_kJ_per_proton)
    return {
        "n_protons_min": n_min,
        "n_protons_typical": 3.0,
        "P_to_O_typical": 2.5,
    }


def main() -> None:
    pmf = proton_motive_force(delta_psi_mV=-150.0, delta_pH=0.75)
    for k, v in pmf.items():
        print(f"{k}: {v:.3g}")
    print()
    coupling = atp_synthase_coupling(pmf["dG_per_proton_kJ_mol"])
    for k, v in coupling.items():
        print(f"{k}: {v:.3g}")
    print()
    # Calcium gradient: cytosol 0.1 uM, extracellular 1 mM
    e_ca = nernst(c_out=1e-3, c_in=1e-7, z=2)
    print(f"Ca2+ Nernst potential (cyto vs ECF): {e_ca*1000:.0f} mV")
    # Potassium gradient: cytosol 140 mM, extracellular 5 mM
    e_k = nernst(c_out=5e-3, c_in=140e-3, z=1)
    print(f"K+ Nernst potential (cyto vs ECF): {e_k*1000:.0f} mV "
          "(close to resting potential)")


if __name__ == "__main__":
    main()
