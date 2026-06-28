"""Finite-difference solver for Laplace's equation in 2D, applied to a
parallel-plate capacitor with finite plates.

Solves nabla^2 phi = 0 on a square grid by Gauss-Seidel relaxation with
Dirichlet boundaries: two horizontal plates held at +V and -V inside a
grounded box. Computes the stored energy U = (eps0/2) integral |grad phi|^2
and infers a capacitance C = 2U / V^2 per unit depth, then compares to the
infinite-plate value eps0 * (plate width) / gap. The ratio C/C_infinite is
the fringing-field correction, reported against plate aspect ratio
(width / gap). Supports the Section 8.8 worked example and the simulation
exercise.
"""

import numpy as np

EPS0 = 8.8541878128e-12  # F/m


def solve(nx=201, ny=201, plate_frac=0.5, gap_frac=0.2, volts=1.0,
          tol=1e-6, max_iter=20000):
    phi = np.zeros((ny, nx))
    fixed = np.zeros((ny, nx), bool)

    cx = nx // 2
    cy = ny // 2
    half_w = int(plate_frac * nx / 2)
    half_g = int(gap_frac * ny / 2)

    top = cy - half_g
    bot = cy + half_g
    x0, x1 = cx - half_w, cx + half_w

    phi[top, x0:x1] = +volts
    fixed[top, x0:x1] = True
    phi[bot, x0:x1] = -volts
    fixed[bot, x0:x1] = True
    # grounded box boundary stays at zero and fixed
    fixed[0, :] = fixed[-1, :] = fixed[:, 0] = fixed[:, -1] = True

    for it in range(max_iter):
        old = phi.copy()
        phi[1:-1, 1:-1] = np.where(
            fixed[1:-1, 1:-1],
            phi[1:-1, 1:-1],
            0.25 * (phi[:-2, 1:-1] + phi[2:, 1:-1]
                    + phi[1:-1, :-2] + phi[1:-1, 2:]),
        )
        if np.max(np.abs(phi - old)) < tol:
            break
    return phi, it


def capacitance_per_depth(phi, volts, h=1.0):
    """C per unit depth from U = (eps0/2) sum |grad phi|^2 * cell area."""
    gy, gx = np.gradient(phi, h)
    energy = 0.5 * EPS0 * np.sum(gx ** 2 + gy ** 2) * h * h
    return 2.0 * energy / (2.0 * volts) ** 2  # plates at +V and -V => 2V across


if __name__ == "__main__":
    for aspect in (2.5, 5.0, 10.0):
        gap = 0.2
        plate = aspect * gap
        phi, iters = solve(plate_frac=min(plate, 0.9), gap_frac=gap)
        C = capacitance_per_depth(phi, 1.0)
        C_inf = EPS0 * (plate) / gap  # crude infinite-plate scaling
        print(f"aspect {aspect:5.1f}: C/C_inf ~ {C / C_inf:5.3f}  "
              f"(fringing surplus), {iters} iters")
