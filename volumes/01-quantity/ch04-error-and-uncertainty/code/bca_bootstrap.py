"""Bias-corrected and accelerated (BCa) bootstrap confidence interval.

Worked example from Vol I Ch 4.6: a sensor calibration slope where
the residuals are visibly non-Gaussian. The BCa interval corrects
both for median bias of the bootstrap distribution and for
skewness in its tails, following Efron (1987).

Reference: Efron, B. (1987). Better bootstrap confidence intervals.
JASA 82(397), 171-185. DOI: 10.1080/01621459.1987.10478410.

Run with: python bca_bootstrap.py
"""

import numpy as np
from scipy import stats


def jackknife_acceleration(theta_fn, data):
    """Return the acceleration constant a-hat from the jackknife."""
    n = len(data)
    theta_jack = np.empty(n)
    for i in range(n):
        leave_one_out = np.delete(data, i, axis=0)
        theta_jack[i] = theta_fn(leave_one_out)
    theta_bar = theta_jack.mean()
    num = np.sum((theta_bar - theta_jack) ** 3)
    den = 6.0 * (np.sum((theta_bar - theta_jack) ** 2)) ** 1.5
    return num / den if den != 0 else 0.0


def bca_interval(theta_fn, data, n_boot=10_000, alpha=0.05, seed=12345):
    """Return the (1-alpha) BCa bootstrap confidence interval."""
    rng = np.random.default_rng(seed)
    n = len(data)
    theta_hat = theta_fn(data)
    boot_thetas = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.integers(0, n, size=n)
        boot_thetas[b] = theta_fn(data[idx])
    # bias-correction z0
    prop_less = np.mean(boot_thetas < theta_hat)
    z0 = stats.norm.ppf(prop_less)
    # acceleration a-hat
    a_hat = jackknife_acceleration(theta_fn, data)
    # adjusted quantiles
    z_alpha = stats.norm.ppf(alpha / 2.0)
    z_one_minus = stats.norm.ppf(1.0 - alpha / 2.0)
    alpha_low = stats.norm.cdf(
        z0 + (z0 + z_alpha) / (1.0 - a_hat * (z0 + z_alpha))
    )
    alpha_high = stats.norm.cdf(
        z0 + (z0 + z_one_minus) / (1.0 - a_hat * (z0 + z_one_minus))
    )
    lo = np.quantile(boot_thetas, alpha_low)
    hi = np.quantile(boot_thetas, alpha_high)
    return theta_hat, (lo, hi), (z0, a_hat)


def slope_estimator(xy):
    """Least-squares slope for a 2-column (x, y) array."""
    x = xy[:, 0]
    y = xy[:, 1]
    xbar = x.mean()
    ybar = y.mean()
    num = np.sum((x - xbar) * (y - ybar))
    den = np.sum((x - xbar) ** 2)
    return num / den


def demo():
    """Sensor with residuals from a skewed (chi-square minus mean) law."""
    rng = np.random.default_rng(2026)
    n = 30
    x = np.linspace(290.0, 310.0, n)  # kelvin
    true_slope = 5.10  # mV/K
    intercept = 0.50  # mV
    residual = rng.chisquare(df=2, size=n) - 2.0  # skewed, mean 0
    residual *= 0.05  # scale to mV
    y = intercept + true_slope * x + residual
    data = np.column_stack([x, y])

    theta_hat, (lo, hi), (z0, a_hat) = bca_interval(
        slope_estimator, data, n_boot=20_000
    )
    print(f"slope_hat = {theta_hat:.4f} mV/K")
    print(f"95% BCa CI = ({lo:.4f}, {hi:.4f}) mV/K")
    print(f"z0 = {z0:.4f}, a_hat = {a_hat:.4f}")

    # naive percentile interval for comparison
    boot_p = np.empty(20_000)
    n_data = len(data)
    rng2 = np.random.default_rng(99)
    for b in range(20_000):
        idx = rng2.integers(0, n_data, size=n_data)
        boot_p[b] = slope_estimator(data[idx])
    lo_p = np.quantile(boot_p, 0.025)
    hi_p = np.quantile(boot_p, 0.975)
    print(f"95% percentile CI = ({lo_p:.4f}, {hi_p:.4f}) mV/K")


if __name__ == "__main__":
    demo()
