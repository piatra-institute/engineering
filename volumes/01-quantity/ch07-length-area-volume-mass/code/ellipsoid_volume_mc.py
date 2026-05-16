# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Monte Carlo distribution of a triaxial ellipsoid's volume.

V = (4/3) pi a b c, with semi-axes a, b, c each drawn Gaussian with
specified mean and standard deviation. Compares the empirical
standard deviation of V to the product-of-powers linear estimate.

Used by Simulation exercise 1 in the chapter on length, area,
volume, mass.
"""

from __future__ import annotations

import math

import numpy as np

RNG = np.random.default_rng(401)
N_SAMPLES = 100_000

A_NOM, A_SD = 2.6, 0.1
B_NOM, B_SD = 2.0, 0.1
C_NOM, C_SD = 1.8, 0.1
# All in centimetres.


def main() -> None:
    a = RNG.normal(A_NOM, A_SD, size=N_SAMPLES)
    b = RNG.normal(B_NOM, B_SD, size=N_SAMPLES)
    c = RNG.normal(C_NOM, C_SD, size=N_SAMPLES)
    V = (4.0 / 3.0) * math.pi * a * b * c  # cm^3

    V_nom = (4.0 / 3.0) * math.pi * A_NOM * B_NOM * C_NOM
    rel_a = A_SD / A_NOM
    rel_b = B_SD / B_NOM
    rel_c = C_SD / C_NOM
    rel_V_lin = math.sqrt(rel_a**2 + rel_b**2 + rel_c**2)
    sd_V_lin = V_nom * rel_V_lin

    print(f"nominal V                : {V_nom:.3f}  cm^3")
    print(f"Monte Carlo mean V       : {V.mean():.3f}  cm^3")
    print(f"Monte Carlo sd V         : {V.std(ddof=1):.3f}  cm^3")
    print(f"linear-propagation sd V  : {sd_V_lin:.3f}  cm^3")
    print(f"ratio (MC / linear)      : {V.std(ddof=1) / sd_V_lin:.4f}")
    print()
    print("Distribution quantiles of V (cm^3):")
    for q in [0.025, 0.16, 0.5, 0.84, 0.975]:
        print(f"  q = {q:.3f} : {np.quantile(V, q):.3f}")


if __name__ == "__main__":
    main()
