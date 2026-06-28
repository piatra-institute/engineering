"""Mass-transfer coefficients from standard Sherwood correlations.

Computes the Sherwood number, the mass-transfer coefficient k_c, and the
Schmidt number for three common geometries, then applies the
Chilton-Colburn analogy to convert a heat-transfer coefficient into a
mass-transfer coefficient.

Usage:
    python mass_transfer_coeff.py
"""

from __future__ import annotations


def schmidt(nu: float, D: float) -> float:
    return nu / D


def sh_flat_plate(Re: float, Sc: float) -> float:
    """Laminar average flat plate."""
    return 0.664 * Re ** 0.5 * Sc ** (1.0 / 3.0)


def sh_pipe(Re: float, Sc: float) -> float:
    """Turbulent fully developed pipe (analogue of Dittus-Boelter)."""
    return 0.023 * Re ** 0.83 * Sc ** (1.0 / 3.0)


def sh_sphere(Re: float, Sc: float) -> float:
    """Ranz-Marshall for a sphere, droplet, or particle."""
    return 2.0 + 0.6 * Re ** 0.5 * Sc ** (1.0 / 3.0)


def kc_from_sh(Sh: float, D: float, Lchar: float) -> float:
    return Sh * D / Lchar


def kc_from_h_chilton_colburn(h: float, rho: float, cp: float,
                              u: float, Pr: float, Sc: float) -> float:
    """Convert h to k_c via (h / rho cp u) Pr^2/3 = (k_c / u) Sc^2/3."""
    jH = (h / (rho * cp * u)) * Pr ** (2.0 / 3.0)
    return jH * u / Sc ** (2.0 / 3.0)


if __name__ == "__main__":
    nu = 1.5e-5         # air kinematic viscosity, m2/s
    D = 2.6e-5          # water vapour in air, m2/s
    Sc = schmidt(nu, D)
    Re = 5.0e4
    Sh = sh_flat_plate(Re, Sc)
    L = 1.0
    print(f"Sc                 : {Sc:.3f}")
    print(f"Sh (flat plate)    : {Sh:.1f}")
    print(f"k_c                : {kc_from_sh(Sh, D, L):.2e} m/s")
