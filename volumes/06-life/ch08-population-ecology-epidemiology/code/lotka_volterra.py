# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numpy",
#     "scipy",
#     "matplotlib",
# ]
# ///
"""Lotka-Volterra and Rosenzweig-MacArthur predator-prey integration.

Vol VI Ch 8 §8.2.

Reproduces:
  * Classical Lotka-Volterra orbits (neutral stability, closed curves).
  * Rosenzweig-MacArthur with logistic prey and Holling type II response.
  * Paradox-of-enrichment sweep: as K_N rises past a critical value,
    the stable equilibrium loses stability via a Hopf bifurcation and
    a stable limit cycle emerges.

Usage:
  uv run lotka_volterra.py
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def lotka_volterra(t, y, alpha, beta, delta, gamma):
    """Classical Lotka-Volterra.

    dN/dt = alpha N - beta N P
    dP/dt = delta N P - gamma P
    """
    N, P = y
    return [alpha * N - beta * N * P, delta * N * P - gamma * P]


def rosenzweig_macarthur(t, y, r, K_N, beta, h, delta, gamma):
    """Rosenzweig-MacArthur: logistic prey + Holling type II response."""
    N, P = y
    prey = r * N * (1 - N / K_N) - beta * N * P / (N + h)
    pred = delta * N * P / (N + h) - gamma * P
    return [prey, pred]


def simulate_lv(t_max=50.0, dt=0.05):
    """Three Lotka-Volterra orbits at different initial conditions."""
    params = dict(alpha=1.0, beta=0.01, delta=0.005, gamma=0.5)
    t_span = (0, t_max)
    t_eval = np.arange(0, t_max, dt)
    fig, ax = plt.subplots(figsize=(7, 7))
    for N0, P0 in [(120, 100), (150, 80), (180, 60)]:
        sol = solve_ivp(
            lotka_volterra, t_span, [N0, P0],
            args=tuple(params.values()), t_eval=t_eval,
            rtol=1e-8, atol=1e-10,
        )
        ax.plot(sol.y[0], sol.y[1], label=f"start ({N0}, {P0})")
    ax.plot(100, 100, "*", color="red", markersize=12, label="equilibrium")
    ax.set_xlabel("prey N")
    ax.set_ylabel("predator P")
    ax.set_title("Lotka-Volterra phase portrait (neutral centre)")
    ax.legend()
    fig.tight_layout()
    fig.savefig("lotka_volterra_orbits.png", dpi=150)
    plt.close(fig)


def hopf_sweep():
    """Sweep K_N in Rosenzweig-MacArthur; find approximate bifurcation."""
    r, beta, h, delta, gamma = 1.0, 0.5, 0.5, 0.4, 0.2
    K_crit = h * (delta + gamma) / (delta - gamma)
    print(f"Theoretical K_crit = h (delta + gamma) / (delta - gamma) = {K_crit:.3f}")
    t_eval = np.linspace(0, 200, 4000)
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    for ax, K_N in zip(axes.ravel(), [0.8, 1.2, 1.8, 3.0]):
        sol = solve_ivp(
            rosenzweig_macarthur, (0, 200), [0.5, 0.3],
            args=(r, K_N, beta, h, delta, gamma),
            t_eval=t_eval, rtol=1e-8, atol=1e-10,
        )
        ax.plot(sol.t, sol.y[0], label="prey N")
        ax.plot(sol.t, sol.y[1], label="predator P")
        ax.set_title(f"K_N = {K_N}")
        ax.set_xlabel("time")
        ax.set_ylabel("density")
        ax.legend(fontsize=8)
    fig.suptitle("Rosenzweig-MacArthur: Hopf bifurcation sweep over K_N")
    fig.tight_layout()
    fig.savefig("rm_hopf_sweep.png", dpi=150)
    plt.close(fig)


def main():
    simulate_lv()
    hopf_sweep()


if __name__ == "__main__":
    main()
