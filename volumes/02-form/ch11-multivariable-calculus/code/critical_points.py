# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "numpy",
# ]
# ///
"""
Locate and classify critical points of f(x, y) = sin(x) cos(y) on
[0, 2 pi]^2. Supports the Simulation exercise on numerical
critical-point location.

The gradient vanishes when cos(x) cos(y) = 0 and -sin(x) sin(y) = 0,
which gives the lattice (x, y) in { pi/2, 3 pi/2 } x { 0, pi, 2 pi }
union { 0, pi, 2 pi } x { pi/2, 3 pi/2 }. The script enumerates
candidates by scanning a coarse grid, refines each by Newton's
method on the gradient, then classifies by the Hessian eigenvalues.

Usage:
    python critical_points.py
"""

from __future__ import annotations
import math
from dataclasses import dataclass

import numpy as np


def grad(x: float, y: float) -> np.ndarray:
    return np.array([math.cos(x) * math.cos(y), -math.sin(x) * math.sin(y)])


def hess(x: float, y: float) -> np.ndarray:
    return np.array([
        [-math.sin(x) * math.cos(y), -math.cos(x) * math.sin(y)],
        [-math.cos(x) * math.sin(y), -math.sin(x) * math.cos(y)],
    ])


@dataclass(frozen=True)
class Critical:
    x: float
    y: float
    f_value: float
    eigenvalues: tuple[float, float]
    classification: str


def classify(eigs: np.ndarray) -> str:
    if np.all(eigs > 1e-9):
        return "minimum"
    if np.all(eigs < -1e-9):
        return "maximum"
    if np.any(eigs > 1e-9) and np.any(eigs < -1e-9):
        return "saddle"
    return "degenerate"


def newton_refine(x: float, y: float, max_iter: int = 50, tol: float = 1e-12) -> tuple[float, float]:
    for _ in range(max_iter):
        g = grad(x, y)
        if np.linalg.norm(g) < tol:
            return x, y
        h = hess(x, y)
        try:
            step = np.linalg.solve(h, g)
        except np.linalg.LinAlgError:
            return x, y
        x -= float(step[0])
        y -= float(step[1])
    return x, y


def main() -> None:
    seen: list[tuple[float, float]] = []
    criticals: list[Critical] = []
    grid = np.linspace(0.0, 2.0 * math.pi, 25)
    for x0 in grid:
        for y0 in grid:
            x, y = newton_refine(float(x0), float(y0))
            if not (0.0 <= x <= 2.0 * math.pi and 0.0 <= y <= 2.0 * math.pi):
                continue
            if any(abs(x - sx) < 1e-4 and abs(y - sy) < 1e-4 for sx, sy in seen):
                continue
            if np.linalg.norm(grad(x, y)) > 1e-6:
                continue
            seen.append((x, y))
            eigs = np.linalg.eigvalsh(hess(x, y))
            cls = classify(eigs)
            criticals.append(Critical(x, y, math.sin(x) * math.cos(y),
                                      (float(eigs[0]), float(eigs[1])), cls))

    criticals.sort(key=lambda c: (round(c.x, 3), round(c.y, 3)))
    print(f"{'x':>8} {'y':>8} {'f(x,y)':>10} {'lambda_1':>10} {'lambda_2':>10}  type")
    for c in criticals:
        print(f"{c.x:8.4f} {c.y:8.4f} {c.f_value:10.4f} "
              f"{c.eigenvalues[0]:10.4f} {c.eigenvalues[1]:10.4f}  {c.classification}")
    print(f"\nfound {len(criticals)} critical points in [0, 2 pi]^2.")


if __name__ == "__main__":
    main()
