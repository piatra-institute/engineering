# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Polynomial least-squares fit by three methods, with conditioning report.

Reads two-column CSV (header x,y); fits degree p (default 6) by
  1. Normal equations solved by LU,
  2. QR via Householder (numpy default),
  3. SVD with truncation cutoff eps * sigma_1, eps = 1e-12.
Reports the three condition numbers, the coefficient vectors,
and the residual 2-norms.

Usage:
    uv run code/least_squares_three_ways.py [csv_path] [degree]
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np


def fit_normal_equations(V: np.ndarray, y: np.ndarray) -> np.ndarray:
    G = V.T @ V
    rhs = V.T @ y
    return np.linalg.solve(G, rhs)


def fit_qr(V: np.ndarray, y: np.ndarray) -> np.ndarray:
    Q, R = np.linalg.qr(V, mode="reduced")
    return np.linalg.solve(R, Q.T @ y)


def fit_svd(V: np.ndarray, y: np.ndarray, eps: float = 1e-12) -> tuple[np.ndarray, np.ndarray, int]:
    U, S, Vt = np.linalg.svd(V, full_matrices=False)
    cutoff = eps * S[0]
    S_inv = np.where(S > cutoff, 1.0 / S, 0.0)
    kept = int(np.sum(S > cutoff))
    coeffs = Vt.T @ (S_inv * (U.T @ y))
    return coeffs, S, kept


def main() -> None:
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else \
        Path(__file__).resolve().parent.parent / "data" / "temperature-sample.csv"
    degree = int(sys.argv[2]) if len(sys.argv) > 2 else 6

    data = np.loadtxt(csv_path, delimiter=",", skiprows=1)
    x, y = data[:, 0], data[:, 1]
    # Rescale x to [-1, 1] for the SVD/QR comparison? Report raw, per project.
    V = np.vander(x, N=degree + 1, increasing=True)

    c_ne = fit_normal_equations(V, y)
    c_qr = fit_qr(V, y)
    c_svd, S, kept = fit_svd(V, y)

    kV = np.linalg.cond(V)
    kG = np.linalg.cond(V.T @ V)

    print(f"dataset: {csv_path.name}  m = {x.size}  degree p = {degree}")
    print(f"kappa(V)            = {kV:.3e}")
    print(f"kappa(V^T V)        = {kG:.3e}  (rule of thumb: {np.log10(kG):.1f} digits lost)")
    print(f"singular values     = {S}")
    print(f"SVD retained        = {kept} of {S.size}")
    print()
    header = f"{'i':>3} {'normal eq':>14} {'QR':>14} {'SVD':>14}"
    print(header)
    for i, (a, b, c) in enumerate(zip(c_ne, c_qr, c_svd)):
        print(f"{i:>3} {a:>14.6e} {b:>14.6e} {c:>14.6e}")
    print()
    print(f"residual ||V c - y||_2: NE {np.linalg.norm(V @ c_ne - y):.4e}  "
          f"QR {np.linalg.norm(V @ c_qr - y):.4e}  "
          f"SVD {np.linalg.norm(V @ c_svd - y):.4e}")


if __name__ == "__main__":
    main()
