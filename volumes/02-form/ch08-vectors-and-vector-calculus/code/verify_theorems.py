# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Numerical verification of the three integral theorems.

Each routine evaluates both sides of an integral theorem for one of the
worked examples in the chapter and reports the two values and their
relative discrepancy. The discretisations are deliberately simple
(midpoint sums and uniform parameter grids) so the reader can see the
structure rather than a black-box quadrature. Refining the grid size
``n`` drives the discrepancy toward floating-point noise, which is the
operational confirmation that the analytic equality holds.

Worked examples reproduced here:
    * Green's theorem for F = (-y, x) on the unit disc        -> 2*pi
    * Divergence theorem for F = (x^2, y^2, z^2) on unit cube -> 3
    * Stokes' theorem for F = (-y, x, 0) on the unit disc     -> 2*pi

Usage:
    uv run verify_theorems.py
    uv run verify_theorems.py --n 400
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def green_unit_disc(n: int) -> tuple[float, float]:
    """Green's theorem for F = (-y, x) on the unit disc.

    Left  (boundary line integral) is computed analytically per segment
    of a polygonal approximation of the unit circle.
    Right (double integral of curl_z = 2) is 2 * area, estimated by a
    midpoint grid over the disc.
    """
    # Boundary: polygon with n vertices on the unit circle.
    t = np.linspace(0.0, 2.0 * math.pi, n + 1)
    x, y = np.cos(t), np.sin(t)
    line = 0.0
    for i in range(n):
        dx, dy = x[i + 1] - x[i], y[i + 1] - y[i]
        # midpoint of segment
        mx, my = 0.5 * (x[i] + x[i + 1]), 0.5 * (y[i] + y[i + 1])
        # F . dr = (-y) dx + (x) dy
        line += (-my) * dx + mx * dy

    # Interior: curl_z = dQ/dx - dP/dy = 1 - (-1) = 2 over the disc.
    grid = np.linspace(-1.0, 1.0, n)
    dx = grid[1] - grid[0]
    xx, yy = np.meshgrid(grid, grid)
    inside = (xx**2 + yy**2) <= 1.0
    area_int = 2.0 * inside.sum() * dx * dx
    return line, area_int


def divergence_unit_cube(n: int) -> tuple[float, float]:
    """Divergence theorem for F = (x^2, y^2, z^2) on [0,1]^3.

    Left  (surface flux): only the faces at coordinate 1 contribute,
    each integrating its squared coordinate to 1, total 3.
    Right (volume integral of div F = 2x+2y+2z): midpoint sum.
    """
    # Surface flux, face by face, midpoint rule on each face.
    g = (np.arange(n) + 0.5) / n
    a, b = np.meshgrid(g, g)
    cell = (1.0 / n) ** 2
    flux = 0.0
    # x = 1 face: F.n = x^2 = 1 ; x = 0 face: F.n = -(0) = 0
    flux += np.sum(np.ones_like(a)) * cell
    # y = 1 face: F.n = 1 ; y = 0 face: 0
    flux += np.sum(np.ones_like(a)) * cell
    # z = 1 face: F.n = 1 ; z = 0 face: 0
    flux += np.sum(np.ones_like(a)) * cell

    # Volume integral of div F = 2x + 2y + 2z, midpoint rule.
    c = (np.arange(n) + 0.5) / n
    xx, yy, zz = np.meshgrid(c, c, c, indexing="ij")
    vol = np.sum(2.0 * xx + 2.0 * yy + 2.0 * zz) * (1.0 / n) ** 3
    return flux, vol


def stokes_unit_disc(n: int) -> tuple[float, float]:
    """Stokes' theorem for F = (-y, x, 0) on the flat unit disc.

    Left  (curl flux): curl F = (0, 0, 2); flux through the disc is
    2 * area, midpoint grid.
    Right (boundary circulation): polygonal line integral, same as the
    Green's-theorem boundary computation.
    """
    grid = np.linspace(-1.0, 1.0, n)
    dx = grid[1] - grid[0]
    xx, yy = np.meshgrid(grid, grid)
    inside = (xx**2 + yy**2) <= 1.0
    curl_flux = 2.0 * inside.sum() * dx * dx

    t = np.linspace(0.0, 2.0 * math.pi, n + 1)
    x, y = np.cos(t), np.sin(t)
    circ = 0.0
    for i in range(n):
        dxi, dyi = x[i + 1] - x[i], y[i + 1] - y[i]
        mx, my = 0.5 * (x[i] + x[i + 1]), 0.5 * (y[i] + y[i + 1])
        circ += (-my) * dxi + mx * dyi
    return curl_flux, circ


def report(name: str, left: float, right: float, exact: float) -> None:
    disc = abs(left - right) / max(abs(exact), 1e-30)
    print(f"{name}")
    print(f"    left  side : {left:+.6f}")
    print(f"    right side : {right:+.6f}")
    print(f"    exact      : {exact:+.6f}")
    print(f"    rel. discrepancy (left vs right) : {disc:.3e}")
    print()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--n", type=int, default=200, help="grid resolution")
    args = ap.parse_args()
    n = args.n

    gl, gr = green_unit_disc(n)
    report("Green's theorem, F = (-y, x), unit disc", gl, gr, 2 * math.pi)

    dl, dr = divergence_unit_cube(n)
    report("Divergence theorem, F = (x^2, y^2, z^2), unit cube", dl, dr, 3.0)

    sl, sr = stokes_unit_disc(n)
    report("Stokes' theorem, F = (-y, x, 0), unit disc", sl, sr, 2 * math.pi)


if __name__ == "__main__":
    main()
