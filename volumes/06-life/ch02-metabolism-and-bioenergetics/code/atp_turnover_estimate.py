"""
Three independent estimates of an adult human's daily ATP turnover.

The chapter project asks the reader to estimate daily ATP turnover
three ways and to reconcile them to within a factor of two. This
script implements all three methods, prints intermediate quantities,
and reports a final reconciled value.

Method A: from food-energy intake and capture efficiency.
Method B: from cell count and per-cell ATP hydrolysis rate.
Method C: from oxygen consumption and the P/O ratio.

Dependencies: standard library only.

Usage:
    python atp_turnover_estimate.py

Supports Vol VI Chapter 2, Section 2.1 (ATP currency), the second
estimation block (foreshadow), and the chapter project.
"""

from __future__ import annotations


KCAL_TO_J = 4184.0          # joules per kilocalorie
ATP_MOLAR_MASS = 507.18     # g/mol of ATP (free acid)
F_KJ_PER_MOL = 50.0         # cellular free energy of ATP hydrolysis, kJ/mol
SECONDS_PER_DAY = 86_400


def method_a_food_energy(
    intake_kcal_per_day: float = 2000.0,
    capture_efficiency: float = 0.40,
) -> dict[str, float]:
    """Method A: from food energy in and overall capture efficiency.

    Most of the chemical energy in food appears as ATP via oxidative
    phosphorylation; the remainder is dissipated as catabolic heat.
    The overall food-to-ATP efficiency is ~30-40% depending on substrate
    mix and uncoupling.
    """
    intake_j = intake_kcal_per_day * KCAL_TO_J
    captured_j = capture_efficiency * intake_j
    moles_atp = captured_j / (F_KJ_PER_MOL * 1e3)
    grams_atp = moles_atp * ATP_MOLAR_MASS
    return {
        "intake_J_per_day": intake_j,
        "captured_J_per_day": captured_j,
        "moles_ATP_per_day": moles_atp,
        "kg_ATP_per_day": grams_atp / 1000.0,
    }


def method_b_cell_count(
    cell_count: float = 4e13,
    atp_per_cell_per_second: float = 1e7,
) -> dict[str, float]:
    """Method B: from total cell count and per-cell ATP hydrolysis.

    The body holds ~4e13 cells (Bianconi 2013); the average cell
    hydrolyses ATP at ~1e7 molecules/s, weighted toward muscle, brain,
    and liver. The number multiplies up to a body-wide rate.
    """
    n_avogadro = 6.022e23
    atp_per_second = cell_count * atp_per_cell_per_second
    moles_atp = atp_per_second * SECONDS_PER_DAY / n_avogadro
    grams_atp = moles_atp * ATP_MOLAR_MASS
    return {
        "ATP_molecules_per_second": atp_per_second,
        "moles_ATP_per_day": moles_atp,
        "kg_ATP_per_day": grams_atp / 1000.0,
    }


def method_c_oxygen(
    o2_ml_per_min: float = 250.0,
    p_to_o_ratio: float = 2.5,
) -> dict[str, float]:
    """Method C: from O2 consumption and the P/O ratio.

    Resting humans consume ~250 mL O2/min. Each O2 reduced to water
    accepts 4 electrons; with P/O = 2.5 (2.5 ATP per pair of electrons,
    or 5 ATP per O2), the molar ATP yield follows.
    """
    o2_l_per_day = o2_ml_per_min * 1440 / 1000.0
    o2_mol_per_day = o2_l_per_day / 22.4   # STP molar volume
    atp_per_o2 = 2.0 * p_to_o_ratio        # 2 electron pairs per O2
    moles_atp = o2_mol_per_day * atp_per_o2
    grams_atp = moles_atp * ATP_MOLAR_MASS
    return {
        "O2_mol_per_day": o2_mol_per_day,
        "ATP_per_O2": atp_per_o2,
        "moles_ATP_per_day": moles_atp,
        "kg_ATP_per_day": grams_atp / 1000.0,
    }


def reconcile(*estimates: dict[str, float]) -> tuple[float, float]:
    """Return mean and (max - min) range of the three kg/day estimates."""
    values = [e["kg_ATP_per_day"] for e in estimates]
    mean = sum(values) / len(values)
    spread = max(values) - min(values)
    return mean, spread


def main() -> None:
    a = method_a_food_energy()
    b = method_b_cell_count()
    c = method_c_oxygen()
    print("Method A (food energy):")
    for k, v in a.items():
        print(f"  {k}: {v:.3g}")
    print("Method B (cell count):")
    for k, v in b.items():
        print(f"  {k}: {v:.3g}")
    print("Method C (oxygen consumption):")
    for k, v in c.items():
        print(f"  {k}: {v:.3g}")
    mean, spread = reconcile(a, b, c)
    print()
    print(f"Reconciled mean: {mean:.1f} kg ATP/day")
    print(f"Spread (max - min): {spread:.1f} kg/day")
    print("Textbook value: ~50 kg/day (Lehninger ch. 13)")


if __name__ == "__main__":
    main()
