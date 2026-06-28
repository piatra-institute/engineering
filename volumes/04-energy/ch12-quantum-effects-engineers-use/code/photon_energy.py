#!/usr/bin/env python3
"""Photon energy, momentum, and frequency from wavelength, plus the working
1.24 eV-micrometre rule used at the bench.

Run:
    python3 code/photon_energy.py 405 633 850 1550
"""
import sys

H = 6.62607015e-34      # J s, exact in the 2019 SI
C = 2.99792458e8        # m/s, exact
E_CHARGE = 1.602176634e-19  # C, exact


def photon(lam_nm):
    lam = lam_nm * 1e-9
    nu = C / lam
    energy_j = H * nu
    energy_ev = energy_j / E_CHARGE
    momentum = H / lam
    return nu, energy_j, energy_ev, momentum


def main(args):
    wavelengths = [float(a) for a in args] or [405.0, 633.0, 850.0, 1550.0]
    print(f"{'lambda(nm)':>11} {'nu(THz)':>10} {'E(eV)':>8} "
          f"{'E(J)':>11} {'p(kg m/s)':>12} {'1.24/um':>8}")
    for lam_nm in wavelengths:
        nu, ej, ev, p = photon(lam_nm)
        rule = 1.24 / (lam_nm * 1e-3)   # 1.24 eV-micrometre working rule
        print(f"{lam_nm:11.1f} {nu/1e12:10.1f} {ev:8.3f} "
              f"{ej:11.3e} {p:12.3e} {rule:8.3f}")


if __name__ == "__main__":
    main(sys.argv[1:])
