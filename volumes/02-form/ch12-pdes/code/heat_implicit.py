"""Implicit solvers (BTCS and Crank-Nicolson) for the 1D heat equation.

Reference implementation for Volume II Chapter 12 (PDEs).

Solves u_t = alpha u_xx on 0 <= x <= L with Dirichlet boundaries
u(0,t) = u(L,t) = 0 and initial condition u(x,0) = sin(pi x), whose
exact solution is u(x,t) = sin(pi x) exp(-alpha pi^2 t). Both
schemes solve a tridiagonal system per step via the Thomas
algorithm (scipy.linalg.solve_banded), so the per-step cost is
O(N) and both are unconditionally stable. The script runs each
scheme at several Courant numbers r = alpha dt / dx^2, all far
above the explicit CFL bound r <= 1/2, and reports the L2 error
against the exact solution to expose the accuracy difference:
BTCS is first order in time, Crank-Nicolson second order.

Usage:
    python3 heat_implicit.py

Writes:
    ../data/heat_implicit.csv   columns scheme, r, t, x, u, u_exact
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from scipy.linalg import solve_banded

L = 1.0
ALPHA = 1.0
N = 51                              # boundary + interior grid points
DX = L / (N - 1)
T_FINAL = 0.5
SNAPSHOTS = (0.0, 0.125, 0.25, 0.5)


def exact(x: np.ndarray, t: float) -> np.ndarray:
    """Exact fundamental-mode decay."""
    return np.sin(np.pi * x) * np.exp(-ALPHA * np.pi**2 * t)


def banded_matrix(diag: float, off: float, m: int) -> np.ndarray:
    """Build a tridiagonal matrix in solve_banded (l=u=1) layout."""
    ab = np.zeros((3, m))
    ab[0, 1:] = off          # super-diagonal
    ab[1, :] = diag          # main diagonal
    ab[2, :-1] = off         # sub-diagonal
    return ab


def step_btcs(u_in: np.ndarray, r: float) -> np.ndarray:
    """One backward-Euler step on the interior nodes."""
    m = u_in.size - 2
    ab = banded_matrix(1.0 + 2.0 * r, -r, m)
    rhs = u_in[1:-1].copy()
    u_out = u_in.copy()
    u_out[1:-1] = solve_banded((1, 1), ab, rhs)
    return u_out


def step_crank_nicolson(u_in: np.ndarray, r: float) -> np.ndarray:
    """One Crank-Nicolson step on the interior nodes."""
    m = u_in.size - 2
    ab = banded_matrix(1.0 + r, -r / 2.0, m)
    interior = u_in[1:-1]
    rhs = (1.0 - r) * interior
    rhs[1:] += (r / 2.0) * interior[:-1]
    rhs[:-1] += (r / 2.0) * interior[1:]
    u_out = u_in.copy()
    u_out[1:-1] = solve_banded((1, 1), ab, rhs)
    return u_out


def run(scheme: str, r: float) -> dict[float, np.ndarray]:
    dt = r * DX * DX / ALPHA
    nsteps = int(round(T_FINAL / dt))
    x = np.linspace(0.0, L, N)
    u = np.sin(np.pi * x)
    u[0] = u[-1] = 0.0
    stepper = step_btcs if scheme == "btcs" else step_crank_nicolson
    snap_steps = {round(t / dt): t for t in SNAPSHOTS if t > 0}
    out: dict[float, np.ndarray] = {0.0: u.copy()}
    for n in range(1, nsteps + 1):
        u = stepper(u, r)
        if n in snap_steps:
            out[snap_steps[n]] = u.copy()
    return out


def l2_error(u: np.ndarray, x: np.ndarray, t: float) -> float:
    return float(np.sqrt(np.mean((u - exact(x, t)) ** 2)))


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    data_dir = repo_root / "data"
    data_dir.mkdir(exist_ok=True)
    x = np.linspace(0.0, L, N)

    with (data_dir / "heat_implicit.csv").open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["scheme", "r", "t", "x", "u", "u_exact"])
        for scheme in ("btcs", "crank_nicolson"):
            for r in (0.4, 5.0, 26.0):
                snaps = run(scheme, r)
                for t, u in snaps.items():
                    ue = exact(x, t)
                    for xi, ui, uei in zip(x, u, ue):
                        writer.writerow(
                            [scheme, r, t, f"{xi:.6f}",
                             f"{ui:.6f}", f"{uei:.6f}"]
                        )

    # Console summary of the accuracy difference at t = T_FINAL.
    print(f"{'scheme':16s} {'r':>6s} {'L2 error at t=0.5':>20s}")
    for scheme in ("btcs", "crank_nicolson"):
        for r in (0.4, 5.0, 26.0):
            snaps = run(scheme, r)
            err = l2_error(snaps[0.5], x, 0.5)
            print(f"{scheme:16s} {r:6.1f} {err:20.3e}")


if __name__ == "__main__":
    main()
