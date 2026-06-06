# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Inverse iteration and Rayleigh-quotient iteration.

Companion to Vol II, Ch 10, section 10.6. Demonstrates:

  * fixed-shift inverse iteration converging to the eigenvalue nearest
    a chosen shift, on the matrix B with spectrum {3 +- i, 5}, and
  * Rayleigh-quotient iteration converging cubically on the symmetric
    tridiagonal A with spectrum {1, 2, 4}.

Each step solves a linear system rather than forming an inverse. The
near-singularity of (A - mu I) when mu approaches an eigenvalue is the
source of the fast convergence, not a numerical defect: the amplified
direction is exactly the eigenvector sought, and normalisation keeps
the iterate bounded.

Run:
    uv run inverse_iteration.py
"""

from __future__ import annotations

import numpy as np


def inverse_iteration(
    matrix: np.ndarray, shift: float, x0: np.ndarray, steps: int = 6
) -> list[float]:
    """Fixed-shift inverse iteration; return the Rayleigh-quotient trace."""
    n = matrix.shape[0]
    shifted = matrix - shift * np.eye(n)
    x = x0 / np.linalg.norm(x0)
    quotients: list[float] = []
    for _ in range(steps):
        y = np.linalg.solve(shifted, x)
        x = y / np.linalg.norm(y)
        quotients.append(float(x @ matrix @ x))
    return quotients


def rayleigh_quotient_iteration(
    matrix: np.ndarray, x0: np.ndarray, steps: int = 6, jitter: float = 1e-13
) -> list[float]:
    """Rayleigh-quotient iteration; cubic convergence for symmetric input."""
    n = matrix.shape[0]
    x = x0 / np.linalg.norm(x0)
    shifts: list[float] = []
    for _ in range(steps):
        mu = float(x @ matrix @ x)
        shifts.append(mu)
        a = matrix - mu * np.eye(n)
        try:
            y = np.linalg.solve(a, x)
        except np.linalg.LinAlgError:
            # Shift landed on an eigenvalue: perturb and continue.
            y = np.linalg.solve(a + jitter * np.eye(n), x)
        x = y / np.linalg.norm(y)
    return shifts


def main() -> None:
    b = np.array([[3.0, 1.0, 0.0], [-1.0, 3.0, 0.0], [0.0, 0.0, 5.0]])
    print("B spectrum:", np.round(np.linalg.eigvals(b), 6))
    qs = inverse_iteration(b, shift=4.5, x0=np.array([1.0, 1.0, 1.0]))
    print("inverse iteration, shift 4.5, Rayleigh quotients -> 5:")
    for k, q in enumerate(qs):
        print(f"  step {k}: {q:.10f}")

    a = np.array([[2.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]])
    print("\nA spectrum:", np.round(np.linalg.eigvals(a), 6))
    shifts = rayleigh_quotient_iteration(a, x0=np.array([1.0, 0.4, -0.2]))
    print("Rayleigh-quotient iteration shifts -> 2 (cubic):")
    for k, s in enumerate(shifts):
        print(f"  step {k}: {s:.12f}   error {abs(s - 2.0):.2e}")


if __name__ == "__main__":
    main()
