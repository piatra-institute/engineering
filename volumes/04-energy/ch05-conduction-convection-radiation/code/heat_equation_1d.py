"""Explicit finite-difference solver for the one-dimensional heat equation.

Solves dT/dt = alpha d2T/dx2 in a slab with Dirichlet boundary conditions, on a
uniform grid, with the forward-time centred-space scheme. The scheme is stable
when the mesh Fourier number alpha dt / dx^2 stays at or below 1/2; the solver
checks this and reports it. Used in the simulation exercises to compare the
transient against the semi-infinite-solid error-function solution at short
times.

SI units throughout: metres, seconds, kelvin.
"""

from __future__ import annotations

import math


def stability_number(alpha, dt, dx):
    """Mesh Fourier number; the explicit scheme is stable for values <= 0.5."""
    return alpha * dt / dx ** 2


def step(temps, fo):
    """Advance one explicit time step (interior nodes), Dirichlet ends fixed."""
    new = temps[:]
    for i in range(1, len(temps) - 1):
        new[i] = temps[i] + fo * (temps[i + 1] - 2.0 * temps[i] + temps[i - 1])
    return new


def solve_slab(length, alpha, t_initial, t_left, t_right, n_nodes, dt, n_steps):
    """March the slab forward in time.

    Returns the grid positions and the final temperature field. Raises if the
    chosen time step violates the explicit stability limit.
    """
    dx = length / (n_nodes - 1)
    fo = stability_number(alpha, dt, dx)
    if fo > 0.5:
        raise ValueError(f"unstable: mesh Fourier number {fo:.3f} exceeds 0.5")

    temps = [t_initial] * n_nodes
    temps[0] = t_left
    temps[-1] = t_right
    for _ in range(n_steps):
        temps = step(temps, fo)
        temps[0] = t_left
        temps[-1] = t_right

    x = [i * dx for i in range(n_nodes)]
    return x, temps


def semi_infinite_erf(x, t, alpha, t_initial, t_surface):
    """Analytical semi-infinite-solid profile after a surface step change."""
    arg = x / (2.0 * math.sqrt(alpha * t))
    return t_surface + (t_initial - t_surface) * math.erf(arg)


if __name__ == "__main__":
    # Concrete slab, surface stepped from 20 C to 0 C.
    alpha = 5.0e-7
    length = 0.30
    n = 61
    dx = length / (n - 1)
    dt = 0.4 * dx ** 2 / alpha  # keep Fourier number at 0.4
    steps = 600
    x, temps = solve_slab(length, alpha, 20.0, 0.0, 20.0, n, dt, steps)
    t_final = dt * steps
    print(f"t = {t_final:.0f} s, mesh Fo = {stability_number(alpha, dt, dx):.3f}")
    for i in (0, 5, 10, 20, 40, 60):
        exact = semi_infinite_erf(x[i], t_final, alpha, 20.0, 0.0)
        print(f"  x={x[i]*1000:5.0f} mm: FD={temps[i]:6.2f} C  erf={exact:6.2f} C")
