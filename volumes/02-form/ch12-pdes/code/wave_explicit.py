"""Centred explicit solver for the 1D wave equation.

Reference implementation for Volume II Chapter 12 (PDEs).

Solves u_tt = c^2 u_xx on 0 <= x <= L with Dirichlet boundaries
u(0,t) = u(L,t) = 0, initial displacement a triangular pulse,
and zero initial velocity. Runs at Courant numbers C = c dt / dx
both below and above the CFL bound C = 1 to demonstrate the
stability boundary.

Usage:
    python3 wave_explicit.py

Writes:
    ../data/wave_pulse.csv   columns C, t, x, u
    ../data/wave_pulse.png   line plot at C = 0.9 at four times
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np

L = 1.0
C = 1.0
N = 201
DX = L / (N - 1)
T_FINAL = 2.0
SNAPSHOTS = (0.0, 0.5, 1.0, 1.5, 2.0)


def initial_pulse(x: np.ndarray) -> np.ndarray:
    """Compact triangular pulse around x = 0.5, half-width 0.1."""
    return np.maximum(0.0, 1.0 - np.abs(x - 0.5) / 0.1)


def step_wave(courant: float) -> dict[float, np.ndarray]:
    dt = courant * DX / C
    nsteps = int(round(T_FINAL / dt))
    x = np.linspace(0.0, L, N)
    u_prev = initial_pulse(x)
    u = u_prev.copy()
    u[0] = u[-1] = 0.0
    # First step using the zero-initial-velocity condition:
    # u^1 = u^0 + 0.5 C^2 (u^0_{j+1} - 2 u^0_j + u^0_{j-1}).
    r2 = courant * courant
    u[1:-1] = u_prev[1:-1] + 0.5 * r2 * (
        u_prev[2:] - 2 * u_prev[1:-1] + u_prev[:-2]
    )
    out: dict[float, np.ndarray] = {0.0: u_prev.copy()}
    snap_steps = {round(t / dt): t for t in SNAPSHOTS if t > 0}
    for n in range(2, nsteps + 1):
        u_new = u.copy()
        u_new[1:-1] = (
            2 * u[1:-1] - u_prev[1:-1]
            + r2 * (u[2:] - 2 * u[1:-1] + u[:-2])
        )
        u_prev, u = u, u_new
        if n in snap_steps:
            out[snap_steps[n]] = u.copy()
    return out


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    data_dir = repo_root / "data"
    data_dir.mkdir(exist_ok=True)
    csv_path = data_dir / "wave_pulse.csv"
    x = np.linspace(0.0, L, N)
    with csv_path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["C", "t", "x", "u"])
        for courant in (0.50, 0.90):
            snaps = step_wave(courant)
            for t, u in snaps.items():
                for xi, ui in zip(x, u):
                    writer.writerow([courant, t, f"{xi:.6f}", f"{ui:.6f}"])

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        snaps = step_wave(0.90)
        fig, ax = plt.subplots(figsize=(8, 4))
        for t, u in snaps.items():
            ax.plot(x, u, label=f"t = {t:.2f}")
        ax.set_xlabel("x")
        ax.set_ylabel("u(x, t)")
        ax.set_title("Wave equation, C = 0.90")
        ax.legend(ncols=2)
        fig.tight_layout()
        fig.savefig(data_dir / "wave_pulse.png", dpi=140)
    except ImportError:
        pass


if __name__ == "__main__":
    main()
