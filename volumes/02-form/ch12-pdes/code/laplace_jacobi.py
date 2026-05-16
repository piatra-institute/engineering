"""Jacobi relaxation for Laplace's equation on the unit square.

Reference implementation for Volume II Chapter 12 (PDEs).

Solves nabla^2 u = 0 on [0,1] x [0,1] with Dirichlet boundary
data u(x,1) = sin(pi x), zero elsewhere. Iterates until the
maximum change between sweeps falls below TOL. Records the
sweep count, the residual history, and the converged field.

Usage:
    python3 laplace_jacobi.py

Writes:
    ../data/laplace_jacobi.csv   columns x, y, u
    ../data/laplace.png          contour plot of the converged field
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np

N = 81                       # grid points per side, including boundary
TOL = 1.0e-6
MAX_SWEEPS = 200_000


def jacobi() -> tuple[np.ndarray, int, list[float]]:
    u = np.zeros((N, N), dtype=np.float64)
    x = np.linspace(0.0, 1.0, N)
    u[-1, :] = np.sin(np.pi * x)  # top edge u(x, 1) = sin(pi x)
    history: list[float] = []
    for sweep in range(1, MAX_SWEEPS + 1):
        u_new = u.copy()
        u_new[1:-1, 1:-1] = 0.25 * (
            u[2:, 1:-1] + u[:-2, 1:-1] + u[1:-1, 2:] + u[1:-1, :-2]
        )
        delta = float(np.max(np.abs(u_new - u)))
        history.append(delta)
        u = u_new
        if delta < TOL:
            return u, sweep, history
    return u, MAX_SWEEPS, history


def analytic(N: int) -> np.ndarray:
    x = np.linspace(0.0, 1.0, N)
    y = np.linspace(0.0, 1.0, N)
    X, Y = np.meshgrid(x, y, indexing="xy")
    return np.sin(np.pi * X) * np.sinh(np.pi * Y) / np.sinh(np.pi)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    data_dir = repo_root / "data"
    data_dir.mkdir(exist_ok=True)

    u, sweeps, _history = jacobi()
    u_exact = analytic(N)
    rmse = float(np.sqrt(np.mean((u - u_exact) ** 2)))
    print(f"Jacobi converged in {sweeps} sweeps; RMSE vs analytic = {rmse:.3e}")

    x = np.linspace(0.0, 1.0, N)
    y = np.linspace(0.0, 1.0, N)
    csv_path = data_dir / "laplace_jacobi.csv"
    with csv_path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["x", "y", "u"])
        for j, yj in enumerate(y):
            for i, xi in enumerate(x):
                writer.writerow([f"{xi:.6f}", f"{yj:.6f}", f"{u[j, i]:.6f}"])

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(5, 5))
        cs = ax.contourf(x, y, u, levels=20, cmap="viridis")
        ax.contour(x, y, u, levels=10, colors="black", linewidths=0.5)
        fig.colorbar(cs, ax=ax, label="u(x, y)")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_aspect("equal")
        ax.set_title("Laplace, Jacobi relaxation")
        fig.tight_layout()
        fig.savefig(data_dir / "laplace.png", dpi=140)
    except ImportError:
        pass


if __name__ == "__main__":
    main()
