"""
Energetic cost of Na+/K+ ATPase ion pumping in a typical mammalian cell.

The Na+/K+ ATPase exchanges 3 Na+ out for 2 K+ in per ATP hydrolysed
(Skou 1957). Steady-state ion leak through channels at the resting
potential sets the pumping rate required to maintain the gradient;
that pumping rate sets a metabolic cost that is the single largest ATP
sink in many resting cells.

Supports:
  - Volume VI, Chapter 1, Calculation exercise on ATP throughput.
  - Volume VI, Chapter 1, Calculation exercise on Na/K pump flux.

Dependencies:
  numpy.

Usage:
  python na_k_pump_atp_cost.py
"""

import numpy as np

# Constants.
N_A = 6.022e23
F = 96485.0  # C/mol


def pump_atp_per_action_potential(
    axon_radius_m: float, axon_length_m: float,
    v_change_v: float, c_m_F_per_m2: float = 9.0e-3,
    z: int = 1) -> float:
    """Approximate ATP cost of restoring the membrane after one action
    potential, summed over the axon's surface.

    The membrane carries capacitance C_m per unit area. A voltage
    change Delta V across area A involves charge Q = C_m * A * dV;
    restoring it pumps Q / (z*F) moles of cation across the membrane.
    With 3 Na+ pumped per ATP, ATP molecules required is
    N_ATP = Q * N_A / (3 * F).
    """
    A = 2.0 * np.pi * axon_radius_m * axon_length_m  # cylindrical
    Q = c_m_F_per_m2 * A * v_change_v
    n_ion = Q / F  # moles of monovalent ions
    n_atp = (n_ion / 3.0) * N_A  # 3 Na+ per ATP
    return n_atp


def main() -> None:
    # Typical mammalian unmyelinated axon: r = 0.5 um, L = 1 cm
    r = 0.5e-6
    L = 1.0e-2
    dv = 0.1  # 100 mV peak depolarisation
    atp = pump_atp_per_action_potential(r, L, dv)
    print(f"# Unmyelinated axon, r = {r * 1e6:.1f} um, L = {L * 1e3:.0f} mm:")
    print(f"  ATP per action potential: {atp:.2e}")
    print(f"  Canonical literature value: ~10^9 ATP per cm of axon "
          f"per AP (Attwell & Laughlin 2001)")

    # Larger axon
    r = 5.0e-6
    L = 1.0e-2
    atp = pump_atp_per_action_potential(r, L, dv)
    print(f"\n# Squid-giant-style axon, r = {r * 1e6:.1f} um, "
          f"L = {L * 1e3:.0f} mm:")
    print(f"  ATP per AP: {atp:.2e}")

    # Fraction of a cell's ATP budget at rest
    print("\n# Cell-level resting ATP budget:")
    cell_atp_pool = 1.0e10  # rough mammalian cell at rest
    pump_atp_per_s = 5.0e8  # rough resting Na/K pump rate per cell
    print(f"  Cell ATP pool (typical mammalian, instantaneous): "
          f"{cell_atp_pool:.2e}")
    print(f"  Na/K pump consumption: {pump_atp_per_s:.2e} ATP/s")
    print(f"  Fraction of total resting ATP turnover going to pumping: "
          f"~25--35% (Rolfe & Brown 1997)")

    # Cardiomyocyte mitochondrial budget
    print("\n# Cardiomyocyte mitochondrial accounting:")
    cell_vol_um3 = 20000.0
    mito_fraction = 0.35
    mito_per_cell = mito_fraction * cell_vol_um3 / 1.0
    print(f"  Volume = {cell_vol_um3:.0f} um^3, "
          f"mitochondria = {mito_fraction * 100:.0f}% by volume")
    print(f"  Number of mitochondria (V_mito ~ 1 um^3 each): "
          f"~{mito_per_cell:.0f}")


if __name__ == "__main__":
    main()
