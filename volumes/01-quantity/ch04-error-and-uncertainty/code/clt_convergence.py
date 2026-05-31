"""CLT convergence demonstration for Vol I Ch 4 §4.4.

Draws N = 1e5 samples of size n from four parent distributions
(uniform, exponential, log-normal, Cauchy) at n = 1, 3, 10, 30 and
plots the empirical sample-mean distribution against the Gaussian
limit.
"""
from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

RNG = np.random.default_rng(seed=20260531)
N = 100_000


def draw(parent: str, n: int) -> np.ndarray:
    if parent == "uniform":
        return RNG.uniform(0, 1, size=(N, n)).mean(axis=1)
    if parent == "exponential":
        return RNG.exponential(scale=1.0, size=(N, n)).mean(axis=1)
    if parent == "lognormal":
        return RNG.lognormal(mean=0.0, sigma=0.5, size=(N, n)).mean(axis=1)
    if parent == "cauchy":
        return stats.cauchy.rvs(size=(N, n), random_state=RNG).mean(axis=1)
    raise ValueError(parent)


def kolmogorov_smirnov(sample_means: np.ndarray) -> float:
    mu, sigma = sample_means.mean(), sample_means.std(ddof=1)
    z = (sample_means - mu) / sigma
    ks, _ = stats.kstest(z, "norm")
    return float(ks)


if __name__ == "__main__":
    parents = ["uniform", "exponential", "lognormal", "cauchy"]
    ns = [1, 3, 10, 30]
    for p in parents:
        for n in ns:
            xbars = draw(p, n)
            sk = float(stats.skew(xbars))
            ks = kolmogorov_smirnov(xbars)
            print(f"{p:>11}  n={n:3d}  skew={sk:+.3f}  KS={ks:.4f}")
