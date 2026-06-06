# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Least-squares adjustment of a spirit-levelling network.

Each row of the CSV is one observed height difference (to minus from)
along a levelling run, with the run length in kilometres. Benchmark A
is held fixed at H_A = 100.000 m; the heights of B, C, D are unknown.

The observation model is linear:  l_k = H_to - H_from + noise.
With A fixed, each observation gives one row of a design matrix A_des
in the unknowns x = (H_B, H_C, H_D).  Standard levelling practice
weights each run by the inverse of its length (variance grows with
distance), so this is a *weighted* least-squares problem solved both
by the weighted normal equations and by a QR on the whitened system.

Usage:
    uv run code/leveling_adjustment.py [csv_path]
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

H_FIXED = {"A": 100.000}
UNKNOWNS = ["B", "C", "D"]


def build_system(rows):
    idx = {name: j for j, name in enumerate(UNKNOWNS)}
    m, n = len(rows), len(UNKNOWNS)
    A = np.zeros((m, n))
    b = np.zeros(m)
    w = np.zeros(m)
    for k, (frm, to, diff, length) in enumerate(rows):
        b[k] = diff
        w[k] = 1.0 / length  # inverse-distance weight
        if to in idx:
            A[k, idx[to]] += 1.0
        else:
            b[k] -= H_FIXED[to]
        if frm in idx:
            A[k, idx[frm]] -= 1.0
        else:
            b[k] += H_FIXED[frm]
    return A, b, w


def main() -> None:
    csv_path = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else Path(__file__).resolve().parent.parent / "data" / "leveling-network.csv"
    )
    raw = np.genfromtxt(csv_path, delimiter=",", dtype=None, names=True, encoding="utf-8")
    rows = [(r["from"], r["to"], float(r["observed_diff_m"]), float(r["run_length_km"]))
            for r in raw]

    A, b, w = build_system(rows)
    W = np.diag(w)
    sqrtW = np.diag(np.sqrt(w))

    # Weighted normal equations: (A^T W A) x = A^T W b
    G = A.T @ W @ A
    rhs = A.T @ W @ b
    x_ne = np.linalg.solve(G, rhs)

    # QR on the whitened system sqrtW A x = sqrtW b
    Aw, bw = sqrtW @ A, sqrtW @ b
    Q, R = np.linalg.qr(Aw, mode="reduced")
    x_qr = np.linalg.solve(R, Q.T @ bw)

    resid = A @ x_qr - b
    # Reference variance: weighted residual sum of squares / redundancy
    redundancy = A.shape[0] - A.shape[1]
    sigma0_sq = float(resid @ W @ resid) / redundancy
    cov = sigma0_sq * np.linalg.inv(G)
    stderr = np.sqrt(np.diag(cov))

    print(f"observations m = {A.shape[0]}  unknowns n = {A.shape[1]}  "
          f"redundancy = {redundancy}")
    print(f"kappa(A)       = {np.linalg.cond(A):.3e}")
    print(f"kappa(A^T W A) = {np.linalg.cond(G):.3e}")
    print()
    print(f"{'BM':>3} {'height (NE)':>14} {'height (QR)':>14} {'std err (m)':>12}")
    for j, name in enumerate(UNKNOWNS):
        print(f"{name:>3} {x_ne[j]:>14.4f} {x_qr[j]:>14.4f} {stderr[j]:>12.4f}")
    print()
    print("per-run residuals (m):")
    for (frm, to, *_), r in zip(rows, resid):
        print(f"  {frm}->{to}: {r:+.4f}")
    print(f"\nreference standard deviation sigma_0 = {np.sqrt(sigma0_sq):.4f}")


if __name__ == "__main__":
    main()
