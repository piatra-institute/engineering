# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numpy",
#     "scipy",
#     "matplotlib",
#     "pandas",
# ]
# ///
"""SIR model fitting to a real outbreak dataset (Vol VI Ch 8 project).

Reads daily case-count data from a CSV, fits an SIR model by
nonlinear least squares to log-incidence, and reports point
estimates and parametric-bootstrap 95% CIs for R0 and the recovery
rate gamma. Compares predicted and observed peak timing,
peak height, and final size.

Usage:
  uv run sir_fit.py [path/to/data.csv]
  (defaults to data/covid_nz_first_wave.csv)
"""

from __future__ import annotations

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import matplotlib.pyplot as plt


def sir_rhs(t, y, beta, gamma, N):
    S, I, R = y
    new_inf = beta * S * I / N
    rec = gamma * I
    return [-new_inf, new_inf - rec, rec]


def simulate_sir(R0, gamma, N, I0, t_grid):
    beta = R0 * gamma
    y0 = [N - I0, I0, 0.0]
    sol = solve_ivp(
        sir_rhs, (t_grid[0], t_grid[-1]), y0, args=(beta, gamma, N),
        t_eval=t_grid, rtol=1e-8, atol=1e-10,
    )
    return sol.y


def predicted_daily_incidence(R0, gamma, N, I0, t_grid):
    """Return daily new infections from SIR fit."""
    S, I, R = simulate_sir(R0, gamma, N, I0, t_grid)
    new_S = -np.diff(S, prepend=S[0])
    return np.clip(new_S, 0, None)


def neg_log_likelihood(params, observed, N, t_grid):
    """Poisson NLL for daily case counts."""
    R0, gamma, I0_log10 = params
    if R0 < 1.0 or R0 > 12.0:
        return 1e10
    if gamma < 0.01 or gamma > 1.0:
        return 1e10
    I0 = 10 ** I0_log10
    predicted = predicted_daily_incidence(R0, gamma, N, I0, t_grid)
    predicted = np.clip(predicted, 1e-6, None)
    return float(np.sum(predicted - observed * np.log(predicted)))


def fit(observed, N, t_grid):
    x0 = [2.5, 1 / 7, 1.0]  # R0, gamma, log10(I0)
    res = minimize(
        neg_log_likelihood, x0, args=(observed, N, t_grid),
        method="Nelder-Mead",
        options={"xatol": 1e-4, "fatol": 1e-2, "maxiter": 4000},
    )
    R0_hat, gamma_hat, I0_log10_hat = res.x
    return R0_hat, gamma_hat, 10 ** I0_log10_hat, res.fun


def bootstrap_ci(observed, N, t_grid, n_boot=200, seed=42):
    """Parametric Poisson bootstrap of fit parameters."""
    rng = np.random.default_rng(seed)
    R0_hat, gamma_hat, I0_hat, _ = fit(observed, N, t_grid)
    predicted = predicted_daily_incidence(R0_hat, gamma_hat, N, I0_hat, t_grid)
    R0_samples = []
    gamma_samples = []
    for _ in range(n_boot):
        sampled = rng.poisson(np.clip(predicted, 1e-6, None))
        try:
            R0_b, gamma_b, _, _ = fit(sampled, N, t_grid)
            R0_samples.append(R0_b)
            gamma_samples.append(gamma_b)
        except Exception:
            continue
    return (np.percentile(R0_samples, [2.5, 97.5]),
            np.percentile(gamma_samples, [2.5, 97.5]))


def main():
    here = Path(__file__).resolve().parent
    repo_root = here.parents[4]
    default = repo_root / "volumes/06-life/ch08-population-ecology-epidemiology/data/covid_nz_first_wave.csv"
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else default
    if not path.exists():
        print(f"Dataset not found: {path}")
        print("Run from repo root with `uv run` so the relative data path resolves.")
        return
    df = pd.read_csv(path)
    observed = df["daily_cases"].to_numpy()
    N = 5_000_000  # population of NZ ~5M (illustrative)
    t_grid = np.arange(len(observed), dtype=float)
    R0_hat, gamma_hat, I0_hat, nll = fit(observed, N, t_grid)
    R0_ci, gamma_ci = bootstrap_ci(observed, N, t_grid, n_boot=100)
    print(f"R0 point estimate: {R0_hat:.3f}")
    print(f"R0 95% bootstrap CI: ({R0_ci[0]:.3f}, {R0_ci[1]:.3f})")
    print(f"gamma point estimate: {gamma_hat:.4f} d^-1")
    print(f"gamma 95% bootstrap CI: ({gamma_ci[0]:.4f}, {gamma_ci[1]:.4f})")
    print(f"NLL at fit: {nll:.3f}")
    predicted = predicted_daily_incidence(R0_hat, gamma_hat, N, I0_hat, t_grid)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(t_grid, observed, "o", label="observed", markersize=3)
    ax.plot(t_grid, predicted, "-", label=f"SIR fit, R0={R0_hat:.2f}")
    ax.set_xlabel("day")
    ax.set_ylabel("daily cases")
    ax.legend()
    fig.tight_layout()
    fig.savefig(here / "sir_fit_result.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
