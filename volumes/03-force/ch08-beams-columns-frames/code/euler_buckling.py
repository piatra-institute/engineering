"""Euler column buckling and the column strength curve.

Computes the critical load for the four classical end conditions and
sweeps the critical stress against the slenderness ratio, marking the
transition slenderness where Euler buckling meets material yielding.
Writes the strength curve to CSV.

Run:
    python euler_buckling.py
"""

from __future__ import annotations

import math

import numpy as np

K_FACTORS = {
    "pinned-pinned": 1.0,
    "fixed-fixed": 0.5,
    "fixed-free": 2.0,
    "fixed-pinned": 0.7,
}


def critical_load(E, I, L, K):
    """Euler critical load P_cr = pi^2 E I / (K L)^2."""
    return math.pi**2 * E * I / (K * L) ** 2


def transition_slenderness(E, sigma_y):
    """lambda_c = pi sqrt(E / sigma_y)."""
    return math.pi * math.sqrt(E / sigma_y)


def main():
    E = 200e9          # Pa
    sigma_y = 250e6    # Pa
    # a square solid bar 50 mm x 50 mm for the worked numbers
    b = h = 0.050
    A = b * h
    I = b * h**3 / 12
    r = math.sqrt(I / A)
    L = 3.0

    print(f"section r = {r*1e3:.2f} mm, A = {A*1e4:.2f} cm^2")
    for name, K in K_FACTORS.items():
        Pcr = critical_load(E, I, L, K)
        print(f"{name:>14s}: K={K}, P_cr = {Pcr/1e3:.1f} kN")

    lam_c = transition_slenderness(E, sigma_y)
    print(f"transition slenderness lambda_c = {lam_c:.1f}")

    lam = np.linspace(10, 200, 200)
    sigma_euler = math.pi**2 * E / lam**2          # Pa
    sigma_cr = np.minimum(sigma_euler, sigma_y)    # capped by yield
    np.savetxt(
        "../data/column_strength_curve.csv",
        np.column_stack([lam, sigma_euler / 1e6, sigma_cr / 1e6]),
        delimiter=",",
        header="slenderness,sigma_euler_MPa,sigma_capped_MPa",
        comments="",
        fmt="%.3f",
    )


if __name__ == "__main__":
    main()
