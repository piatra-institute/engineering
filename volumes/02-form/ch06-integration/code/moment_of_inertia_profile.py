# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""
Moment of inertia of an elongated household object computed by
numerical integration on a measured cross-section profile.

For a body of axial length L with cross-section area A(x) and uniform
mass density rho, the moment of inertia about the perpendicular axis
through one end is

    I_end = rho * int_0^L A(x) * x^2 dx,

and the total mass is m = rho * int_0^L A(x) dx, so density cancels
when both are integrated from the same profile:

    I_end = m * (int_0^L A(x) x^2 dx) / (int_0^L A(x) dx).

This script reads a measured profile from data/hammer_profile.csv
(columns: x_mm, area_mm2), computes I_end using the trapezoidal
rule, halves the sampling interval by linear interpolation to check
convergence, and reports the result with an estimate of its
discretisation error.

Supports Volume II, Chapter 6:
  - Project (household moment of inertia, method ii).
  - Diagnosis exercise on hammer-decomposition discrepancy.

Run directly with uv:
    uv run moment_of_inertia_profile.py
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np


def load_profile(csv_path: Path) -> tuple[np.ndarray, np.ndarray]:
    xs: list[float] = []
    areas: list[float] = []
    with csv_path.open() as f:
        reader = csv.reader(f)
        next(reader)  # header
        for row in reader:
            xs.append(float(row[0]))
            areas.append(float(row[1]))
    return np.array(xs), np.array(areas)


def trapezoid(y: np.ndarray, x: np.ndarray) -> float:
    return float(np.trapz(y, x))


def halve_interval(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray,
                                                          np.ndarray]:
    """Insert linearly interpolated midpoints between successive samples."""
    x_new = np.empty(2 * x.size - 1)
    x_new[0::2] = x
    x_new[1::2] = 0.5 * (x[:-1] + x[1:])
    y_new = np.interp(x_new, x, y)
    return x_new, y_new


def moment_of_inertia(x_mm: np.ndarray, area_mm2: np.ndarray,
                      total_mass_kg: float) -> float:
    """I_end about the perpendicular axis through x = 0, in kg m^2."""
    x_m = x_mm * 1e-3
    area_m2 = area_mm2 * 1e-6
    numerator = trapezoid(area_m2 * x_m * x_m, x_m)
    denominator = trapezoid(area_m2, x_m)
    return total_mass_kg * numerator / denominator


def main() -> None:
    here = Path(__file__).parent.parent / "data"
    x_mm, area_mm2 = load_profile(here / "hammer_profile.csv")

    # Documented properties of the (hypothetical) hammer.
    mass_kg = 0.680  # 680 g claw hammer

    # Compute on the original grid and on a once-halved grid.
    I_h = moment_of_inertia(x_mm, area_mm2, mass_kg)

    x2, a2 = halve_interval(x_mm, area_mm2)
    I_h2 = moment_of_inertia(x2, a2, mass_kg)

    delta = abs(I_h2 - I_h)
    print(f"Profile samples:           {x_mm.size}")
    print(f"I (original spacing):      {I_h:.6e} kg m^2")
    print(f"I (halved spacing):        {I_h2:.6e} kg m^2")
    print(f"Convergence-by-halving:    {delta:.3e} kg m^2 "
          f"({100 * delta / I_h2:.3f} %)")


if __name__ == "__main__":
    main()
