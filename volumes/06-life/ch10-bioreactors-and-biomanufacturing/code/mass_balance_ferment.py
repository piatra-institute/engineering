# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Close a household-scale fermentation mass balance (chapter project).

Two routines:

1. sauerkraut_balance(cabbage_kg, salt_g, target_pct):
   - reports salt mass fraction, brine water displaced, expected
     CO2 release per kg cabbage from heterolactic fermentation, and a
     conservative biomass-yield estimate.

2. sugar_yeast_balance(sugar_g, water_g):
   - reports ethanol theoretical yield (Gay-Lussac, 0.511 g ethanol /
     g glucose), CO2 release (0.489 g CO2 / g glucose), and the
     mass-loss prediction (mostly CO2) that a kitchen scale can verify
     against an open vessel run.

Run: uv run mass_balance_ferment.py
"""
from __future__ import annotations
from dataclasses import dataclass


# Stoichiometric constants (mass basis)
YIELD_ETHANOL_FROM_GLUCOSE = 0.511   # g ethanol / g glucose
YIELD_CO2_FROM_GLUCOSE = 0.489       # g CO2 / g glucose
M_LACTATE_FROM_GLUCOSE = 1.0         # g lactate / g glucose (homolactic)
M_CO2_HETEROLACTIC = 0.244           # g CO2 / g glucose (heterolactic, Leuconostoc)


@dataclass
class SauerkrautResult:
    salt_fraction_pct: float
    cabbage_water_g: float
    estimated_co2_g: float
    estimated_lactate_g: float


def sauerkraut_balance(cabbage_kg: float, salt_g: float,
                       water_fraction: float = 0.92,
                       sugar_fraction: float = 0.025) -> SauerkrautResult:
    cabbage_g = cabbage_kg * 1000.0
    salt_fraction = 100.0 * salt_g / (cabbage_g + salt_g)
    cabbage_water_g = water_fraction * cabbage_g
    sugar_g = sugar_fraction * cabbage_g
    # Mixed homolactic / heterolactic; assume ~80 percent goes
    # homolactic in mature kraut and 20 percent heterolactic.
    homo_g = 0.8 * sugar_g
    hetero_g = 0.2 * sugar_g
    lactate_g = homo_g * M_LACTATE_FROM_GLUCOSE + hetero_g * 0.5
    co2_g = hetero_g * M_CO2_HETEROLACTIC
    return SauerkrautResult(
        salt_fraction_pct=salt_fraction,
        cabbage_water_g=cabbage_water_g,
        estimated_co2_g=co2_g,
        estimated_lactate_g=lactate_g,
    )


@dataclass
class SugarYeastResult:
    initial_total_g: float
    theoretical_ethanol_g: float
    theoretical_co2_g: float
    expected_mass_loss_g: float


def sugar_yeast_balance(sugar_g: float, water_g: float,
                        extent_of_reaction: float = 0.9) -> SugarYeastResult:
    sugar_reacted_g = sugar_g * extent_of_reaction
    ethanol_g = sugar_reacted_g * YIELD_ETHANOL_FROM_GLUCOSE
    co2_g = sugar_reacted_g * YIELD_CO2_FROM_GLUCOSE
    return SugarYeastResult(
        initial_total_g=sugar_g + water_g,
        theoretical_ethanol_g=ethanol_g,
        theoretical_co2_g=co2_g,
        expected_mass_loss_g=co2_g,
    )


def main() -> None:
    print("--- Sauerkraut mass balance (1.5 kg cabbage, 30 g salt) ---")
    r = sauerkraut_balance(cabbage_kg=1.5, salt_g=30.0)
    print(f"  Salt mass fraction: {r.salt_fraction_pct:.2f} percent")
    print(f"  Cabbage-bound water (released as brine): {r.cabbage_water_g:.0f} g")
    print(f"  Estimated lactate produced: {r.estimated_lactate_g:.1f} g")
    print(f"  Estimated CO2 released (mostly early heterolactic): {r.estimated_co2_g:.1f} g")
    print("  Target salt fraction window (Pediococcus / Leuconostoc): 1.8 - 2.5 percent")

    print("\n--- Sugar-yeast CO2 ferment (250 g sucrose, 1000 g water) ---")
    s = sugar_yeast_balance(sugar_g=250.0, water_g=1000.0,
                            extent_of_reaction=0.9)
    print(f"  Initial total mass: {s.initial_total_g:.0f} g")
    print(f"  Theoretical ethanol produced: {s.theoretical_ethanol_g:.0f} g")
    print(f"  Theoretical CO2 produced:    {s.theoretical_co2_g:.0f} g")
    print(f"  Expected mass loss (CO2 leaves through airlock): {s.expected_mass_loss_g:.0f} g")
    print("  Kitchen scale, daily mass log:")
    print("    integral of dm/dt is the CO2 release curve;")
    print("    rate of mass loss falls when sugar is consumed.")


if __name__ == "__main__":
    main()
