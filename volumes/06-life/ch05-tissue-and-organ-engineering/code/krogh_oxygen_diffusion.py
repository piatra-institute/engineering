# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Oxygen diffusion through a metabolically active tissue slab.

Solves the steady-state oxygen-balance equation D d^2 C/dx^2 = q_dot
for a slab of thickness L supplied from one face at concentration C0
and consuming oxygen uniformly at rate q_dot. Reports the maximum
thickness L_max at which the far-face concentration just reaches zero.

This is the classical one-dimensional reduction of the Krogh cylinder
analysis. The cylindrical-symmetry version with capillary at the
centre and tissue cylinder of radius R_t produces a similar
quadratic profile in r; for a slab it is exact in closed form.

Working numbers (metabolically active tissue):
- D_O2 ~ 2.0e-9 m^2/s
- q_dot ~ 1.0e-3 mol/(m^3 s)
- C0 ~ 0.13 mM at arterial PO2 = 100 mmHg

Run: uv run krogh_oxygen_diffusion.py
"""
from __future__ import annotations
import math
import numpy as np


def slab_max_thickness(D: float, q_dot: float, C0: float) -> float:
    """Closed-form L_max for a slab with one-face supply.

    Steady-state: D d^2 C / dx^2 = q_dot, with C(0) = C0, C(L) = 0
    and dC/dx (L) = 0 simultaneously (the cell at the far face is
    just at the threshold of starvation).  Solving gives
    L_max = sqrt(2 D C0 / q_dot).
    """
    return math.sqrt(2.0 * D * C0 / q_dot)


def slab_profile(D: float, q_dot: float, C0: float, L: float, n: int = 201):
    """Numerical concentration profile through the slab.

    Uses a finite-difference solver on a uniform grid; returns
    (x_array, C_array) over [0, L].
    """
    dx = L / (n - 1)
    A = np.zeros((n, n))
    b = np.zeros(n)
    A[0, 0] = 1.0
    b[0] = C0
    A[-1, -1] = 1.0
    b[-1] = 0.0
    for i in range(1, n - 1):
        A[i, i - 1] = D / dx**2
        A[i, i] = -2.0 * D / dx**2
        A[i, i + 1] = D / dx**2
        b[i] = q_dot
    C = np.linalg.solve(A, b)
    x = np.linspace(0.0, L, n)
    return x, C


def sensitivity_sweep():
    """Report L_max under +/- a decade variations in D and q_dot."""
    C0 = 0.13e-3 * 1000.0  # 0.13 mM in mol/m^3 -> 0.13 mol/m^3
    print(f"baseline: D=2.0e-9 m^2/s, q_dot=1.0e-3 mol/(m^3 s), C0={C0:.3f} mol/m^3")
    print(f"  L_max = {1e6 * slab_max_thickness(2.0e-9, 1.0e-3, C0):.1f} um")
    print()
    print("sensitivity sweep:")
    print(f"{'D (m^2/s)':>12} {'q_dot (mol/m^3 s)':>20} {'L_max (um)':>14}")
    for D in [5.0e-10, 1.0e-9, 2.0e-9, 5.0e-9, 1.0e-8]:
        for q_dot in [1.0e-4, 5.0e-4, 1.0e-3, 5.0e-3, 1.0e-2]:
            L = 1e6 * slab_max_thickness(D, q_dot, C0)
            print(f"{D:12.2e} {q_dot:20.2e} {L:14.1f}")


def main():
    C0 = 0.13e-3 * 1000.0
    D = 2.0e-9
    q_dot = 1.0e-3
    L_max = slab_max_thickness(D, q_dot, C0)
    print(f"closed-form maximum supply thickness: {1e6 * L_max:.1f} um")
    # Numerical sanity: profile at L = L_max should reach zero at far face
    x, C = slab_profile(D, q_dot, C0, L_max)
    print(f"numerical: C(0) = {C[0]:.4f}, C(L_max) = {C[-1]:.4f} mol/m^3")
    print(f"numerical minimum: {C.min():.4f} mol/m^3 at x = {1e6 * x[np.argmin(C)]:.1f} um")
    print()
    sensitivity_sweep()


if __name__ == "__main__":
    main()
