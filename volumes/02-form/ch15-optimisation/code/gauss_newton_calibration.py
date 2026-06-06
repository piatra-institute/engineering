# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Gauss-Newton and Levenberg-Marquardt calibration of a decay model.

Fits the three-parameter exponential-decay model

    yhat(t; theta) = A * exp(-k t) + C,   theta = (A, k, C)

to noisy measurements by nonlinear least squares,

    min_theta  (1/2) sum_i r_i(theta)^2,   r_i = y_i - yhat(t_i; theta).

Three solvers are implemented from scratch on the same residual and
Jacobian, so the chapter's worked numbers can be reproduced and the
convergence contrast (Gauss-Newton and Levenberg-Marquardt near-
quadratic, gradient descent geometric) can be seen directly:

  * gauss_newton:  step  -(J^T J)^{-1} J^T r
  * levenberg_marquardt:  step  -(J^T J + mu I)^{-1} J^T r, mu adapted
  * gradient_descent:  step  -eta J^T r

The Gauss-Newton approximation drops the residual-weighted second-
derivative term of the true Hessian, which is small when the residuals
are small at the optimum (the small-residual regime), and that is why
Gauss-Newton inherits the fast tail of a second-order method without
ever forming a second derivative of the model.
"""

from __future__ import annotations

import numpy as np


def model(t: np.ndarray, theta: np.ndarray) -> np.ndarray:
    A, k, C = theta
    return A * np.exp(-k * t) + C


def residual(t: np.ndarray, y: np.ndarray, theta: np.ndarray) -> np.ndarray:
    return y - model(t, theta)


def jacobian(t: np.ndarray, theta: np.ndarray) -> np.ndarray:
    """Jacobian of the residual r_i = y_i - yhat(t_i) w.r.t. theta.

    d r / d A = -exp(-k t),  d r / d k = A t exp(-k t),  d r / d C = -1.
    """
    A, k, _C = theta
    e = np.exp(-k * t)
    JA = -e
    Jk = A * t * e
    JC = -np.ones_like(t)
    return np.column_stack([JA, Jk, JC])


def gauss_newton(t, y, theta0, iters=20):
    theta = np.array(theta0, dtype=float)
    hist = []
    for _ in range(iters):
        r = residual(t, y, theta)
        hist.append(np.linalg.norm(r))
        J = jacobian(t, theta)
        # Linearised subproblem min_p ||J p + r||^2, solved by lstsq for
        # numerical robustness; equivalent to the normal equations
        # (J^T J) p = -J^T r when J has full column rank.
        step, *_ = np.linalg.lstsq(J, -r, rcond=None)
        theta = theta + step
    hist.append(np.linalg.norm(residual(t, y, theta)))
    return theta, np.array(hist)


def levenberg_marquardt(t, y, theta0, iters=20, mu=1e-2):
    theta = np.array(theta0, dtype=float)
    hist = [np.linalg.norm(residual(t, y, theta))]
    for _ in range(iters):
        r = residual(t, y, theta)
        J = jacobian(t, theta)
        H = J.T @ J
        g = J.T @ r
        step = np.linalg.solve(H + mu * np.eye(len(theta)), -g)
        trial = theta + step
        if np.linalg.norm(residual(t, y, trial)) < np.linalg.norm(r):
            theta = trial          # accept: shrink damping toward Gauss-Newton
            mu = max(mu / 3.0, 1e-9)
        else:
            mu = mu * 3.0          # reject: grow damping toward gradient step
        hist.append(np.linalg.norm(residual(t, y, theta)))
    return theta, np.array(hist)


def gradient_descent(t, y, theta0, iters=2000, eta=1e-3):
    theta = np.array(theta0, dtype=float)
    hist = [np.linalg.norm(residual(t, y, theta))]
    for _ in range(iters):
        r = residual(t, y, theta)
        J = jacobian(t, theta)
        theta = theta - eta * (J.T @ r)
        hist.append(np.linalg.norm(residual(t, y, theta)))
    return theta, np.array(hist)


def main() -> None:
    rng = np.random.default_rng(0)
    t = np.linspace(0.0, 5.0, 30)
    theta_true = np.array([2.6, 0.55, 0.40])
    y = model(t, theta_true) + rng.normal(0.0, 0.05, size=t.shape)

    theta0 = np.array([2.0, 0.3, 0.5])      # reasonable start
    theta0_poor = np.array([1.0, 0.1, 0.0])  # poor start: trips pure GN

    th_gn, h_gn = gauss_newton(t, y, theta0)
    th_lm, h_lm = levenberg_marquardt(t, y, theta0_poor)
    th_gd, h_gd = gradient_descent(t, y, theta0)

    # Condition number of the Gauss-Newton Hessian at the optimum.
    J = jacobian(t, th_lm)
    kappa = np.linalg.cond(J.T @ J)

    print("true    theta:", theta_true)
    print("GN  fit theta:", th_gn, "iters to 1e-6:", int(np.argmax(h_gn < 1e-6 * h_gn[0]) or len(h_gn)))
    print("LM  fit theta:", th_lm)
    print("GD  fit theta:", th_gd, "final residual:", h_gd[-1])
    print("cond(J^T J) at optimum:", f"{kappa:.3e}")
    print("GN residual history:", np.round(h_gn, 6))
    print("LM residual history:", np.round(h_lm, 6))


if __name__ == "__main__":
    main()
