# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "scipy"]
# ///
"""Censored Weibull life analysis for Vol II Ch 14, second case study.

Fits a two-parameter Weibull (shape beta, scale eta) to a right-censored
ball-bearing life test by maximum likelihood, then reports the B10 life
with a lower confidence bound by the delta method and a parametric
bootstrap. Reproduces the numbers quoted in the chapter prose.

The likelihood treats a failure at time t as contributing the Weibull
density f(t) and a unit censored at time c as contributing the survival
probability S(c) = exp(-(c/eta)**beta). Dropping the censored units biases
eta low; this script keeps them.

Run:  uv run casestudy_weibull.py
"""

import numpy as np
from scipy.optimize import minimize
from scipy.stats import weibull_min, norm

# Data: eight observed failures, two units censored at the 500 h cutoff.
FAIL = np.array([120.0, 180.0, 226.0, 270.0, 314.0, 358.0, 408.0, 484.0])
CENS = np.array([500.0, 500.0])


def neg_log_likelihood(params, fail, cens):
    """Negative log-likelihood for right-censored Weibull data."""
    log_beta, log_eta = params  # optimise on log scale to keep positivity
    beta, eta = np.exp(log_beta), np.exp(log_eta)
    # Failures contribute the log density; censored units the log survival.
    ll_fail = np.sum(weibull_min.logpdf(fail, beta, scale=eta))
    ll_cens = np.sum(weibull_min.logsf(cens, beta, scale=eta))
    return -(ll_fail + ll_cens)


def fit(fail, cens):
    start = np.log([2.0, 400.0])
    res = minimize(neg_log_likelihood, start, args=(fail, cens), method="BFGS")
    beta, eta = np.exp(res.x)
    return beta, eta, res


def b10_life(beta, eta, p=0.10):
    """Time by which a fraction p of the population has failed."""
    return eta * (-np.log(1.0 - p)) ** (1.0 / beta)


def delta_method_se_b10(beta, eta, cov_be, p=0.10):
    """Delta-method standard error of the B10 life.

    cov_be is the 2x2 covariance of (beta, eta) in natural units.
    """
    c = -np.log(1.0 - p)
    g = eta * c ** (1.0 / beta)
    # Partials of g w.r.t. beta and eta.
    dg_dbeta = -eta * c ** (1.0 / beta) * np.log(c) / beta**2
    dg_deta = c ** (1.0 / beta)
    grad = np.array([dg_dbeta, dg_deta])
    var = grad @ cov_be @ grad
    return float(np.sqrt(var)), float(g)


def parametric_bootstrap_b10(beta, eta, n_fail, n_cens, cutoff, B=5000, seed=0):
    """5th percentile of the B10 estimate over simulated censored datasets."""
    rng = np.random.default_rng(seed)
    n = n_fail + n_cens
    b10s = []
    for _ in range(B):
        t = weibull_min.rvs(beta, scale=eta, size=n, random_state=rng)
        cens_mask = t >= cutoff
        f = t[~cens_mask]
        c = np.full(int(cens_mask.sum()), cutoff)
        if len(f) < 2:  # need at least two failures to fit
            continue
        try:
            bh, eh, _ = fit(f, c)
            b10s.append(b10_life(bh, eh))
        except Exception:
            continue
    b10s = np.array(b10s)
    return float(np.percentile(b10s, 5.0))


def main():
    beta, eta, res = fit(FAIL, CENS)
    print(f"MLE shape  beta = {beta:.3f}")
    print(f"MLE scale  eta  = {eta:.1f} hours")

    # Covariance from the inverse Hessian, transformed from log to natural
    # units by the Jacobian diag(beta, eta).
    cov_log = res.hess_inv
    J = np.diag([beta, eta])
    cov_be = J @ cov_log @ J
    se_beta = np.sqrt(cov_be[0, 0])
    se_eta = np.sqrt(cov_be[1, 1])
    print(f"se(beta) = {se_beta:.2f},  se(eta) = {se_eta:.0f} hours")

    b10 = b10_life(beta, eta)
    se_b10, _ = delta_method_se_b10(beta, eta, cov_be)
    lcb = b10 - norm.ppf(0.95) * se_b10
    print(f"B10 life = {b10:.0f} hours")
    print(f"delta-method se(B10) = {se_b10:.0f} hours")
    print(f"one-sided 95% lower bound (delta) = {lcb:.0f} hours")

    boot_lcb = parametric_bootstrap_b10(beta, eta, len(FAIL), len(CENS), 500.0)
    print(f"parametric-bootstrap 5th pct of B10 = {boot_lcb:.0f} hours")

    naive_mean = FAIL.mean()
    print(f"naive mean of failures only (WRONG) = {naive_mean:.0f} hours")


if __name__ == "__main__":
    main()
