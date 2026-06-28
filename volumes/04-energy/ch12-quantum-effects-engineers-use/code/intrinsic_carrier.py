#!/usr/bin/env python3
"""Intrinsic carrier concentration of a semiconductor versus temperature, and
the temperature at which it equals a given doping density.

n_i(T) = sqrt(N_c N_v) * exp(-E_g / (2 k_B T)), with the effective density of
states scaling as T^(3/2). Uses silicon parameters by default.

Run:
    python3 code/intrinsic_carrier.py
"""
import math

K_B = 1.380649e-23          # J/K, exact in the 2019 SI
E_CHARGE = 1.602176634e-19  # C
E_G_SI = 1.12               # eV, silicon band gap near 300 K

# effective density of states at 300 K (per cm^3), silicon
NC_300 = 2.8e19
NV_300 = 1.04e19


def n_i(T, eg_ev=E_G_SI):
    """Intrinsic carrier concentration (per cm^3) at temperature T (K)."""
    nc = NC_300 * (T / 300.0) ** 1.5
    nv = NV_300 * (T / 300.0) ** 1.5
    eg_j = eg_ev * E_CHARGE
    return math.sqrt(nc * nv) * math.exp(-eg_j / (2.0 * K_B * T))


def temperature_for_density(target, eg_ev=E_G_SI):
    """Bisect for the T where n_i(T) == target (per cm^3)."""
    lo, hi = 200.0, 1500.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if n_i(mid, eg_ev) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    print("Silicon intrinsic carrier concentration:")
    for T in (300, 400, 500, 600):
        print(f"  T = {T} K : n_i = {n_i(T):.3e} /cm^3")
    target = 1e15
    T_cross = temperature_for_density(target)
    print(f"\nn_i reaches {target:.0e} /cm^3 (moderate doping) at "
          f"T = {T_cross:.0f} K ({T_cross-273:.0f} C).")
    print("Above this temperature intrinsic carriers swamp the dopants and")
    print("the device loses its designed behaviour, the reason silicon power")
    print("electronics is rated for junction temperatures well below it.")


if __name__ == "__main__":
    main()
