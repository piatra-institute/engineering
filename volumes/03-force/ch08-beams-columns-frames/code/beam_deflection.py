"""Finite-difference solver for the Euler-Bernoulli beam equation.

Solves EI y'''' (x) = w(x) on a simply supported span by a
second-order central difference on the fourth derivative, with the
simple-support conditions y = 0 and y'' = 0 at both ends. Verifies the
midspan deflection against the closed form 5 w0 L^4 / (384 EI) for a
uniform load.

Run:
    python beam_deflection.py
"""

from __future__ import annotations

import numpy as np


def solve_simply_supported(E, I, L, w0, n=201):
    """Return x and y(x) for a uniform load w0 (N/m), simple supports."""
    x = np.linspace(0.0, L, n)
    dx = x[1] - x[0]
    EI = E * I

    # interior unknowns are y[1..n-2]; y[0]=y[n-1]=0 (deflection)
    # y'' = 0 at the ends is imposed with a ghost-node reflection.
    N = n
    A = np.zeros((N, N))
    rhs = np.zeros(N)
    coeff = EI / dx**4

    for i in range(N):
        if i == 0 or i == N - 1:
            A[i, i] = 1.0          # y = 0 at supports
            rhs[i] = 0.0
            continue
        # rows adjacent to supports use the y''=0 (M=0) condition by
        # setting the ghost deflection equal to minus the interior node,
        # which is the standard simple-support stencil.
        if i == 1:
            A[i, i - 1] += coeff * (-4 + 1)   # ghost reflection
            A[i, i] += coeff * 6
            A[i, i + 1] += coeff * (-4)
            A[i, i + 2] += coeff * 1
        elif i == N - 2:
            A[i, i - 2] += coeff * 1
            A[i, i - 1] += coeff * (-4)
            A[i, i] += coeff * 6
            A[i, i + 1] += coeff * (-4 + 1)
        else:
            A[i, i - 2] += coeff * 1
            A[i, i - 1] += coeff * (-4)
            A[i, i] += coeff * 6
            A[i, i + 1] += coeff * (-4)
            A[i, i + 2] += coeff * 1
        rhs[i] = -w0   # downward load gives downward (negative) deflection

    y = np.linalg.solve(A, rhs)
    return x, y


def main():
    E = 200e9
    I = 100e-3 * (200e-3) ** 3 / 12   # 100 x 200 mm rectangle
    L = 5.0
    w0 = 5.0e3

    x, y = solve_simply_supported(E, I, L, w0)
    mid = np.min(y)
    closed = -5 * w0 * L**4 / (384 * E * I)
    print(f"finite-difference midspan deflection = {mid*1e3:.3f} mm")
    print(f"closed-form  5 w0 L^4 / 384 EI       = {closed*1e3:.3f} mm")
    print(f"relative error = {abs(mid-closed)/abs(closed)*100:.2f} %")

    np.savetxt(
        "../data/deflection_profile.csv",
        np.column_stack([x, y * 1e3]),
        delimiter=",",
        header="x_m,deflection_mm",
        comments="",
        fmt="%.5f",
    )


if __name__ == "__main__":
    main()
