"""Terminal velocity of a sphere settling in a viscous fluid, across drag
regimes.

At low Reynolds number the Stokes law gives a closed-form terminal
velocity. Outside the Stokes regime the drag coefficient depends on Re
through the standard sphere-drag curve, so the balance of gravity, buoyancy,
and drag must be solved iteratively. This routine uses the Schiller=Naumann
correlation for C_D, which tracks the standard curve up to the drag crisis.

Run:
    python sphere_terminal_velocity.py
to reproduce the falling-sphere examples in the chapter.
"""

from __future__ import annotations

import math

G = 9.81


def cd_schiller_naumann(Re: float) -> float:
    """Sphere drag coefficient, valid to Re of order 1e5 (below the drag
    crisis). Reduces to 24/Re in the Stokes limit."""
    if Re < 1e-6:
        return 24.0 / 1e-6
    return (24.0 / Re) * (1.0 + 0.15 * Re**0.687)


def terminal_velocity(d, rho_s, rho_f, mu, tol=1e-9):
    """Terminal settling velocity of a sphere of diameter d and density
    rho_s in a fluid of density rho_f and viscosity mu. Iterates the force
    balance with the Schiller=Naumann drag law."""
    # Stokes starting guess: U = g d^2 (rho_s - rho_f) / (18 mu).
    U = G * d**2 * (rho_s - rho_f) / (18.0 * mu)
    weight_minus_buoy = (math.pi / 6.0) * d**3 * (rho_s - rho_f) * G
    area = math.pi * d**2 / 4.0
    for _ in range(200):
        Re = rho_f * U * d / mu
        cd = cd_schiller_naumann(Re)
        # Drag = 0.5 rho_f U^2 A C_D; set equal to weight minus buoyancy.
        U_new = math.sqrt(weight_minus_buoy / (0.5 * rho_f * area * cd))
        if abs(U_new - U) < tol:
            U = U_new
            break
        U = 0.5 * (U + U_new)
    Re = rho_f * U * d / mu
    return {"U_terminal": U, "Re": Re, "C_D": cd_schiller_naumann(Re)}


if __name__ == "__main__":
    print("5 mm steel-like sphere in glycerin (Stokes regime):")
    r = terminal_velocity(d=5e-3, rho_s=7800.0, rho_f=1260.0, mu=1.5)
    print(f"  U = {r['U_terminal']:.4g} m/s, Re = {r['Re']:.3g}")
    print("2 mm raindrop in air (beyond Stokes):")
    r = terminal_velocity(d=2e-3, rho_s=1000.0, rho_f=1.225, mu=1.8e-5)
    print(f"  U = {r['U_terminal']:.4g} m/s, Re = {r['Re']:.3g}")
