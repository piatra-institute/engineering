"""Transient one-dimensional diffusion in a slab by finite differences.

Solves Fick's second law dc/dt = D d2c/dx2 on 0 <= x <= L with a fixed
surface concentration at x = 0 and a no-flux symmetry plane at x = L,
starting from a uniform initial concentration. Uses the explicit FTCS
scheme; the stability limit is D dt / dx^2 <= 0.5.

The early-time response matches the semi-infinite error-function
solution; this script reports the penetration depth as a check.

Usage:
    python transient_diffusion.py
"""

from __future__ import annotations


def solve(D: float, L: float, c_surface: float, c_init: float,
          t_end: float, nx: int = 101) -> dict:
    dx = L / (nx - 1)
    dt = 0.4 * dx * dx / D          # keep below the 0.5 stability limit
    r = D * dt / (dx * dx)

    c = [c_init] * nx
    c[0] = c_surface
    t = 0.0
    steps = 0
    while t < t_end:
        new = c[:]
        for i in range(1, nx - 1):
            new[i] = c[i] + r * (c[i + 1] - 2.0 * c[i] + c[i - 1])
        # no-flux (symmetry) at the far face: mirror the interior node
        new[-1] = c[-1] + r * (2.0 * c[-2] - 2.0 * c[-1])
        new[0] = c_surface
        c = new
        t += dt
        steps += 1

    # penetration depth: first node where c has barely moved from c_init
    pen = L
    for i, ci in enumerate(c):
        if abs(ci - c_init) < 0.01 * abs(c_surface - c_init):
            pen = i * dx
            break
    return {"profile": c, "dx": dx, "steps": steps,
            "penetration_m": pen, "diffusive_scale_m": (D * t_end) ** 0.5}


if __name__ == "__main__":
    out = solve(D=2.1e-9, L=0.05, c_surface=8.0, c_init=0.0, t_end=3600.0)
    print(f"steps              : {out['steps']}")
    print(f"penetration depth  : {out['penetration_m']:.4f} m")
    print(f"sqrt(D t) scale    : {out['diffusive_scale_m']:.4f} m")
