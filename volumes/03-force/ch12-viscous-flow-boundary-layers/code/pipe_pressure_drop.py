"""Pressure drop across a pipe by the Darcy=Weisbach equation, with the
regime-aware friction factor from moody.py.

Given the geometry, fluid properties, and flow rate, the routine returns
the Reynolds number, the friction factor, the flow regime, and the
pressure drop. This is the core calculation behind the chapter's pipe
project.

Run:
    python pipe_pressure_drop.py
to reproduce the worked household-pipe example.
"""

from __future__ import annotations

import math

from moody import friction_factor


def pressure_drop(Q, D, L, rho, mu, eps=0.0):
    """Pressure drop (Pa) for volume flow Q (m^3/s) through a pipe of
    diameter D (m), length L (m), with fluid density rho and dynamic
    viscosity mu, and absolute roughness eps (m). Returns a dict."""
    area = math.pi * D**2 / 4.0
    u_bar = Q / area
    Re = rho * u_bar * D / mu
    rel_rough = eps / D
    f = friction_factor(Re, rel_rough)
    dp = f * (L / D) * 0.5 * rho * u_bar**2
    if Re < 2300.0:
        regime = "laminar"
    elif Re < 4000.0:
        regime = "transitional"
    else:
        regime = "turbulent"
    return {
        "u_bar": u_bar,
        "Re": Re,
        "friction_factor": f,
        "regime": regime,
        "delta_p_Pa": dp,
    }


if __name__ == "__main__":
    # Household supply pipe: 20 mm copper, 50 m, 0.2 L/s of water at 20 C.
    result = pressure_drop(
        Q=0.2e-3, D=0.020, L=50.0, rho=998.0, mu=1.0e-3, eps=1.5e-6
    )
    for key, value in result.items():
        if isinstance(value, float):
            print(f"{key:>16}: {value:.4g}")
        else:
            print(f"{key:>16}: {value}")
