"""FTCS explicit solver for the 1D heat equation.

Reference implementation for Volume II Chapter 12 (PDEs).

Solves u_t = alpha u_xx on 0 <= x <= L with Dirichlet boundaries
u(0,t) = u(L,t) = 0 and initial condition a midpoint-peaked
triangle. Runs at three Courant numbers r = alpha dt / dx^2 and
writes one CSV row per (r, t, x).

Usage:
    python3 heat_ftcs.py

Writes:
    ../data/heat_ftcs.csv   columns r, t, x, u
    ../data/heat_ftcs.png   line plot at r = 0.4 at three times
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np

L = 1.0
ALPHA = 1.0
N = 51                            # interior + boundary grid points
DX = L / (N - 1)
T_FINAL = 0.2
SNAPSHOTS = (0.0, 0.05, 0.10, 0.20)


def triangle(x: np.ndarray) -> np.ndarray:
    """Midpoint-peaked unit triangle on [0, L]."""
    return np.where(x <= L / 2, 2 * x / L, 2 * (L - x) / L)


def ftcs(r: float) -> dict[float, np.ndarray]:
    """Run FTCS at Courant number r; return snapshots by time."""
    dt = r * DX * DX / ALPHA
    nsteps = int(round(T_FINAL / dt))
    x = np.linspace(0.0, L, N)
    u = triangle(x)
    u[0] = u[-1] = 0.0
    snap_steps = {round(t / dt): t for t in SNAPSHOTS if t > 0}
    out: dict[float, np.ndarray] = {0.0: u.copy()}
    for n in range(1, nsteps + 1):
        u_new = u.copy()
        u_new[1:-1] = u[1:-1] + r * (u[2:] - 2 * u[1:-1] + u[:-2])
        u = u_new
        if n in snap_steps:
            out[snap_steps[n]] = u.copy()
    return out


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    data_dir = repo_root / "data"
    data_dir.mkdir(exist_ok=True)
    csv_path = data_dir / "heat_ftcs.csv"

    x = np.linspace(0.0, L, N)
    with csv_path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["r", "t", "x", "u"])
        for r in (0.40, 0.50, 0.55):
            snapshots = ftcs(r)
            for t, u in snapshots.items():
                for xi, ui in zip(x, u):
                    writer.writerow([r, t, f"{xi:.6f}", f"{ui:.6f}"])

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        snapshots = ftcs(0.40)
        fig, ax = plt.subplots(figsize=(7, 4))
        for t, u in snapshots.items():
            ax.plot(x, u, label=f"t = {t:.2f}")
        ax.set_xlabel("x")
        ax.set_ylabel("u(x, t)")
        ax.set_title("FTCS at r = 0.40")
        ax.legend()
        fig.tight_layout()
        fig.savefig(data_dir / "heat_ftcs.png", dpi=140)
    except ImportError:
        pass


if __name__ == "__main__":
    main()
