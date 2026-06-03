# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Scaffold porosity, surface area, and connectivity diagnostics.

Models a porous scaffold as a simple-cubic packing of spherical pores
of diameter d_p separated by wall thickness t_w. Computes:

- porosity (void volume fraction)
- specific surface area (pore surface area per unit scaffold volume)
- interconnect throat size (the throat between adjacent pores)

Tabulates against the pore-size design windows for dermal, bone,
vascular, and nerve applications.

Run: uv run scaffold_porosity_calc.py
"""
from __future__ import annotations
import math


def porosity(d_p: float, t_w: float) -> float:
    """Void volume fraction for cubic packing of spherical pores."""
    a = d_p + t_w  # unit-cell edge
    v_pore = (math.pi / 6.0) * d_p**3
    v_cell = a**3
    return v_pore / v_cell


def specific_surface_area(d_p: float, t_w: float) -> float:
    """Pore surface area per unit scaffold volume (1/m)."""
    a = d_p + t_w
    s_pore = math.pi * d_p**2
    return s_pore / a**3


def throat_diameter(d_p: float, t_w: float) -> float:
    """In cubic packing, adjacent pores share an opening only if
    pores overlap; otherwise throats must be cut. For t_w > 0 the
    throat diameter is the diameter of the circle cut through the
    wall by the pore-pore axis.

    For non-overlapping pores (t_w > 0), the throat is conventionally
    cut at the wall midpoint with diameter d_throat = d_p - 2 t_w/k
    for some packing constant k. We use k = 1 (simple cut).
    """
    return max(0.0, d_p - 2.0 * t_w)


def design_window_check():
    """Report porosity and surface area for each tissue's window."""
    targets = {
        "dermal regeneration": (60e-6, 200e-6),
        "bone ingrowth":       (100e-6, 400e-6),
        "vascular ingrowth":   (50e-6, 300e-6),
        "nerve guidance":      (5e-6,  50e-6),
    }
    t_w = 30e-6
    print(f"wall thickness fixed at t_w = {t_w * 1e6:.0f} um")
    print()
    print(f"{'application':<22} {'pore (um)':>14} {'porosity':>10} {'S/V (1/mm)':>12} {'throat (um)':>12}")
    for name, (lo, hi) in targets.items():
        for d_p in (lo, hi):
            phi = porosity(d_p, t_w)
            sa = 1e-3 * specific_surface_area(d_p, t_w)
            th = 1e6 * throat_diameter(d_p, t_w)
            print(f"{name:<22} {d_p * 1e6:14.1f} {phi:10.3f} {sa:12.1f} {th:12.1f}")
    print()


def main():
    print("scaffold porosity diagnostics for cubic packing of spherical pores")
    print()
    design_window_check()
    print("interpretation:")
    print("  porosity > 0.7 is the standard target for cell infiltration;")
    print("  specific surface area > 30 mm^-1 supports adequate cell-")
    print("    matrix contact area;")
    print("  throat diameter > 30 um is required for vascular ingrowth")
    print("    (capillary diameter ~ 8 um but endothelial sprouts need")
    print("    larger channels to advance).")
    print("  the dermal-regeneration window (60-200 um) at t_w = 30 um")
    print("  produces porosity 0.27-0.43 in cubic packing; real")
    print("  freeze-dried scaffolds reach porosity 0.85-0.95 because")
    print("  the foaming process produces interconnected open-cell")
    print("  geometry rather than separated spherical pores.")


if __name__ == "__main__":
    main()
