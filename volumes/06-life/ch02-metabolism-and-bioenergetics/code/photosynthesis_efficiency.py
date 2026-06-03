"""
Photosynthesis efficiency calculations from quantum input to biomass
output, at four stages of accounting.

The chapter's worked example 3 walks through field-scale photosynthesis
efficiency. This script formalises the four-stage chain and reports
the maximum-theoretical, photochemical, biochemical, and field
efficiencies along with intermediate quantities.

Stages:
  1. Maximum theoretical (PAR fraction of solar input).
  2. Photochemical (quantum requirement: 8-10 photons per CO2 fixed).
  3. Biochemical (Calvin cycle ATP/NADPH costs).
  4. Field-scale (photorespiration, dark respiration, reflectance).

Dependencies: standard library only.

Usage:
    python photosynthesis_efficiency.py

Supports Vol VI Chapter 2, Sections 2.3 (photosynthesis) and 2.6
(worked example 3); the second estimation block (quantum maximum); and
the estimation exercise on algal photobioreactor productivity.
"""

from __future__ import annotations


PLANCK_J_S = 6.626e-34
SPEED_LIGHT_M_S = 2.998e8
AVOGADRO = 6.022e23
KJ_PER_MOL_GLUCOSE = 2870.0   # standard free energy of complete oxidation
GLUCOSE_KJ_PER_GRAM = 15.6


def photon_energy_J(wavelength_nm: float) -> float:
    """Photon energy at the given wavelength."""
    wavelength_m = wavelength_nm * 1e-9
    return PLANCK_J_S * SPEED_LIGHT_M_S / wavelength_m


def quantum_maximum_efficiency(
    wavelength_nm: float = 680.0,
    photons_per_co2: int = 8,
    glucose_energy_kJ_per_mol: float = KJ_PER_MOL_GLUCOSE,
) -> float:
    """Maximum theoretical efficiency from photon energy to glucose
    free energy, accounting for the quantum requirement.

    Glucose synthesis requires 6 CO2; if each CO2 costs `photons_per_co2`
    photons, then synthesising one mol glucose costs 6 * photons_per_co2
    mol of photons.
    """
    photon_J = photon_energy_J(wavelength_nm)
    photons_per_glucose = 6 * photons_per_co2
    input_kJ_per_glucose = photons_per_glucose * photon_J * AVOGADRO / 1000.0
    return glucose_energy_kJ_per_mol / input_kJ_per_glucose


def field_biomass_productivity(
    par_kWh_per_m2_per_day: float = 2.25,
    field_efficiency: float = 0.02,
    glucose_kJ_per_gram: float = GLUCOSE_KJ_PER_GRAM,
) -> dict[str, float]:
    """Field-scale daily biomass productivity in g/(m^2 day).

    Inputs: photosynthetically active radiation (PAR) at the canopy, in
    kWh/(m^2 day), and the field-integrated conversion efficiency.
    """
    captured_kJ = par_kWh_per_m2_per_day * 3600 * field_efficiency
    biomass_g = captured_kJ / glucose_kJ_per_gram
    return {
        "PAR_input_kJ_per_m2_per_day": par_kWh_per_m2_per_day * 3600,
        "captured_kJ_per_m2_per_day": captured_kJ,
        "biomass_g_per_m2_per_day": biomass_g,
        "biomass_kg_per_ha_per_day": biomass_g * 10,
        "biomass_t_per_ha_per_120day": biomass_g * 10 / 1000 * 120,
    }


def stage_summary() -> None:
    print("Stage 1 (max theoretical, 680 nm, 8 photons/CO2):")
    e1 = quantum_maximum_efficiency(680, 8)
    print(f"  efficiency = {100 * e1:.1f}%")
    print()
    print("Stage 2 (relaxed to 10 photons/CO2, accounting for ATP cost):")
    e2 = quantum_maximum_efficiency(680, 10)
    print(f"  efficiency = {100 * e2:.1f}%")
    print()
    print("Stage 3 (whole-spectrum PAR fraction ~45%):")
    e3 = 0.45 * e2
    print(f"  efficiency on incident solar = {100 * e3:.1f}%")
    print()
    print("Stage 4 (field-integrated for productive C4 crop, 2%):")
    field = field_biomass_productivity(par_kWh_per_m2_per_day=2.25,
                                       field_efficiency=0.02)
    for k, v in field.items():
        print(f"  {k}: {v:.2f}")


if __name__ == "__main__":
    stage_summary()
