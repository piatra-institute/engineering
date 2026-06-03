"""
Diffusion timescale for small molecules across cell-scale distances.

For three-dimensional Fickian diffusion of a small molecule with
diffusion coefficient D, the mean-square displacement after time t is
<r^2> = 6 D t, so the characteristic time to diffuse a distance L is
tau ~ L^2 / (6 D).

This file tabulates tau across a range of L and D values relevant to
cell biology and compares the bacterial vs. animal-cell case.

Supports:
  - Volume VI, Chapter 1, Estimation exercise on diffusion time.
  - Volume VI, Chapter 1, Simulation exercises on chemotaxis adaptation.

Dependencies:
  numpy.

Usage:
  python diffusion_timescale.py
"""

import numpy as np


def diffusion_time(L_m: float, D_m2_s: float) -> float:
    """Characteristic time (s) to diffuse a distance L_m with
    diffusion coefficient D_m2_s in 3D (using <r^2> = 6 D t)."""
    return L_m * L_m / (6.0 * D_m2_s)


def main() -> None:
    # Reference diffusion coefficients in water at 25 C (m^2 / s).
    # Reduced by ~3-4x in cytoplasm due to molecular crowding
    # (Luby-Phelps 2000).
    D_values = {
        "small_molecule (glucose)": 7.0e-10,
        "small_molecule (water)": 2.3e-9,
        "small_protein (~30 kDa)": 1.0e-10,
        "GFP-tagged protein": 3.0e-11,
        "vesicle (~100 nm)": 2.0e-12,
    }

    # Reference lengthscales (m).
    L_values = {
        "bacterial radius (1 um)": 1.0e-6,
        "animal cell radius (10 um)": 1.0e-5,
        "neuronal axon (10 cm)": 1.0e-1,
        "neuronal axon (1 m)": 1.0,
    }

    print("# Diffusion time tau ~ L^2 / (6 D), in seconds")
    print(f"# Crowding-corrected: D_cyto ~ D_water / 3.5 for small "
          f"probes (Luby-Phelps 2000)")
    print()
    header = f"  {'Distance':<28} " + " ".join(
        [f"{name:>22}" for name in D_values])
    print(header)
    for L_name, L_m in L_values.items():
        row = f"  {L_name:<28} "
        for D_name, D in D_values.items():
            D_cyto = D / 3.5
            tau = diffusion_time(L_m, D_cyto)
            if tau < 60.0:
                row += f"{tau:18.4g} s   "
            elif tau < 3600.0:
                row += f"{tau / 60.0:18.4g} min "
            elif tau < 86400.0:
                row += f"{tau / 3600.0:18.4g} hr  "
            else:
                row += f"{tau / 86400.0:18.4g} dy  "
        print(row)

    print()
    print("# Reading: bacteria can rely on diffusion alone for "
          "intracellular transport.")
    print("#          Animal cells can rely on diffusion for small "
          "molecules but not for proteins; ")
    print("#          the cytoskeleton + motor proteins move proteins "
          "and vesicles on relevant timescales.")
    print("#          Long neurons cannot rely on diffusion at all; "
          "axonal transport is by motor protein on microtubule.")


if __name__ == "__main__":
    main()
