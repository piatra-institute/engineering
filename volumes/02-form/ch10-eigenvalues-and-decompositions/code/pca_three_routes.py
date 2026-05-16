"""
PCA implemented three ways for the chapter project:
  1. Eigendecomposition of the covariance matrix C = X_c^T X_c / (m-1)
  2. Power iteration with deflation, on the same C
  3. SVD of the centred data matrix X_c

Reports the top-k principal directions (sign-aligned), the
explained-variance ratios, and the condition numbers, then compares
against numpy's library SVD.

Supports:
  - Volume II, Chapter 10, project (PCA from scratch).

Dependencies:
  numpy

Usage:
  python pca_three_routes.py [--samples 200] [--features 10]
                             [--rank 3] [--seed 20260516]
                             [--k 3]
                             [--data path/to/data.csv]
"""

from __future__ import annotations

import argparse
import numpy as np


def synth_data(m: int, n: int, true_rank: int,
               rng: np.random.Generator) -> np.ndarray:
    """Synthesise a data matrix with planted principal directions."""
    # True latent factors in R^true_rank with decreasing variance
    Z = rng.standard_normal(size=(m, true_rank))
    Z *= np.array([5.0 ** (-i) * 10.0 for i in range(true_rank)])
    # Random orthonormal feature loadings
    G = rng.standard_normal(size=(n, true_rank))
    Q, _ = np.linalg.qr(G)
    X = Z @ Q.T + 0.05 * rng.standard_normal(size=(m, n))
    return X


def centre(X: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Subtract the column mean; return centred matrix and mean vector."""
    mu = X.mean(axis=0)
    return X - mu, mu


def pca_eig(Xc: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Route 1: eigendecomposition of the covariance C."""
    m = Xc.shape[0]
    C = Xc.T @ Xc / (m - 1)
    vals, vecs = np.linalg.eigh(C)
    order = np.argsort(-vals)
    return vals[order], vecs[:, order]


def pca_power(Xc: np.ndarray, k: int, steps: int = 200
              ) -> tuple[np.ndarray, np.ndarray]:
    """Route 2: power iteration with deflation."""
    m = Xc.shape[0]
    n = Xc.shape[1]
    C = Xc.T @ Xc / (m - 1)
    vals = np.empty(k)
    vecs = np.empty((n, k))
    C_work = C.copy()
    rng = np.random.default_rng(20260516)
    for j in range(k):
        x = rng.standard_normal(size=n)
        x /= np.linalg.norm(x)
        for _ in range(steps):
            y = C_work @ x
            x = y / np.linalg.norm(y)
        lam = float(x @ C_work @ x)
        vals[j] = lam
        vecs[:, j] = x
        # Deflate
        C_work = C_work - lam * np.outer(x, x)
    return vals, vecs


def pca_svd(Xc: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Route 3: SVD of the centred data matrix."""
    m = Xc.shape[0]
    U, s, Vt = np.linalg.svd(Xc, full_matrices=False)
    vals = (s ** 2) / (m - 1)
    return vals, Vt.T


def sign_align(V: np.ndarray, V_ref: np.ndarray) -> np.ndarray:
    """Flip sign of each column to maximise correlation with V_ref."""
    out = V.copy()
    for j in range(V.shape[1]):
        if np.dot(V[:, j], V_ref[:, j]) < 0:
            out[:, j] *= -1
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=int, default=200)
    parser.add_argument("--features", type=int, default=10)
    parser.add_argument("--rank", type=int, default=3,
                        help="True rank of synthesised data")
    parser.add_argument("--seed", type=int, default=20260516)
    parser.add_argument("--k", type=int, default=3,
                        help="Number of principal components to compare")
    parser.add_argument("--data", type=str, default=None,
                        help="Path to CSV; first row treated as header")
    args = parser.parse_args()

    if args.data is None:
        rng = np.random.default_rng(args.seed)
        X = synth_data(args.samples, args.features, args.rank, rng)
        print(f"# synthesised data: m={args.samples}, n={args.features}, "
              f"true_rank={args.rank}")
    else:
        X = np.loadtxt(args.data, delimiter=",", skiprows=1)
        print(f"# loaded data from {args.data}: shape {X.shape}")

    Xc, _ = centre(X)
    m = Xc.shape[0]
    cond_X = np.linalg.cond(Xc)
    C = Xc.T @ Xc / (m - 1)
    cond_C = np.linalg.cond(C)
    print(f"# kappa(X_c) = {cond_X:.4e}, kappa(C) = {cond_C:.4e} "
          f"(expected ratio ~ kappa(X_c)^2)")

    vals1, V1 = pca_eig(Xc)
    vals2, V2 = pca_power(Xc, args.k)
    vals3, V3 = pca_svd(Xc)

    V_ref = V3[:, :args.k]
    V1 = sign_align(V1[:, :args.k], V_ref)
    V2 = sign_align(V2[:, :args.k], V_ref)
    V3 = sign_align(V3[:, :args.k], V_ref)

    print()
    print(f"# Top {args.k} eigenvalues / variances:")
    print(f"{'i':>3} {'eig(C)':>12} {'power':>12} {'svd':>12}")
    for i in range(args.k):
        print(f"{i:3d} {vals1[i]:12.6e} {vals2[i]:12.6e} {vals3[i]:12.6e}")

    print()
    print(f"# Explained-variance ratios (cumulative):")
    total1 = vals1[: min(args.features, args.samples - 1)].sum()
    total3 = vals3[: min(args.features, args.samples - 1)].sum()
    print(f"# from eig: total = {total1:.6e}")
    print(f"# from svd: total = {total3:.6e}")
    cum = 0.0
    for i in range(args.k):
        cum += vals3[i]
        print(f"# k={i+1}: explained = {cum/total3:.4f}")

    print()
    print(f"# Pairwise sign-aligned principal-direction agreement:")
    print(f"# max|V_eig - V_svd|   = {np.abs(V1 - V3).max():.3e}")
    print(f"# max|V_power - V_svd| = {np.abs(V2 - V3).max():.3e}")


if __name__ == "__main__":
    main()
