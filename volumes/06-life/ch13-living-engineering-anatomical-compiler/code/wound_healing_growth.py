"""
wound_healing_growth.py

Two-dimensional Fisher-KPP wound-healing simulation.

Equation:  du/dt = D nabla^2 u + r u (1 - u/K)
Initial condition: circular wound (u = 0) inside healthy tissue (u = K).

Used by Vol VI Ch 13 Exercise 13.7 (simulation) to compare the
numerical wound-closure speed to the analytical Fisher-KPP wave speed
c = 2 sqrt(D r).

Reference: Fisher (1937, Ann Eugenics); Murray (2002, Mathematical
Biology, ch 13).
"""

import numpy as np

def step(u, D, r, K, dx, dt):
    """Single explicit time step (forward Euler, 5-point Laplacian)."""
    lap = (np.roll(u, 1, axis=0) + np.roll(u, -1, axis=0)
           + np.roll(u, 1, axis=1) + np.roll(u, -1, axis=1)
           - 4 * u) / dx ** 2
    growth = r * u * (1 - u / K)
    return u + dt * (D * lap + growth)

def simulate(N=200, L=2000.0, D=100.0, r=1e-4, K=1.0, R0=500.0,
             t_end=3600.0, dt=None, verbose=True):
    """Simulate wound healing on N x N grid with side length L (um)."""
    dx = L / N
    if dt is None:
        # CFL-style stability for explicit diffusion
        dt = 0.2 * dx ** 2 / D
    nsteps = int(t_end / dt)
    x = np.linspace(-L / 2, L / 2, N)
    X, Y = np.meshgrid(x, x)
    u = np.where(X ** 2 + Y ** 2 < R0 ** 2, 0.0, K)
    times = []
    radii = []
    snap = max(1, nsteps // 20)
    for n in range(nsteps):
        u = step(u, D, r, K, dx, dt)
        if n % snap == 0:
            # Wound radius: largest r where mean density < 0.5
            rr = np.sqrt(X ** 2 + Y ** 2).ravel()
            uu = u.ravel()
            order = np.argsort(rr)
            rr = rr[order]
            uu = uu[order]
            # Find rough boundary
            edge_idx = np.searchsorted(uu, 0.5 * K)
            if 0 < edge_idx < len(rr):
                radius = rr[edge_idx]
            else:
                radius = 0.0
            times.append(n * dt)
            radii.append(radius)
            if verbose:
                print(f"t = {n * dt:.0f} s, wound radius ~ {radius:.0f} um")
    return np.array(times), np.array(radii)

def main():
    D, r = 100.0, 1e-4
    c = 2 * (D * r) ** 0.5
    print(f"Analytic Fisher-KPP wave speed: c = 2 sqrt(D r) = {c:.3f} um/s")
    times, radii = simulate(N=80, t_end=2500.0, verbose=False)
    if len(times) > 1:
        dr_dt = (radii[1] - radii[-1]) / (times[-1] - times[1])
        print(f"Numerical inward speed (R decreasing): {dr_dt:.3f} um/s")

if __name__ == "__main__":
    main()
