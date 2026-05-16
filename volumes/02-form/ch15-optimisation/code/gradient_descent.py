# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Gradient descent on the elongated quadratic of Section 15.5.

Demonstrates the zigzag behaviour predicted by the convergence theorem
of gradient descent on a strongly convex quadratic with condition
number kappa = L / mu. For f(x_1, x_2) = 0.5 (x_1^2 + 100 x_2^2),
mu = 1, L = 100, kappa = 100. The constant-step iteration
x_{k+1} = x_k - eta grad f(x_k) converges geometrically with rate
(1 - mu / L) per step in the strong-direction component and oscillates
in the steep direction whenever eta * L > 1.

Sweeps three step sizes and reports the iteration count to reach
||x_k|| < 1e-6 from x_0 = (1.0, 1.0), or 'diverged' if ||x_k|| > 1e6
within the iteration cap.
"""

from __future__ import annotations

import numpy as np

ITER_CAP = 50_000
TOL = 1e-6
DIV_THRESHOLD = 1e6
HESSIAN_EIGENVALUES = np.array([1.0, 100.0])


def grad_f(x: np.ndarray) -> np.ndarray:
    """Gradient of f(x) = 0.5 (x_1^2 + 100 x_2^2)."""
    return HESSIAN_EIGENVALUES * x


def f(x: np.ndarray) -> float:
    return float(0.5 * np.sum(HESSIAN_EIGENVALUES * x * x))


def run(eta: float, x0: np.ndarray) -> tuple[str, int, float]:
    x = x0.copy()
    for k in range(ITER_CAP):
        n = float(np.linalg.norm(x))
        if n < TOL:
            return ("converged", k, f(x))
        if n > DIV_THRESHOLD:
            return ("diverged", k, f(x))
        x = x - eta * grad_f(x)
    return ("max-iter", ITER_CAP, f(x))


def main() -> None:
    x0 = np.array([1.0, 1.0])
    print("Gradient descent on f(x) = 0.5 (x_1^2 + 100 x_2^2)")
    print("kappa = 100; predicted optimal constant step eta_opt = 2/(L+mu) ~ 0.0198")
    print()
    print(f"{'eta':>10}  {'status':>12}  {'iters':>8}  {'final f':>14}")
    for eta in (1e-3, 1e-2, 2e-2, 2.5e-2):
        status, iters, fv = run(eta, x0)
        print(f"{eta:>10.4f}  {status:>12}  {iters:>8d}  {fv:>14.4e}")


if __name__ == "__main__":
    main()
