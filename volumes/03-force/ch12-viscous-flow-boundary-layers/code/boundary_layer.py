"""Flat-plate boundary-layer quantities: laminar (Blasius) and turbulent
(one-seventh-power / empirical) thickness, skin-friction coefficient, and
drag, with the transition-aware combined estimate.

Run:
    python boundary_layer.py
to reproduce the flat-plate and fuselage estimates in the chapter.
"""

from __future__ import annotations

import math


def re_x(U, x, nu):
    """Local Reynolds number based on streamwise distance."""
    return U * x / nu


def delta_laminar(x, Re_x):
    """Laminar boundary-layer (99 percent) thickness, Blasius."""
    return 5.0 * x / math.sqrt(Re_x)


def cf_laminar_local(Re_x):
    """Local laminar skin-friction coefficient, Blasius."""
    return 0.664 / math.sqrt(Re_x)


def cf_laminar_avg(Re_L):
    """Average laminar skin-friction coefficient over a plate of length L."""
    return 1.328 / math.sqrt(Re_L)


def delta_turbulent(x, Re_x):
    """Turbulent boundary-layer thickness, one-seventh-power correlation."""
    return 0.37 * x / Re_x**0.2


def cf_turbulent_local(Re_x):
    """Local turbulent skin-friction coefficient."""
    return 0.0592 / Re_x**0.2


def cf_turbulent_avg(Re_L):
    """Average turbulent skin-friction coefficient over a plate."""
    return 0.074 / Re_L**0.2


def drag_force(rho, U, area, cf_avg):
    """Skin-friction drag from the average skin-friction coefficient."""
    return 0.5 * rho * U**2 * area * cf_avg


if __name__ == "__main__":
    # Flat plate, 1 m, air at 20 m/s.
    U, L, nu, rho = 20.0, 1.0, 1.5e-5, 1.225
    ReL = re_x(U, L, nu)
    print("Flat plate, 1 m, air at 20 m/s:")
    print(f"  Re_L = {ReL:.3g}")
    print(f"  delta (laminar)   = {delta_laminar(L, ReL) * 1e3:.3f} mm")
    print(f"  Cf_bar (laminar)  = {cf_laminar_avg(ReL):.5f}")

    # Aircraft fuselage estimate.
    U, L, nu, rho = 230.0, 38.0, 4e-5, 0.38
    ReL = re_x(U, L, nu)
    S_w = 900.0
    cf = cf_turbulent_avg(ReL)
    print("\nAircraft fuselage (turbulent):")
    print(f"  Re_L = {ReL:.3g}, Cf_bar = {cf:.5f}")
    print(f"  skin-friction drag = {drag_force(rho, U, S_w, cf):.0f} N")
