"""
voltage_gradient_1d.py

One-dimensional reaction-diffusion model of a tissue voltage gradient.

State variable: membrane potential V(x, t) on [0, L].
Equation: dV/dt = D * d^2 V / dx^2 - k (V - V_rest)
Boundary conditions: V(0, t) = V_drive (Dirichlet), V(L, t) free (Neumann).

Used by Vol VI Ch 13 Exercise 13.6 (simulation) to illustrate that the
steady-state spread of a bioelectric perturbation is governed by the
length scale lambda = sqrt(D/k), not by the diffusion coefficient alone.

Reference: Levin 2014 (BioEssays); Pezzulo & Levin 2015 (J R Soc Interface).
"""

import numpy as np

def steady_state(D, k, V_rest, V_drive, L, N=200):
    """Compute steady-state V(x) via solving the linear system."""
    dx = L / (N - 1)
    x = np.linspace(0, L, N)
    # Build tridiagonal: D V'' - k (V - V_rest) = 0
    A = np.zeros((N, N))
    b = np.zeros(N)
    # Dirichlet at x=0
    A[0, 0] = 1.0
    b[0] = V_drive
    # Interior
    for i in range(1, N - 1):
        A[i, i - 1] = D / dx ** 2
        A[i, i] = -2 * D / dx ** 2 - k
        A[i, i + 1] = D / dx ** 2
        b[i] = -k * V_rest
    # Neumann at x=L (zero-flux): V[N-1] = V[N-2]
    A[N - 1, N - 1] = 1.0
    A[N - 1, N - 2] = -1.0
    b[N - 1] = 0.0
    V = np.linalg.solve(A, b)
    return x, V

def analytic(x, D, k, V_rest, V_drive):
    """Analytic solution for infinite domain: exponential decay."""
    lam = np.sqrt(D / k)
    return V_rest + (V_drive - V_rest) * np.exp(-x / lam)

def main():
    # Parameters in micrometres, seconds, millivolts
    D = 10.0            # um^2/s
    V_rest = -60.0      # mV
    V_drive = -30.0     # mV at left boundary (local depolarisation)
    L = 1000.0          # um = 1 mm
    for k in (0.1, 1.0):
        x, V = steady_state(D, k, V_rest, V_drive, L)
        Va = analytic(x, D, k, V_rest, V_drive)
        lam = (D / k) ** 0.5
        print(f"k = {k:.2f}/s, lambda = sqrt(D/k) = {lam:.2f} um")
        print(f"  V at x = 0: {V[0]:.2f} mV (drive {V_drive:.2f})")
        print(f"  V at x = 10 um: {V[2]:.2f} mV (analytic {Va[2]:.2f})")
        print(f"  V at x = 100 um: {V[20]:.2f} mV (analytic {Va[20]:.2f})")
        print(f"  V at x = L: {V[-1]:.2f} mV (rest {V_rest:.2f})")
        print()

if __name__ == "__main__":
    main()
