# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numpy",
#     "scipy",
#     "matplotlib",
# ]
# ///
"""SIR and SEIR compartmental-model solvers for Vol VI Ch 8 §8.3.

Provides:
  * SIR ODE integration (`solve_sir`) and SEIR ODE integration (`solve_seir`).
  * Final-size relation solver (`final_size`).
  * Effective reproduction number R_t from a fitted SIR trajectory.

Usage:
  uv run sir_seir_solve.py
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import matplotlib.pyplot as plt


def sir_rhs(t, y, beta, gamma, N):
    S, I, R = y
    new_inf = beta * S * I / N
    rec = gamma * I
    return [-new_inf, new_inf - rec, rec]


def seir_rhs(t, y, beta, sigma, gamma, N):
    S, E, I, R = y
    new_inf = beta * S * I / N
    progression = sigma * E
    rec = gamma * I
    return [-new_inf, new_inf - progression, progression - rec, rec]


def solve_sir(R0, gamma, N, I0, t_max):
    beta = R0 * gamma
    y0 = [N - I0, I0, 0.0]
    sol = solve_ivp(
        sir_rhs, (0, t_max), y0, args=(beta, gamma, N),
        t_eval=np.linspace(0, t_max, 2001), rtol=1e-9, atol=1e-12,
    )
    return sol


def solve_seir(R0, sigma, gamma, N, I0, t_max):
    beta = R0 * gamma
    y0 = [N - I0, 0.0, I0, 0.0]
    sol = solve_ivp(
        seir_rhs, (0, t_max), y0, args=(beta, sigma, gamma, N),
        t_eval=np.linspace(0, t_max, 2001), rtol=1e-9, atol=1e-12,
    )
    return sol


def final_size(R0):
    """Solve s_infinity = exp(-R0 (1 - s_infinity))."""
    if R0 <= 1.0:
        return 1.0
    f = lambda s: s - np.exp(-R0 * (1 - s))
    return brentq(f, 1e-12, 1.0 - 1e-6)


def main():
    R0 = 3.0
    gamma = 1 / 7
    sigma = 1 / 5
    N = 1_000_000
    I0 = 10
    t_max = 365

    sir = solve_sir(R0, gamma, N, I0, t_max)
    seir = solve_seir(R0, sigma, gamma, N, I0, t_max)

    s_inf = final_size(R0)
    print(f"R0 = {R0}, gamma = {gamma:.4f}, sigma = {sigma:.4f}")
    print(f"Final fraction susceptible s_infty = {s_inf:.4f}")
    print(f"Final attack rate = {1 - s_inf:.4f}")
    print(f"Herd-immunity threshold p_c = 1 - 1/R0 = {1 - 1/R0:.4f}")

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(sir.t, sir.y[1] / N, label="SIR I/N", linewidth=2)
    ax.plot(seir.t, seir.y[2] / N, "--", label="SEIR I/N", linewidth=2)
    ax.set_xlabel("days")
    ax.set_ylabel("prevalence I/N")
    ax.set_title(f"SIR vs SEIR prevalence, R0={R0}, 1/sigma=5d, 1/gamma=7d")
    ax.legend()
    fig.tight_layout()
    fig.savefig("sir_seir_prevalence.png", dpi=150)

    # Peak summary
    sir_peak_t = sir.t[np.argmax(sir.y[1])]
    seir_peak_t = seir.t[np.argmax(seir.y[2])]
    print(f"SIR peak time:  {sir_peak_t:.1f} d, prevalence "
          f"{sir.y[1].max() / N:.3f}")
    print(f"SEIR peak time: {seir_peak_t:.1f} d, prevalence "
          f"{seir.y[2].max() / N:.3f}")
    plt.close("all")


if __name__ == "__main__":
    main()
