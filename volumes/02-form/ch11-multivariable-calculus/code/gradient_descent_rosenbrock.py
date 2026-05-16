# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "numpy",
# ]
# ///
"""
Gradient descent on the Rosenbrock function f(x, y) = (x - 1)^2 +
b (y - x^2)^2 with b = 10. Supports the Simulation exercise on
gradient descent and the chapter's discussion of why naive
optimisers crawl through curved valleys.

Reports the trajectory length, the final iterate, the final loss,
and an indicator of whether the iterate has reached the global
minimum (x*, y*) = (1, 1) within tolerance.

Usage:
    python gradient_descent_rosenbrock.py
"""

from __future__ import annotations
from dataclasses import dataclass

import numpy as np


def rosenbrock(x: float, y: float, b: float = 10.0) -> float:
    """Rosenbrock objective; minimum value 0 at (1, 1)."""
    return (x - 1.0) ** 2 + b * (y - x * x) ** 2


def rosenbrock_grad(x: float, y: float, b: float = 10.0) -> tuple[float, float]:
    """Closed-form gradient of the Rosenbrock function."""
    dfx = 2.0 * (x - 1.0) - 4.0 * b * x * (y - x * x)
    dfy = 2.0 * b * (y - x * x)
    return dfx, dfy


@dataclass(frozen=True)
class Trajectory:
    iterations: int
    final_xy: tuple[float, float]
    final_loss: float
    grad_norm: float
    reached_minimum: bool


def gradient_descent(
    x0: float,
    y0: float,
    step: float,
    n_iter: int,
    b: float = 10.0,
    tol: float = 1e-3,
) -> Trajectory:
    """Run fixed-step-size gradient descent and report the final state."""
    x, y = x0, y0
    for _ in range(n_iter):
        dfx, dfy = rosenbrock_grad(x, y, b)
        x -= step * dfx
        y -= step * dfy
    dfx, dfy = rosenbrock_grad(x, y, b)
    grad_norm = float(np.hypot(dfx, dfy))
    loss = rosenbrock(x, y, b)
    reached = (abs(x - 1.0) < tol) and (abs(y - 1.0) < tol)
    return Trajectory(n_iter, (x, y), loss, grad_norm, reached)


def main() -> None:
    """Run the Simulation-exercise configuration and report results."""
    config = dict(x0=-1.0, y0=1.0, step=0.001, n_iter=10_000, b=10.0)
    traj = gradient_descent(**config)
    print(f"start         : ({config['x0']:.3f}, {config['y0']:.3f})")
    print(f"step size     : {config['step']}")
    print(f"iterations    : {traj.iterations}")
    print(f"final iterate : ({traj.final_xy[0]:.5f}, {traj.final_xy[1]:.5f})")
    print(f"final loss    : {traj.final_loss:.6e}")
    print(f"||grad||      : {traj.grad_norm:.6e}")
    print(f"at global min : {traj.reached_minimum}")
    # Diagnostic comment for the reader: the iterate after 10000 steps
    # at step 0.001 is well inside the curved valley but has not yet
    # reached (1, 1). The valley's elongation makes the gradient point
    # almost across the valley rather than along it.


if __name__ == "__main__":
    main()
