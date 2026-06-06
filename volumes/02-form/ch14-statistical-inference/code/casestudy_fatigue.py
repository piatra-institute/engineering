# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "scipy"]
# ///
"""End-to-end fatigue S-N case study for Volume II Chapter 14.

Reads fatigue-sn.csv (stress amplitude in MPa, cycles to failure),
fits the log-log Basquin model log10(N) = b0 + b1 * log10(S) + eps,
checks residual assumptions, and reports a parametric prediction
interval and a residual-bootstrap prediction interval for the life at
a query stress amplitude. Run with:  uv run casestudy_fatigue.py
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from scipy import stats

QUERY_STRESS_MPA = 260.0
N_BOOTSTRAP = 5000
RNG = np.random.default_rng(14)


def load_data() -> tuple[np.ndarray, np.ndarray]:
    path = (Path(__file__).parent.parent / "data" / "fatigue-sn.csv").resolve()
    stress, cycles = [], []
    with open(path, newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            stress.append(float(row["stress_amplitude_MPa"]))
            cycles.append(float(row["cycles_to_failure"]))
    return np.asarray(stress), np.asarray(cycles)


def fit(log_s: np.ndarray, log_n: np.ndarray):
    design = np.column_stack([np.ones_like(log_s), log_s])
    beta, *_ = np.linalg.lstsq(design, log_n, rcond=None)
    resid = log_n - design @ beta
    n = log_s.size
    sigma = float(np.sqrt(resid @ resid / (n - 2)))
    return beta, resid, sigma, design


def main() -> None:
    stress, cycles = load_data()
    log_s, log_n = np.log10(stress), np.log10(cycles)
    beta, resid, sigma, design = fit(log_s, log_n)
    n = log_s.size
    sxx = float(((log_s - log_s.mean()) ** 2).sum())
    r2 = 1.0 - (resid @ resid) / ((log_n - log_n.mean()) ** 2).sum()

    print(f"beta0 = {beta[0]:.3f}, beta1 = {beta[1]:.3f} (Basquin m = {-beta[1]:.3f})")
    print(f"sigma = {sigma:.4f}, Sxx = {sxx:.4f}, R^2 = {r2:.4f}")
    se_slope = sigma / np.sqrt(sxx)
    t_crit = stats.t.ppf(0.975, n - 2)
    print(f"slope 95% CI = [{beta[1] - t_crit * se_slope:.3f}, "
          f"{beta[1] + t_crit * se_slope:.3f}]")

    # Assumption check: Shapiro-Wilk on residuals (a numeric companion to
    # the Q-Q plot). A small p flags non-normal residuals.
    sw_stat, sw_p = stats.shapiro(resid)
    print(f"Shapiro-Wilk on residuals: W = {sw_stat:.3f}, p = {sw_p:.3f}")

    # Parametric prediction interval at the query stress.
    log_sq = np.log10(QUERY_STRESS_MPA)
    yhat = beta[0] + beta[1] * log_sq
    lev = 1.0 + 1.0 / n + (log_sq - log_s.mean()) ** 2 / sxx
    se_pred = sigma * np.sqrt(lev)
    lo, hi = yhat - t_crit * se_pred, yhat + t_crit * se_pred
    print(f"\nquery S = {QUERY_STRESS_MPA} MPa -> log10 N point = {yhat:.3f} "
          f"(N = {10 ** yhat:.3e} cycles)")
    print(f"parametric 95% PI (log scale): [{lo:.3f}, {hi:.3f}]")
    print(f"parametric 95% PI (cycles): [{10 ** lo:.3e}, {10 ** hi:.3e}]")

    # Residual-bootstrap prediction interval. Resample residuals, refit,
    # and draw one fresh residual to mimic a future specimen.
    fitted = design @ beta
    preds = np.empty(N_BOOTSTRAP)
    for b in range(N_BOOTSTRAP):
        boot_y = fitted + RNG.choice(resid, size=n, replace=True)
        boot_beta, *_ = np.linalg.lstsq(design, boot_y, rcond=None)
        new_resid = RNG.choice(resid)
        preds[b] = boot_beta[0] + boot_beta[1] * log_sq + new_resid
    blo, bhi = np.percentile(preds, [2.5, 97.5])
    print(f"\nbootstrap 95% PI (log scale): [{blo:.3f}, {bhi:.3f}]")
    print(f"bootstrap 95% PI (cycles): [{10 ** blo:.3e}, {10 ** bhi:.3e}]")


if __name__ == "__main__":
    main()
