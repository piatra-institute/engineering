"""Forced- and free-convection correlations for the working geometries.

Implements the Nusselt-number correlations of section 5.3 and converts them to
a convection coefficient h = Nu k / L. Covers flow over a flat plate (laminar
and turbulent), fully developed pipe flow (Dittus-Boelter), and free convection
from a vertical plate and a horizontal cylinder (Churchill-Chu).

SI units throughout. Fluid properties are passed in explicitly so the same
functions serve air, water, or any other fluid.
"""

from __future__ import annotations

import math


def reynolds(rho, u, length, mu):
    return rho * u * length / mu


def prandtl(cp, mu, k):
    return cp * mu / k


def plate_laminar_nu(re_l, pr):
    """Average Nusselt number, laminar flow over an isothermal flat plate."""
    return 0.664 * re_l ** 0.5 * pr ** (1.0 / 3.0)


def plate_turbulent_nu(re_x, pr):
    """Local Nusselt number, turbulent flow over a flat plate."""
    return 0.0296 * re_x ** 0.8 * pr ** (1.0 / 3.0)


def dittus_boelter_nu(re_d, pr, heating=True):
    """Fully developed turbulent pipe flow (Dittus-Boelter)."""
    n = 0.4 if heating else 0.3
    return 0.023 * re_d ** 0.8 * pr ** n


def rayleigh(g, beta, dt, length, nu, alpha):
    return g * beta * dt * length ** 3 / (nu * alpha)


def vertical_plate_free_nu(ra_l, pr):
    """Churchill-Chu correlation for a vertical isothermal plate."""
    num = 0.387 * ra_l ** (1.0 / 6.0)
    den = (1.0 + (0.492 / pr) ** (9.0 / 16.0)) ** (8.0 / 27.0)
    return (0.825 + num / den) ** 2


def horizontal_cylinder_free_nu(ra_d, pr):
    """Churchill-Chu correlation for a horizontal cylinder."""
    num = 0.387 * ra_d ** (1.0 / 6.0)
    den = (1.0 + (0.559 / pr) ** (9.0 / 16.0)) ** (8.0 / 27.0)
    return (0.6 + num / den) ** 2


def coefficient_from_nu(nu, k, length):
    """Convert a Nusselt number to a convection coefficient h = Nu k / L."""
    return nu * k / length


if __name__ == "__main__":
    # Air at about 300 K (illustrative properties).
    air = dict(rho=1.16, mu=1.85e-5, k=0.026, cp=1007.0, nu=1.59e-5,
               alpha=2.25e-5, beta=1.0 / 300.0)
    pr_air = prandtl(air["cp"], air["mu"], air["k"])
    print(f"Pr(air) = {pr_air:.3f}")

    # Forced flow over a 0.5 m plate at 5 m/s.
    re = reynolds(air["rho"], 5.0, 0.5, air["mu"])
    nu = plate_laminar_nu(re, pr_air)
    h = coefficient_from_nu(nu, air["k"], 0.5)
    print(f"flat plate, 5 m/s: Re={re:.2e}, Nu={nu:.1f}, h={h:.1f} W/(m^2.K)")

    # Free convection from a horizontal cylinder, 50 mm dia, 130 K excess.
    ra = rayleigh(9.81, air["beta"], 130.0, 0.05, air["nu"], air["alpha"])
    nu_c = horizontal_cylinder_free_nu(ra, pr_air)
    h_c = coefficient_from_nu(nu_c, air["k"], 0.05)
    print(f"hot cylinder: Ra={ra:.2e}, Nu={nu_c:.1f}, h={h_c:.1f} W/(m^2.K)")
