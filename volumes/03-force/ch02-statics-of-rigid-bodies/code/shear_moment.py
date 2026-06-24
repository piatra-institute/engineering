"""Shear and bending-moment diagrams for a simply-supported planar beam
under point loads, uniform-over-an-interval distributed loads, and
applied couples.

The routine discretises the span, computes support reactions from
global equilibrium, then integrates the load to shear (dV/dx = -w) and
shear to moment (dM/dx = V) numerically, adding jumps at concentrated
loads and couples.

Verified in the chapter against the closed forms M_max = P L / 4
(central point load) and M_max = w0 L^2 / 8 (uniform load).

Sign convention: distributed and point loads positive downward;
reactions positive upward; sagging moment positive.
"""

from __future__ import annotations

import numpy as np


def solve_beam(L, point_loads=None, dist_loads=None, couples=None, n=2001):
    """Return x, V(x), M(x) for a simply-supported beam.

    Supports are assumed pinned at x = 0 and rollered at x = L.

    Parameters
    ----------
    L : float
        Span.
    point_loads : list[tuple[float, float]]
        (position, magnitude) with magnitude positive downward.
    dist_loads : list[tuple[float, float, float]]
        (x_start, x_end, intensity) uniform per unit length, positive
        downward.
    couples : list[tuple[float, float]]
        (position, moment) applied couple, positive counterclockwise.
    n : int
        Number of sample points.
    """
    point_loads = point_loads or []
    dist_loads = dist_loads or []
    couples = couples or []

    # --- reactions from global equilibrium ---
    total_down = sum(P for _, P in point_loads)
    total_down += sum(w * (b - a) for a, b, w in dist_loads)

    # Moment about left support (x = 0), CCW positive; downward load at x
    # gives clockwise (negative) moment -P*x. Right reaction R_B up at L
    # gives +R_B*L. Applied couple C adds +C.
    moment_about_A = 0.0
    for x, P in point_loads:
        moment_about_A += -P * x
    for a, b, w in dist_loads:
        xc = 0.5 * (a + b)
        moment_about_A += -w * (b - a) * xc
    for x, C in couples:
        moment_about_A += C
    R_B = -moment_about_A / L
    R_A = total_down - R_B

    x = np.linspace(0.0, L, n)
    dx = x[1] - x[0]

    # distributed load intensity sampled on the grid (downward positive)
    w_arr = np.zeros_like(x)
    for a, b, w in dist_loads:
        w_arr += w * ((x >= a) & (x <= b))

    # shear: start just right of A with +R_A, subtract integrated load,
    # subtract point loads as we pass them.
    V = np.zeros_like(x)
    V[0] = R_A
    for i in range(1, n):
        V[i] = V[i - 1] - w_arr[i] * dx
        for xp, P in point_loads:
            if x[i - 1] < xp <= x[i]:
                V[i] -= P
    # add right reaction is implicit; check closure
    V_end_residual = V[-1] + R_B  # should be ~0

    # moment: integrate shear; add couple jumps.
    M = np.zeros_like(x)
    for i in range(1, n):
        M[i] = M[i - 1] + 0.5 * (V[i - 1] + V[i]) * dx
        for xc, C in couples:
            if x[i - 1] < xc <= x[i]:
                M[i] -= C
    return x, V, M, dict(R_A=R_A, R_B=R_B, V_end_residual=V_end_residual)


if __name__ == "__main__":
    L = 6.0
    # central point load P = 10 kN
    x, V, M, info = solve_beam(L, point_loads=[(L / 2, 10.0)])
    print(f"central point load: M_max = {M.max():.4f}  (P L/4 = {10*L/4:.4f})")

    # uniform load w0 = 5 kN/m over full span
    x, V, M, info = solve_beam(L, dist_loads=[(0.0, L, 5.0)])
    print(f"uniform load:       M_max = {M.max():.4f}  "
          f"(w0 L^2/8 = {5*L**2/8:.4f})")
    print(f"reactions: R_A = {info['R_A']:.3f}, R_B = {info['R_B']:.3f}")
