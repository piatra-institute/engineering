"""Potential flow around a circular cylinder, with optional bound circulation.

Stream function (polar, cylinder radius R, freestream U):

    psi = U r sin(theta) (1 - R^2/r^2) - (Gamma / 2 pi) ln(r/R)

Surface (r = R) tangential speed and pressure coefficient:

    u_theta = -2 U sin(theta) - Gamma / (2 pi R)
    Cp      = 1 - (u_theta / U)^2

This script tabulates Cp(theta) for Gamma = 0 (d'Alembert) and for a lifting
case, integrates the surface pressure to confirm zero drag and the
Kutta-Joukowski lift L' = rho U Gamma, and writes the surface distribution.

Run:  uv run cylinder_potential.py
"""

from __future__ import annotations

import csv
import math
from pathlib import Path


def surface(U: float, R: float, gamma: float, n: int = 360):
    """Return lists theta (rad), u_theta, Cp around the cylinder surface."""
    th, ut, cp = [], [], []
    for i in range(n):
        t = 2.0 * math.pi * i / n
        u = -2.0 * U * math.sin(t) - gamma / (2.0 * math.pi * R)
        th.append(t)
        ut.append(u)
        cp.append(1.0 - (u / U) ** 2)
    return th, ut, cp


def integrate_force(U: float, R: float, rho: float, gamma: float):
    """Integrate p = p_inf + 0.5 rho U^2 Cp around the surface.

    Returns (drag_per_length, lift_per_length). Pressure acts inward along the
    inward normal; force on cylinder = - integral p n dl with n outward.
    """
    th, _, cp = surface(U, R, gamma, n=2000)
    q = 0.5 * rho * U**2
    fx = fy = 0.0
    dl = 2.0 * math.pi * R / len(th)
    for t, c in zip(th, cp):
        p = q * c  # gauge pressure (relative to freestream)
        # outward normal (cos t, sin t); pressure pushes inward => force -p n dl
        fx += -p * math.cos(t) * dl
        fy += -p * math.sin(t) * dl
    return fx, fy


def main() -> None:
    U, R, rho = 10.0, 0.5, 1.225

    # Non-lifting case
    fx0, fy0 = integrate_force(U, R, rho, 0.0)
    print(f"Gamma = 0 : drag/len = {fx0:.3e} N/m, lift/len = {fy0:.3e} N/m")

    # Lifting case
    gamma = 8.0
    fx1, fy1 = integrate_force(U, R, rho, gamma)
    kj = rho * U * gamma
    print(f"Gamma = {gamma} : drag/len = {fx1:.3e} N/m, lift/len = {fy1:.3f} N/m")
    print(f"Kutta-Joukowski rho U Gamma = {kj:.3f} N/m")

    out = Path(__file__).resolve().parent.parent / "data" / "cylinder_cp.csv"
    th, ut, cp = surface(U, R, 0.0)
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["theta_deg", "u_theta_m_s", "Cp"])
        for t, u, c in zip(th, ut, cp):
            w.writerow([round(math.degrees(t), 1), round(u, 4), round(c, 4)])
    print(f"Wrote {out.name}")


if __name__ == "__main__":
    main()
