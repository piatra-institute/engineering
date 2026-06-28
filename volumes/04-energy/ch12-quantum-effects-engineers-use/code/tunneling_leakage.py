"""Gate-oxide tunnelling leakage versus oxide thickness.

Uses the WKB thick-barrier transmission factor exp(-2 d sqrt(2 m* phi)/hbar)
to show the exponential sensitivity of leakage to thickness that drove the
silicon industry from SiO2 to high-k dielectrics. The absolute prefactor is
not modelled; the table reports the transmission factor relative to a 2 nm
reference so the scaling is the point.

Run:
    python3 code/tunneling_leakage.py
"""
import math

HBAR = 1.054571817e-34      # J s
M_E = 9.1093837015e-31      # kg
E_CHARGE = 1.602176634e-19  # C

PHI_SIO2 = 3.1              # eV, electron barrier height for SiO2
M_STAR = 0.42 * M_E        # effective tunnelling mass in SiO2 (approx)


def kappa(phi_ev):
    """Decay constant inside the barrier (1/m)."""
    phi_j = phi_ev * E_CHARGE
    return math.sqrt(2.0 * M_STAR * phi_j) / HBAR


def transmission(d_nm, phi_ev=PHI_SIO2):
    d = d_nm * 1e-9
    return math.exp(-2.0 * kappa(phi_ev) * d)


def main():
    ref = transmission(2.0)
    print(f"{'d (nm)':>7} {'T(d)':>12} {'relative to 2 nm':>18}")
    for d in (1.0, 1.5, 2.0, 2.5, 3.0, 4.0):
        T = transmission(d)
        print(f"{d:7.1f} {T:12.3e} {T/ref:18.3e}")
    print("\nEach extra nanometre of oxide cuts the transmission by several")
    print("orders of magnitude. Holding the same gate capacitance while")
    print("adding physical thickness is exactly what a higher-k dielectric")
    print("buys, which is why HfO2 replaced SiO2 around the 45 nm node.")


if __name__ == "__main__":
    main()
