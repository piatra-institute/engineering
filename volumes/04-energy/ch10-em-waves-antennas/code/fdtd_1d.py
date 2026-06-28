"""One-dimensional FDTD solver for the wave equation on a transmission line.

A leapfrog finite-difference time-domain update of the lossless telegrapher's
equations on a normalised line. A sinusoidal source is injected at the left end
and a one-way (Mur first-order) absorbing boundary terminates the right end so
the line behaves as if matched. This is the reference implementation for the
simulation exercise on FDTD and numerical dispersion.

The Courant number S = c dt / dz controls stability and dispersion; S = 1 is
the magic time step at which the 1D scheme is dispersion-free.
"""

from __future__ import annotations


def fdtd_1d(n_cells: int = 400, n_steps: int = 800,
            courant: float = 0.5, freq_cells: float = 40.0):
    """Run the solver; return the final voltage and current arrays.

    n_cells     spatial cells; freq_cells is the source period in time steps.
    courant     Courant number S = c dt / dz (1.0 is dispersion-free in 1D).
    """
    import math

    v = [0.0] * (n_cells + 1)   # voltage nodes 0..n_cells
    i = [0.0] * n_cells         # current nodes (staggered half cells)

    coeff = (courant - 1.0) / (courant + 1.0)  # Mur first-order ABC coefficient

    for step in range(n_steps):
        # update current from the voltage gradient
        for k in range(n_cells):
            i[k] += courant * (v[k + 1] - v[k])
        # remember the old interior node before overwriting the boundary
        v_interior_old = v[n_cells - 1]
        v_boundary_old = v[n_cells]
        # update voltage from the current gradient (interior nodes)
        for k in range(1, n_cells):
            v[k] += courant * (i[k] - i[k - 1])
        # hard sinusoidal source at the left node
        v[0] = math.sin(2.0 * math.pi * step / freq_cells)
        # first-order Mur absorbing boundary at the right node
        v[n_cells] = v_interior_old + coeff * (v[n_cells - 1] - v_boundary_old)

    return v, i


if __name__ == "__main__":
    v, _ = fdtd_1d()
    peak = max(abs(x) for x in v)
    print(f"final peak |V| on the line = {peak:.3f}")
    print("at the magic time step S = 1 the wave propagates without dispersion")
