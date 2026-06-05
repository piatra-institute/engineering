"""
PageRank on a small web graph, by power iteration on the Google matrix.

Reproduces the four-page worked example in Volume II, Chapter 10,
section 10.6 (Power iteration and PageRank). Builds the raw link
matrix H, applies the dangling-node and teleportation corrections to
form the Google matrix G = alpha*H' + (1 - alpha)*1 u^T, and computes
the stationary distribution (the PageRank vector) by power iteration.
Also reports the dominant and second eigenvalues so the reader can see
the spectral-gap bound |lambda_2| <= alpha that governs convergence.

Supports:
  - Chapter section 10.6 (PageRank worked example, four-page web).
  - Diagnosis exercise on a diverging PageRank iteration (row-sum check).

Dependencies:
  numpy

Usage:
  python pagerank_small.py [--alpha 0.85] [--steps 100]
"""

from __future__ import annotations

import argparse
import numpy as np


def link_matrix(adjacency: list[list[int]]) -> np.ndarray:
    """Row-normalised link matrix H[i, j] = 1/deg(i) for i -> j.

    A dangling node (no out-links) is left as an all-zero row; the
    Google-matrix construction repairs it.
    """
    n = len(adjacency)
    H = np.zeros((n, n))
    for i, targets in enumerate(adjacency):
        if targets:
            for j in targets:
                H[i, j] = 1.0 / len(targets)
    return H


def google_matrix(H: np.ndarray, alpha: float) -> np.ndarray:
    """Form G = alpha*H' + (1 - alpha)*1 u^T with dangling repair.

    H' replaces every all-zero (dangling) row of H with the uniform
    distribution u = 1/n, making H' row-stochastic. The teleportation
    term mixes in the uniform distribution with weight 1 - alpha,
    making G strictly positive, irreducible, and aperiodic.
    """
    n = H.shape[0]
    u = np.full(n, 1.0 / n)
    Hp = H.copy()
    for i in range(n):
        if Hp[i].sum() == 0.0:
            Hp[i] = u
    return alpha * Hp + (1.0 - alpha) * np.outer(np.ones(n), u)


def pagerank_power(G: np.ndarray, steps: int,
                   tol: float = 1e-12) -> tuple[np.ndarray, int]:
    """PageRank vector by power iteration on row vectors pi <- pi G."""
    n = G.shape[0]
    pi = np.full(n, 1.0 / n)
    for t in range(1, steps + 1):
        nxt = pi @ G
        if np.linalg.norm(nxt - pi, 1) < tol:
            return nxt / nxt.sum(), t
        pi = nxt
    return pi / pi.sum(), steps


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--alpha", type=float, default=0.85)
    parser.add_argument("--steps", type=int, default=100)
    args = parser.parse_args()

    # Four-page web of section 10.6:
    #   page 0 -> {1, 2}, page 1 -> {2}, page 2 -> {0}, page 3 -> {2}
    adjacency = [[1, 2], [2], [0], [2]]
    H = link_matrix(adjacency)
    G = google_matrix(H, args.alpha)

    print(f"# Four-page web, alpha = {args.alpha}")
    print("# Raw link matrix H (row sums shown):")
    for i, row in enumerate(H):
        print("# " + "  ".join(f"{v:5.2f}" for v in row)
              + f"   | sum = {row.sum():.2f}")

    pi, iters = pagerank_power(G, args.steps)
    order = np.argsort(pi)[::-1]

    print()
    print(f"{'page':>5} {'pagerank':>10}")
    for j in range(len(pi)):
        print(f"{j:5d} {pi[j]:10.4f}")
    print()
    print("# ranking (high to low): "
          + " > ".join(f"page {j}" for j in order))
    print(f"# converged in {iters} iterations")

    # Spectral-gap check: second eigenvalue magnitude bounded by alpha.
    vals = np.linalg.eigvals(G.T)
    mag = np.sort(np.abs(vals))[::-1]
    print(f"# |lambda_1| = {mag[0]:.4f} (should be 1.0)")
    print(f"# |lambda_2| = {mag[1]:.4f} (bounded by alpha = {args.alpha})")


if __name__ == "__main__":
    main()
