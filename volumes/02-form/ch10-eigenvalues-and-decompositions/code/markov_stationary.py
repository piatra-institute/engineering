"""
Stationary distribution of a finite-state Markov chain by two methods:
  1. Left eigenvector of P at lambda = 1 (eigendecomposition).
  2. Direct power iteration on the row-vector recursion
     pi_{t+1} = pi_t P.

Reports the stationary distribution and the mixing time
1/(1 - |lambda_2|).

Supports:
  - Volume II, Chapter 10, Simulation exercise 4 (leaky-cycle chain).
  - Chapter section 10.5 (Markov chains).

Dependencies:
  numpy

Usage:
  python markov_stationary.py [--n 5] [--leak 0.1] [--steps 500]
"""

from __future__ import annotations

import argparse
import numpy as np


def leaky_cycle(n: int, leak: float) -> np.ndarray:
    """Construct a leaky n-cycle: state i -> (i+1) mod n with prob
    1 - leak, state i -> 0 with prob leak. Row-stochastic."""
    P = np.zeros((n, n))
    for i in range(n):
        P[i, (i + 1) % n] = 1.0 - leak
        P[i, 0] += leak
    return P


def stationary_eig(P: np.ndarray) -> np.ndarray:
    """Stationary distribution as the left eigenvector at lambda=1."""
    vals, vecs = np.linalg.eig(P.T)
    idx = int(np.argmin(np.abs(vals - 1.0)))
    pi = np.real(vecs[:, idx])
    pi = pi / pi.sum()
    return pi


def stationary_power(P: np.ndarray, steps: int,
                     pi0: np.ndarray | None = None) -> np.ndarray:
    """Stationary distribution by direct power iteration on row vectors."""
    n = P.shape[0]
    pi = np.full(n, 1.0 / n) if pi0 is None else pi0.copy()
    for _ in range(steps):
        pi = pi @ P
    return pi


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=5)
    parser.add_argument("--leak", type=float, default=0.1)
    parser.add_argument("--steps", type=int, default=500)
    args = parser.parse_args()

    P = leaky_cycle(args.n, args.leak)
    print(f"# Leaky cycle on {args.n} states, leak={args.leak}")
    print(f"# Transition matrix P:")
    for row in P:
        print("# " + "  ".join(f"{v:6.3f}" for v in row))

    pi_eig = stationary_eig(P)
    pi_pow = stationary_power(P, args.steps)

    print()
    print(f"{'state':>6} {'pi_eig':>10} {'pi_power':>10}")
    for i in range(args.n):
        print(f"{i:6d} {pi_eig[i]:10.6f} {pi_pow[i]:10.6f}")

    # Mixing rate from second-largest eigenvalue magnitude
    vals = np.linalg.eigvals(P)
    mag = np.sort(np.abs(vals))[::-1]
    lam2 = float(mag[1])
    print()
    print(f"# |lambda_1| = {mag[0]:.6f} (should be 1.0)")
    print(f"# |lambda_2| = {lam2:.6f}")
    if lam2 < 1.0:
        print(f"# mixing time approximately 1/(1 - |lambda_2|) = "
              f"{1.0/(1.0 - lam2):.2f} steps")
    else:
        print("# |lambda_2| = 1: chain is reducible or periodic; "
              "no unique stationary distribution by power iteration alone")


if __name__ == "__main__":
    main()
