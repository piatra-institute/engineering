# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Markowitz mean-variance portfolio over a grid of risk-aversion values.

Solves, for each gamma > 0,

    min_w  -mu^T w + gamma * w^T Sigma w
    subject to  1^T w = 1

in closed form via the Lagrange apparatus of Volume II Chapter 11, and
also (when allow_short=False is requested) by a simple projected-gradient
loop that enforces w >= 0 to illustrate the inequality-constrained case.

The three-asset instance matches the worked example in the chapter text:
asset 1 is low-return/low-variance, asset 3 is high-return/high-variance.
Prints, for each gamma, the optimal weights, the expected return, and the
portfolio standard deviation, which together trace the efficient frontier.
"""

from __future__ import annotations

import numpy as np

MU = np.array([0.10, 0.12, 0.15])
SIGMA = np.array(
    [
        [0.040, 0.006, 0.000],
        [0.006, 0.090, 0.010],
        [0.000, 0.010, 0.160],
    ]
)


def closed_form(mu: np.ndarray, sigma: np.ndarray, gamma: float) -> np.ndarray:
    """Equality-only (short sales allowed) optimum, two-fund form."""
    sinv = np.linalg.inv(sigma)
    ones = np.ones(len(mu))
    nu = (ones @ sinv @ mu - 2.0 * gamma) / (ones @ sinv @ ones)
    return (sinv @ (mu - nu * ones)) / (2.0 * gamma)


def long_only(mu: np.ndarray, sigma: np.ndarray, gamma: float,
              steps: int = 20000, lr: float = 0.05) -> np.ndarray:
    """No-short-selling optimum by projected gradient onto the simplex."""
    w = np.ones(len(mu)) / len(mu)
    for _ in range(steps):
        grad = -mu + 2.0 * gamma * sigma @ w
        w = project_simplex(w - lr * grad)
    return w


def project_simplex(v: np.ndarray) -> np.ndarray:
    """Euclidean projection of v onto {w >= 0, 1^T w = 1}."""
    u = np.sort(v)[::-1]
    css = np.cumsum(u) - 1.0
    rho = np.nonzero(u - css / (np.arange(len(v)) + 1) > 0)[0][-1]
    theta = css[rho] / (rho + 1.0)
    return np.maximum(v - theta, 0.0)


def report(label: str, w: np.ndarray) -> None:
    ret = float(MU @ w)
    risk = float(np.sqrt(w @ SIGMA @ w))
    weights = ", ".join(f"{x:+.3f}" for x in w)
    print(f"  {label:>16}: w = [{weights}]  return={ret:.4f}  risk={risk:.4f}")


def main() -> None:
    print("Markowitz efficient frontier (three-asset instance)")
    print()
    for gamma in (0.1, 1.0, 5.0, 10.0):
        print(f"gamma = {gamma}")
        report("short allowed", closed_form(MU, SIGMA, gamma))
        report("long only", long_only(MU, SIGMA, gamma))
        print()


if __name__ == "__main__":
    main()
