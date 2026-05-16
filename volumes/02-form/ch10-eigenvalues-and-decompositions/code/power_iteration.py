"""
Power iteration on a dense square matrix, with Rayleigh-quotient
convergence tracking.

Supports:
  - Volume II, Chapter 10, Simulation exercise 1 (geometric convergence
    of the Rayleigh quotient on a random symmetric matrix).
  - Volume II, Chapter 10, Simulation exercise 2 (deflation to find
    the next eigenpair after the dominant one).

Dependencies:
  numpy

Usage:
  python power_iteration.py [--n 50] [--steps 200] [--seed 20260516]
"""

from __future__ import annotations

import argparse
import numpy as np


def random_symmetric(n: int, rng: np.random.Generator) -> np.ndarray:
    """Random symmetric matrix with entries from N(0, 1)."""
    g = rng.standard_normal(size=(n, n))
    return 0.5 * (g + g.T)


def power_iteration(A: np.ndarray, steps: int,
                    x0: np.ndarray | None = None,
                    rng: np.random.Generator | None = None
                    ) -> tuple[np.ndarray, np.ndarray]:
    """Run `steps` power iterations on A and return the history of
    Rayleigh quotients and the final unit-norm iterate.
    """
    n = A.shape[0]
    if rng is None:
        rng = np.random.default_rng(seed=20260516)
    if x0 is None:
        x0 = rng.standard_normal(size=n)
    x = x0 / np.linalg.norm(x0)
    history = np.empty(steps)
    for t in range(steps):
        y = A @ x
        x = y / np.linalg.norm(y)
        history[t] = float(x @ A @ x)  # Rayleigh quotient
    return history, x


def deflate(A: np.ndarray, lam: float, v: np.ndarray) -> np.ndarray:
    """Symmetric deflation: subtract the rank-one component lam * v v^T."""
    return A - lam * np.outer(v, v)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=50)
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--seed", type=int, default=20260516)
    parser.add_argument("--deflate", action="store_true",
                        help="Also compute the second eigenpair by deflation")
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    A = random_symmetric(args.n, rng)

    # Reference eigendecomposition for ground truth
    w, V = np.linalg.eigh(A)
    order = np.argsort(-np.abs(w))
    lam1_true = w[order[0]]
    lam2_true = w[order[1]]
    ratio = abs(lam2_true / lam1_true)

    history, v1_est = power_iteration(A, args.steps, rng=rng)
    err = np.abs(history - lam1_true)

    print(f"# n={args.n}, steps={args.steps}, seed={args.seed}")
    print(f"# true |lambda_1| = {abs(lam1_true):.6f}")
    print(f"# true |lambda_2| = {abs(lam2_true):.6f}")
    print(f"# ratio |lambda_2/lambda_1| = {ratio:.4f}")
    print(f"# expected error after t steps: ratio^t")
    print()
    print(f"{'t':>5} {'rayleigh':>14} {'|error|':>14} "
          f"{'expected':>14}")
    for t in range(0, args.steps, max(1, args.steps // 20)):
        expected = ratio ** t
        print(f"{t:5d} {history[t]:14.6f} {err[t]:14.3e} {expected:14.3e}")

    if args.deflate:
        print("\n# Deflation: subtract lambda_1 * v1 * v1^T and re-iterate")
        Ad = deflate(A, history[-1], v1_est)
        history2, v2_est = power_iteration(Ad, args.steps, rng=rng)
        err2 = np.abs(history2[-1] - lam2_true)
        print(f"# deflated dominant Rayleigh quotient = {history2[-1]:.6f}")
        print(f"# true lambda_2 = {lam2_true:.6f}")
        print(f"# |error| after deflation = {err2:.3e}")


if __name__ == "__main__":
    main()
