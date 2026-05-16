# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "numpy>=1.26",
# ]
# ///
"""
Bootstrap demonstration: estimate the sampling distribution of the
sample median by resampling with replacement.

Reproduces the figure in volumes/02-form/ch14-statistical-inference/
figures/fig-bootstrap.tex at numerical level.

Usage:
    uv run bootstrap_demo.py
"""

from __future__ import annotations

import numpy as np


def bootstrap_statistic(
    sample: np.ndarray,
    statistic,
    n_resamples: int = 2000,
    seed: int = 14,
) -> np.ndarray:
    """Return ``n_resamples`` recomputations of ``statistic`` on
    samples drawn with replacement from ``sample``."""
    rng = np.random.default_rng(seed)
    n = len(sample)
    estimates = np.empty(n_resamples)
    for b in range(n_resamples):
        resample = rng.choice(sample, size=n, replace=True)
        estimates[b] = statistic(resample)
    return estimates


def percentile_ci(estimates: np.ndarray, alpha: float = 0.05) -> tuple[float, float]:
    """Return the (alpha/2, 1 - alpha/2) percentile interval."""
    lower = np.quantile(estimates, alpha / 2.0)
    upper = np.quantile(estimates, 1.0 - alpha / 2.0)
    return float(lower), float(upper)


def main() -> None:
    rng = np.random.default_rng(2026)
    # A right-skewed sample where the median is more stable than the mean.
    sample = rng.lognormal(mean=0.0, sigma=0.75, size=80)

    median_estimates = bootstrap_statistic(sample, np.median, n_resamples=5000)
    mean_estimates = bootstrap_statistic(sample, np.mean, n_resamples=5000)

    point_median = float(np.median(sample))
    point_mean = float(np.mean(sample))

    se_median_boot = float(np.std(median_estimates, ddof=1))
    se_mean_boot = float(np.std(mean_estimates, ddof=1))
    se_mean_clt = float(np.std(sample, ddof=1) / np.sqrt(len(sample)))

    lo_med, hi_med = percentile_ci(median_estimates)
    lo_mean, hi_mean = percentile_ci(mean_estimates)

    print(f"n = {len(sample)}, B = {len(median_estimates)}")
    print()
    print(f"Sample median            = {point_median:.4f}")
    print(f"Bootstrap SE (median)    = {se_median_boot:.4f}")
    print(f"95% percentile CI median = [{lo_med:.4f}, {hi_med:.4f}]")
    print()
    print(f"Sample mean              = {point_mean:.4f}")
    print(f"Bootstrap SE (mean)      = {se_mean_boot:.4f}")
    print(f"Classical SE (mean)      = {se_mean_clt:.4f}")
    print(f"95% percentile CI mean   = [{lo_mean:.4f}, {hi_mean:.4f}]")


if __name__ == "__main__":
    main()
