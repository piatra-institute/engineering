# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Three first-order methods on the Rosenbrock function.

Compares vanilla gradient descent, gradient descent with momentum
(decay beta = 0.9), and Adam on the classical Rosenbrock benchmark

    f(x, y) = (1 - x)^2 + 100 (y - x^2)^2

from the difficult start (x_0, y_0) = (-1.0, 1.0). The global optimum
is at (1, 1) with f = 0. The narrow curved valley exposes the
zigzag pathology of plain gradient descent and the value of momentum
on a nonconvex objective.

Reports iteration count to reach f < 1e-4 and the final loss after
ITER_CAP iterations for each method.
"""

from __future__ import annotations

import numpy as np

ITER_CAP = 20_000
TARGET = 1e-4


def f(x: np.ndarray) -> float:
    return float((1.0 - x[0]) ** 2 + 100.0 * (x[1] - x[0] ** 2) ** 2)


def grad_f(x: np.ndarray) -> np.ndarray:
    dx = -2.0 * (1.0 - x[0]) - 400.0 * x[0] * (x[1] - x[0] ** 2)
    dy = 200.0 * (x[1] - x[0] ** 2)
    return np.array([dx, dy])


def gd(x0: np.ndarray, eta: float) -> tuple[int, float]:
    x = x0.copy()
    for k in range(ITER_CAP):
        if f(x) < TARGET:
            return (k, f(x))
        x = x - eta * grad_f(x)
    return (ITER_CAP, f(x))


def gd_momentum(x0: np.ndarray, eta: float, beta: float = 0.9) -> tuple[int, float]:
    x = x0.copy()
    v = np.zeros_like(x)
    for k in range(ITER_CAP):
        if f(x) < TARGET:
            return (k, f(x))
        v = beta * v + grad_f(x)
        x = x - eta * v
    return (ITER_CAP, f(x))


def adam(
    x0: np.ndarray,
    eta: float = 1e-2,
    b1: float = 0.9,
    b2: float = 0.999,
    eps: float = 1e-8,
) -> tuple[int, float]:
    x = x0.copy()
    m = np.zeros_like(x)
    v = np.zeros_like(x)
    for k in range(1, ITER_CAP + 1):
        if f(x) < TARGET:
            return (k - 1, f(x))
        g = grad_f(x)
        m = b1 * m + (1.0 - b1) * g
        v = b2 * v + (1.0 - b2) * g * g
        mhat = m / (1.0 - b1 ** k)
        vhat = v / (1.0 - b2 ** k)
        x = x - eta * mhat / (np.sqrt(vhat) + eps)
    return (ITER_CAP, f(x))


def main() -> None:
    x0 = np.array([-1.0, 1.0])
    print("Rosenbrock comparison from x_0 = (-1, 1), target f < 1e-4")
    print()
    print(f"{'method':>20}  {'eta':>10}  {'iters':>8}  {'final f':>14}")
    for eta in (1e-3, 3e-3):
        k, fv = gd(x0, eta)
        print(f"{'gd':>20}  {eta:>10.4f}  {k:>8d}  {fv:>14.4e}")
    for eta in (1e-3, 3e-3):
        k, fv = gd_momentum(x0, eta)
        print(f"{'gd + momentum 0.9':>20}  {eta:>10.4f}  {k:>8d}  {fv:>14.4e}")
    for eta in (1e-2, 3e-2):
        k, fv = adam(x0, eta)
        print(f"{'adam':>20}  {eta:>10.4f}  {k:>8d}  {fv:>14.4e}")


if __name__ == "__main__":
    main()
