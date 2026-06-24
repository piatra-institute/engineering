#!/usr/bin/env python3
"""Vibration isolation: transmissibility design helper.

Given a machine mass, a disturbance frequency, and a target
transmissibility, this picks an isolator natural frequency and the
resulting spring stiffness, and reports the transmissibility curve.

Run:  python3 transmissibility.py
"""

import numpy as np


def transmissibility(r, zeta):
    """TR = |X_mass / X_base| for a base-excited SDOF mount."""
    num = 1.0 + (2.0 * zeta * r) ** 2
    den = (1.0 - r ** 2) ** 2 + (2.0 * zeta * r) ** 2
    return np.sqrt(num / den)


def isolator_design(mass, f_disturb, tr_target, zeta=0.05):
    """Return (f_n, k, achieved_TR) for a target transmissibility.

    Uses the lightly damped approximation TR ~ 1/(r^2 - 1) to seed the
    natural frequency, then evaluates the exact curve.
    """
    # solve 1/(r^2 - 1) = tr_target  ->  r^2 = 1 + 1/tr_target
    r2 = 1.0 + 1.0 / tr_target
    r = np.sqrt(r2)
    f_n = f_disturb / r
    omega_n = 2.0 * np.pi * f_n
    k = mass * omega_n ** 2
    achieved = transmissibility(r, zeta)
    return f_n, k, achieved


if __name__ == "__main__":
    mass = 100.0          # kg
    f_disturb = 50.0      # Hz
    tr_target = 0.05      # transmit at most 5 percent of base motion

    f_n, k, tr = isolator_design(mass, f_disturb, tr_target, zeta=0.05)
    print(f"isolator f_n = {f_n:.2f} Hz")
    print(f"required k    = {k/1e3:.1f} kN/m  (total of all mounts)")
    print(f"frequency ratio r = {f_disturb/f_n:.2f}")
    print(f"achieved TR  = {tr:.4f}  ({100*tr:.1f} percent transmitted)")

    print("\nTR over the operating band:")
    for f in (10, 20, 30, 40, 50, 60):
        r = f / f_n
        print(f"  {f:3d} Hz: r = {r:4.2f}  TR = {transmissibility(r, 0.05):.3f}")
