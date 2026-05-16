# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy", "scipy"]
# ///
"""Solve a Hilbert-matrix linear system at orders n = 5, 8, 10, 12, 14
by LU partial pivoting and by truncated SVD. Reports the relative error
against the known exact solution x = (1, 1, ..., 1).

Used by Simulation exercise 3.
"""
from __future__ import annotations

import numpy as np
from numpy.linalg import cond, lstsq, norm, solve, svd


def hilbert(n: int) -> np.ndarray:
    i = np.arange(1, n + 1)[:, None]
    j = np.arange(1, n + 1)[None, :]
    return 1.0 / (i + j - 1.0)


def svd_solve(A: np.ndarray, b: np.ndarray, rtol: float = 1e-12) -> np.ndarray:
    U, s, Vt = svd(A, full_matrices=False)
    cutoff = rtol * s[0]
    s_inv = np.where(s > cutoff, 1.0 / s, 0.0)
    return Vt.T @ (s_inv * (U.T @ b))


def main() -> None:
    print(f"{'n':>3} | {'cond(H)':>12} | {'LU err':>12} | {'SVD err':>12}")
    print("-" * 50)
    for n in (5, 8, 10, 12, 14):
        H = hilbert(n)
        x_true = np.ones(n)
        b = H @ x_true
        x_lu = solve(H, b)
        x_svd = svd_solve(H, b, rtol=1e-12)
        rel_lu = norm(x_lu - x_true) / norm(x_true)
        rel_svd = norm(x_svd - x_true) / norm(x_true)
        print(f"{n:>3} | {cond(H):>12.2e} | {rel_lu:>12.2e} | {rel_svd:>12.2e}")


if __name__ == "__main__":
    main()
