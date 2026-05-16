"""Nonparametric bootstrap for the cooling-cup fit.

Resamples the cooling-cup data with replacement, refits Newton's law on
each resample, accumulates the bootstrap distribution of k_hat, and
reports the 2.5th and 97.5th percentiles as a 95% bootstrap interval.
Compares to the analytical interval from cooling_fit.py.

Dependencies: numpy, scipy.

Run:
    python bootstrap_interval.py
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from scipy import stats

T_INF = 22.0
N_BOOT = 1000
SEED = 0


def load_data(path: Path) -> tuple[np.ndarray, np.ndarray]:
    t_list, T_list = [], []
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            t_list.append(float(row["t_min"]))
            T_list.append(float(row["T_C"]))
    return np.array(t_list), np.array(T_list)


def fit_k(t: np.ndarray, T: np.ndarray, T_inf: float) -> float:
    y = np.log(T - T_inf)
    res = stats.linregress(t, y)
    return -res.slope


def main() -> None:
    here = Path(__file__).parent
    data_path = here.parent / "data" / "cooling_cup.csv"
    t, T = load_data(data_path)

    # Analytical (parametric) interval
    res = stats.linregress(t, np.log(T - T_INF))
    k_hat = -res.slope
    dof = len(t) - 2
    crit = stats.t.ppf(0.975, dof)
    k_lo_analytic = k_hat - crit * res.stderr
    k_hi_analytic = k_hat + crit * res.stderr

    # Bootstrap interval
    rng = np.random.default_rng(SEED)
    n = len(t)
    k_boot = np.empty(N_BOOT)
    for b in range(N_BOOT):
        idx = rng.integers(0, n, size=n)
        try:
            k_boot[b] = fit_k(t[idx], T[idx], T_INF)
        except (ValueError, RuntimeWarning):
            k_boot[b] = np.nan
    k_boot = k_boot[~np.isnan(k_boot)]
    k_lo_boot, k_hi_boot = np.percentile(k_boot, [2.5, 97.5])

    print(f"Cooling-cup k_hat point estimate: {k_hat:.4f} per minute")
    print(f"\nAnalytical 95% CI (delta method, n={n}):")
    print(f"  [{k_lo_analytic:.4f}, {k_hi_analytic:.4f}]")
    print(f"\nBootstrap 95% CI ({N_BOOT} resamples):")
    print(f"  [{k_lo_boot:.4f}, {k_hi_boot:.4f}]")
    print(f"\nRelative widths:")
    print(f"  analytical: {(k_hi_analytic - k_lo_analytic)/k_hat*100:.1f}% of point estimate")
    print(f"  bootstrap:  {(k_hi_boot - k_lo_boot)/k_hat*100:.1f}% of point estimate")
    print("\nFor n=7 the two should agree to within ~10%; large discrepancy indicates")
    print("a non-Gaussian residual structure or a leverage point dominating the fit.")


if __name__ == "__main__":
    main()
