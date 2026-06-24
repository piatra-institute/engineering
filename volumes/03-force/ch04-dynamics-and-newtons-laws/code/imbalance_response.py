#!/usr/bin/env python3
"""Rotating-imbalance force and the transmissibility of a single-degree-of
-freedom passive isolator.

The rotating-imbalance force is F = m_r e omega^2 at rotation speed omega.
A passive isolator of natural frequency omega_n and damping ratio zeta
transmits a fraction T(r) of that force to the foundation, where r =
omega/omega_n is the frequency ratio:

    T(r) = sqrt( (1 + (2 zeta r)^2) / ((1 - r^2)^2 + (2 zeta r)^2) ).

Isolation (T < 1) requires r > sqrt(2); below that the isolator
amplifies. The script tabulates T across a speed sweep for the design
exercise (50 kg rotor, 50 g imbalance at 100 mm, 3000 rpm).
"""
from __future__ import annotations

import math

M_ROTOR = 50.0        # kg
M_IMB = 0.050         # kg of residual imbalance mass
R_IMB = 0.100         # m, its radius
RPM = 3000.0


def omega_from_rpm(rpm):
    return rpm * 2.0 * math.pi / 60.0


def imbalance_force(omega):
    return M_IMB * R_IMB * omega**2


def transmissibility(r, zeta):
    num = 1.0 + (2.0 * zeta * r) ** 2
    den = (1.0 - r**2) ** 2 + (2.0 * zeta * r) ** 2
    return math.sqrt(num / den)


if __name__ == "__main__":
    omega = omega_from_rpm(RPM)
    f0 = imbalance_force(omega)
    print(f"rotation speed   = {omega:.1f} rad/s ({RPM:.0f} rpm)")
    print(f"imbalance force  = {f0:.1f} N (unisolated, into bearings)")

    # Pick isolator natural frequency at 1/4 of the rotation speed (r = 4).
    omega_n = omega / 4.0
    zeta = 0.05
    r = omega / omega_n
    T = transmissibility(r, zeta)
    print(f"isolator f_n     = {omega_n / (2*math.pi):.1f} Hz, r = {r:.1f}")
    print(f"transmissibility = {T:.3f}  ->  transmitted force {f0 * T:.1f} N")
