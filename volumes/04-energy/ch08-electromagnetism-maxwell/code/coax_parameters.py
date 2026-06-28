"""Coaxial-cable per-length parameters and characteristic impedance.

Computes capacitance per metre C' = 2 pi eps / ln(b/a), inductance per
metre L' = (mu / 2 pi) ln(b/a), and characteristic impedance
Z0 = sqrt(L'/C') = (1/2pi) sqrt(mu/eps) ln(b/a). Used in Section 8.8 and
the calculation exercise. Reproduces the RG-58 50-ohm result for a
polyethylene dielectric.
"""

import numpy as np

EPS0 = 8.8541878128e-12
MU0 = 4.0e-7 * np.pi


def coax(a, b, eps_r=1.0, mu_r=1.0):
    eps = eps_r * EPS0
    mu = mu_r * MU0
    ratio = np.log(b / a)
    c_per_m = 2.0 * np.pi * eps / ratio
    l_per_m = mu / (2.0 * np.pi) * ratio
    z0 = np.sqrt(l_per_m / c_per_m)
    v_prop = 1.0 / np.sqrt(l_per_m * c_per_m)
    return c_per_m, l_per_m, z0, v_prop


if __name__ == "__main__":
    cases = [
        ("RG-58 (PE, b/a~3)", 0.45e-3, 1.47e-3, 2.25, 1.0),
        ("air line, b/a=3", 1.0e-3, 3.0e-3, 1.0, 1.0),
        ("exercise cable", 0.4e-3, 2.0e-3, 2.25, 1.0),
    ]
    for name, a, b, er, mr in cases:
        cpm, lpm, z0, vp = coax(a, b, er, mr)
        print(f"{name}:")
        print(f"  C' = {cpm*1e12:6.1f} pF/m, L' = {lpm*1e9:6.1f} nH/m, "
              f"Z0 = {z0:5.1f} ohm, v/c = {vp/2.998e8:.3f}")
