# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26", "scipy>=1.11"]
# ///
"""Fit Monod parameters to specific-growth-rate-versus-substrate data.

Specific growth rate model:

    mu(S) = mu_max * S / (K_S + S)

Fits mu_max and K_S to a set of (S, mu) observations using non-linear
least squares. Reports parameters, residual statistics, and a
parametric covariance estimate. Also runs the chemostat washout check:
given a feed substrate concentration S_f and a candidate dilution rate
D, solves mu(S*) = D for the steady-state substrate concentration and
flags whether the dilution rate exceeds mu_max (washout).

Working numbers (E. coli on glucose, order-of-magnitude):
- mu_max ~ 0.9 h^-1
- K_S ~ 0.05 g/L

Run: uv run monod_growth_fit.py
"""
from __future__ import annotations
import math
import numpy as np
from scipy.optimize import curve_fit


def monod(S: np.ndarray, mu_max: float, K_S: float) -> np.ndarray:
    return mu_max * S / (K_S + S)


def fit_monod(S: np.ndarray, mu: np.ndarray) -> tuple[float, float, np.ndarray]:
    """Return (mu_max, K_S, covariance)."""
    p0 = [max(mu) * 1.05, np.median(S)]
    popt, pcov = curve_fit(monod, S, mu, p0=p0, bounds=(0, np.inf))
    return float(popt[0]), float(popt[1]), pcov


def chemostat_steady_substrate(mu_max: float, K_S: float, D: float) -> float | None:
    """Solve mu(S*) = D for S*. Returns None if D > mu_max (washout)."""
    if D >= mu_max:
        return None
    return K_S * D / (mu_max - D)


def main() -> None:
    # Synthetic data (E. coli on glucose, with realistic scatter)
    rng = np.random.default_rng(20260603)
    S = np.array([0.005, 0.010, 0.025, 0.050, 0.10, 0.25, 0.50, 1.0, 2.0, 5.0])
    mu_true = monod(S, mu_max=0.90, K_S=0.050)
    mu = mu_true + rng.normal(0, 0.02, size=mu_true.shape)
    mu = np.clip(mu, 0.0, None)

    mu_max_hat, K_S_hat, cov = fit_monod(S, mu)
    se = np.sqrt(np.diag(cov))

    print("Monod fit (synthetic data, E. coli on glucose):")
    print(f"  mu_max = {mu_max_hat:.3f} +/- {se[0]:.3f} h^-1")
    print(f"  K_S    = {K_S_hat:.4f} +/- {se[1]:.4f} g/L")
    pred = monod(S, mu_max_hat, K_S_hat)
    resid = mu - pred
    print(f"  RMSE   = {math.sqrt(float(np.mean(resid**2))):.3f} h^-1")
    print(f"  R^2    = {1 - float(np.var(resid))/float(np.var(mu)):.4f}")

    print("\nChemostat steady-state check (mu_max={:.3f}, K_S={:.4f}):"
          .format(mu_max_hat, K_S_hat))
    for D in [0.10, 0.30, 0.60, 0.85, 0.95]:
        S_star = chemostat_steady_substrate(mu_max_hat, K_S_hat, D)
        if S_star is None:
            print(f"  D = {D:.2f} h^-1  -> WASHOUT (D >= mu_max)")
        else:
            print(f"  D = {D:.2f} h^-1  -> S* = {S_star:.4f} g/L")


if __name__ == "__main__":
    main()
