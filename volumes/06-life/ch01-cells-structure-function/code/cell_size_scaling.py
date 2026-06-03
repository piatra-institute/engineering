"""
Cell-size scaling: surface-to-volume ratio and diffusion-limited radius.

Reports the canonical surface-to-volume ratios for representative cell
sizes, and computes the radius at which diffusion-limited oxygen flux
becomes insufficient at typical metabolic demand (the engineering
upper bound on cell radius without forced internal transport).

Supports:
  - Volume VI, Chapter 1, Calculation exercise on surface/volume.
  - Volume VI, Chapter 1, Estimation exercise on diffusion timescale.

Dependencies:
  numpy (only for arange).

Usage:
  python cell_size_scaling.py
"""

import numpy as np

# Constants.
D_O2_WATER = 2.0e-9  # m^2 / s, oxygen diffusion in water
C_O2_AIR_SATD = 0.21e-3  # mol / m^3 (very small near body T;
                          # used as scale)
METABOLIC_RATE_W_PER_M3 = 1.0e3  # rough mammalian-tissue metabolism


def sphere_sa_vol(r_um: float) -> tuple[float, float, float]:
    """Sphere surface area, volume, and SA/V ratio for radius r in um.
    Returns (SA in um^2, V in um^3, SA/V in 1/um).
    """
    sa = 4.0 * np.pi * r_um * r_um
    vol = (4.0 / 3.0) * np.pi * r_um ** 3
    return sa, vol, sa / vol


def biconcave_disc_sa_vol() -> tuple[float, float, float]:
    """Approximate biconcave disc (RBC) SA and V from canonical values.
    """
    sa = 140.0   # um^2 (canonical RBC SA)
    vol = 90.0   # um^3
    return sa, vol, sa / vol


def diffusion_limited_radius() -> float:
    """The radius at which a spherical cell with uniform O2 demand
    runs out of internal O2 at its centre, given diffusion from the
    surface.

    From steady-state diffusion with uniform consumption rate Q
    (mol m^-3 s^-1) and surface concentration C_s, the centre
    concentration falls to zero at r* = sqrt(6 D C_s / Q).
    """
    Q = 1.0e-3  # mol / (m^3 s); rough mammalian
    C_s = 1.0e-1  # mol / m^3; saturated O2 in plasma (rough scale)
    r_star_m = np.sqrt(6.0 * D_O2_WATER * C_s / Q)
    return r_star_m * 1.0e6  # convert to micrometres


def main() -> None:
    print("# Surface-to-volume ratio for spherical cells:")
    print(f"  {'Radius (um)':>12} {'SA (um^2)':>12} {'V (um^3)':>12} "
          f"{'SA/V (1/um)':>12}")
    for r in [0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]:
        sa, vol, sv = sphere_sa_vol(r)
        print(f"  {r:12.2f} {sa:12.2f} {vol:12.2f} {sv:12.4f}")

    sa, vol, sv = biconcave_disc_sa_vol()
    print()
    print(f"# Red blood cell (biconcave disc, canonical):")
    print(f"  SA = {sa:.1f} um^2, V = {vol:.1f} um^3, "
          f"SA/V = {sv:.4f} 1/um")
    # Compare to a sphere of same volume
    r_eq = (3.0 * vol / (4.0 * np.pi)) ** (1.0 / 3.0)
    sa_eq, _, sv_eq = sphere_sa_vol(r_eq)
    ratio = sv / sv_eq
    print(f"  Sphere of same volume: r = {r_eq:.2f} um, "
          f"SA/V = {sv_eq:.4f} 1/um")
    print(f"  RBC is {ratio:.2f}x the sphere's SA/V.")

    r_star = diffusion_limited_radius()
    print()
    print(f"# Diffusion-limited cell radius for O2: "
          f"r* ~ {r_star:.0f} um")
    print(f"  Cells much smaller than r* are not diffusion-limited;")
    print(f"  cells much larger than r* require forced internal "
          f"transport (cytoplasmic streaming, vascular delivery, or")
    print(f"  in vivo a circulatory system at the tissue level).")


if __name__ == "__main__":
    main()
