"""Shear and bending-moment diagrams for a simply supported beam.

Builds V(x) and M(x) for a span L carrying any combination of point
loads and uniform line loads, by integrating the load downward from
the support reactions: dV/dx = -w, dM/dx = V. Reactions come from
global equilibrium. The script writes a sampled diagram to CSV so the
chapter figures and the worked examples can be checked against the
closed-form peaks.

Run:
    python shear_moment.py
"""

from __future__ import annotations

import numpy as np


def reactions(L, point_loads, udl):
    """Return (R_A, R_B) for a simple beam.

    point_loads: list of (a, P) with a the distance from the left
    support and P the downward magnitude (N).
    udl: uniform line load w0 (N/m) over the whole span.
    """
    total = udl * L + sum(P for _, P in point_loads)
    # moment about A: R_B * L = sum(P*a) + w0*L*(L/2)
    moment_A = sum(P * a for a, P in point_loads) + udl * L * (L / 2)
    R_B = moment_A / L
    R_A = total - R_B
    return R_A, R_B


def shear_moment(L, point_loads, udl, n=401):
    x = np.linspace(0.0, L, n)
    R_A, _ = reactions(L, point_loads, udl)
    V = np.full_like(x, R_A)
    V -= udl * x
    for a, P in point_loads:
        V -= np.where(x >= a, P, 0.0)
    # M(x) = integral of V from 0; trapezoidal cumulative
    M = np.concatenate([[0.0], np.cumsum((V[1:] + V[:-1]) / 2 * np.diff(x))])
    return x, V, M


def main():
    L = 8.0          # m
    w0 = 5.0e3       # N/m uniform load
    P = 20.0e3       # N central point load
    x, V, M = shear_moment(L, point_loads=[(L / 2, P)], udl=w0)

    print(f"span L = {L} m, w0 = {w0/1e3} kN/m, central P = {P/1e3} kN")
    print(f"max |V| = {np.max(np.abs(V))/1e3:.2f} kN")
    print(f"max  M  = {np.max(M)/1e3:.2f} kN.m at x = {x[np.argmax(M)]:.2f} m")

    # closed-form check for the two parts, superposed
    M_udl = w0 * L**2 / 8
    M_point = P * L / 4
    print(f"closed-form midspan M = {(M_udl + M_point)/1e3:.2f} kN.m")

    np.savetxt(
        "../data/shear_moment_profile.csv",
        np.column_stack([x, V / 1e3, M / 1e3]),
        delimiter=",",
        header="x_m,shear_kN,moment_kNm",
        comments="",
        fmt="%.4f",
    )


if __name__ == "__main__":
    main()
