# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Nonparametric bootstrap confidence interval for the sample mean.

The example sample is the thirty-day commute series from section 8.1
of chapter 8. The script draws B = 10,000 resamples of size n with
replacement and reports the 2.5th and 97.5th percentiles of the
bootstrap distribution of the sample mean. Compare to the
parametric t-based interval that the chapter computes analytically.
"""

import numpy as np

RNG = np.random.default_rng(2026)
B = 10_000
ALPHA = 0.05

COMMUTE_MIN = np.array([
    27, 28, 29, 26, 32, 30, 27, 28, 29, 28,
    31, 27, 26, 28, 29, 30, 28, 27, 32, 28,
    29, 27, 30, 28, 31, 29, 28, 27, 28, 35,
], dtype=float)


def bootstrap_mean_ci(x: np.ndarray, b: int, alpha: float) -> tuple[float, float, float]:
    n = x.size
    replicates = np.empty(b, dtype=float)
    for i in range(b):
        idx = RNG.integers(0, n, size=n)
        replicates[i] = x[idx].mean()
    lo = np.quantile(replicates, alpha / 2.0)
    hi = np.quantile(replicates, 1.0 - alpha / 2.0)
    return float(replicates.mean()), float(lo), float(hi)


def main() -> None:
    n = COMMUTE_MIN.size
    point = COMMUTE_MIN.mean()
    s = COMMUTE_MIN.std(ddof=1)
    # Parametric t-based 95% CI with n - 1 = 29 dof.
    t_crit = 2.045   # t_{0.975, 29}; cited in the chapter as ~2.05.
    half = t_crit * s / np.sqrt(n)
    boot_mean, boot_lo, boot_hi = bootstrap_mean_ci(COMMUTE_MIN, B, ALPHA)
    print(f"n = {n}, sample mean = {point:.3f} min, sample sd = {s:.3f} min")
    print(f"t-based 95% CI : [{point - half:.3f}, {point + half:.3f}] min")
    print(f"bootstrap 95% CI ({B} replicates): [{boot_lo:.3f}, {boot_hi:.3f}] min")
    print(f"bootstrap mean of replicates    : {boot_mean:.3f} min")


if __name__ == "__main__":
    main()
