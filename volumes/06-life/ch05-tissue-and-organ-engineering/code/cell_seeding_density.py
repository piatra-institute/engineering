# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Cell-count, seeding-density, and scale-up calculations.

For an engineered construct of given volume and target tissue,
compute:

- total cell count required at native tissue density
- starting-cell number from a punch biopsy or blood draw
- scale-up factor (target / starting)
- number of doublings required and time at typical expansion rate
- bioreactor working-volume requirement at terminal seeding density

Run: uv run cell_seeding_density.py
"""
from __future__ import annotations
import math


TISSUE_DENSITY = {
    "liver":             1.0e8,   # hepatocytes per cm^3
    "heart":             1.0e8,
    "kidney":            5.0e7,
    "skin (dermis)":     1.0e7,
    "cartilage":         1.0e7,
    "bone":              5.0e6,   # osteocytes per cm^3
    "brain (cortex)":    1.0e8,
}


def cells_required(volume_cm3: float, tissue: str) -> float:
    return volume_cm3 * TISSUE_DENSITY[tissue]


def doublings_required(starting: float, target: float) -> float:
    if target <= starting:
        return 0.0
    return math.log2(target / starting)


def expansion_time_days(doublings: float, doubling_hours: float) -> float:
    return doublings * doubling_hours / 24.0


def working_volume_litres(cells: float, terminal_density_per_ml: float) -> float:
    return cells / (terminal_density_per_ml * 1000.0)


def scenario(name, volume_cm3, tissue, starting_cells, doubling_hours,
             terminal_density_per_ml):
    target = cells_required(volume_cm3, tissue)
    doubl = doublings_required(starting_cells, target)
    days = expansion_time_days(doubl, doubling_hours)
    vol_L = working_volume_litres(target, terminal_density_per_ml)
    print(f"--- {name} ---")
    print(f"  construct volume: {volume_cm3} cm^3 ({tissue})")
    print(f"  target cell count: {target:.2e}")
    print(f"  starting cells:    {starting_cells:.2e}")
    print(f"  doublings needed:  {doubl:.1f}")
    print(f"  expansion time:    {days:.1f} days at {doubling_hours} h/doubling")
    print(f"  bioreactor working volume at {terminal_density_per_ml:.0e}/mL: {vol_L:.2f} L")
    print()


def main():
    print("cell-seeding and scale-up calculations")
    print()
    # Scenario A: 5 cm^3 liver patch from a 1 cm^2 skin punch biopsy
    # (iPSC-derived hepatocytes; ~ 5e5 starting fibroblasts; long expansion)
    scenario(
        "Liver patch (5 cm^3, iPSC-derived)",
        volume_cm3=5.0,
        tissue="liver",
        starting_cells=5e5,        # skin punch biopsy
        doubling_hours=24.0,       # iPSC doubling
        terminal_density_per_ml=1e7,
    )
    # Scenario B: 1 cm^3 cartilage from a 100 mg articular biopsy
    scenario(
        "Cartilage implant (1 cm^3, autologous chondrocytes)",
        volume_cm3=1.0,
        tissue="cartilage",
        starting_cells=2e6,        # chondrocytes from 100 mg biopsy
        doubling_hours=48.0,       # chondrocyte doubling
        terminal_density_per_ml=5e6,
    )
    # Scenario C: 50 cm^2 x 0.05 cm skin substitute
    scenario(
        "Skin substitute (50 cm^2 x 0.05 cm)",
        volume_cm3=2.5,
        tissue="skin (dermis)",
        starting_cells=1e6,        # keratinocyte / fibroblast biopsy
        doubling_hours=24.0,
        terminal_density_per_ml=5e6,
    )
    # Scenario D: 200 cm^3 liver lobe substitute (clinically relevant
    # for partial hepatic regeneration). This is the conjectural end.
    scenario(
        "Liver lobe substitute (200 cm^3, clinical scale, conjectural)",
        volume_cm3=200.0,
        tissue="liver",
        starting_cells=5e5,
        doubling_hours=24.0,
        terminal_density_per_ml=1e7,
    )
    print("interpretation:")
    print("  scenarios A-C are within the reach of existing cell-")
    print("  expansion infrastructure (autologous chondrocytes are an")
    print("  FDA-approved product; iPSC-derived cardiomyocyte patches")
    print("  have completed early-phase trials). Scenario D requires")
    print("  3-4 weeks of bioreactor expansion and >200 L of medium")
    print("  exchange, and remains conjectural at clinical scale.")


if __name__ == "__main__":
    main()
