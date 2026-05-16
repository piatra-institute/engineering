"""Identifiability regimes for the logistic model.

Generates three synthetic data sets from the same logistic ground truth
(r=0.7 per hour, K=2.0 cells/mL), differing only in the time window:

  Window A: t in [0, 3]   -- exponential phase only
  Window B: t in [0, 10]  -- spans the inflection
  Window C: t in [8, 15]  -- saturation phase only

For each window, fits (r, K) by nonlinear least squares and reports the
parameter intervals. Demonstrates that the data window selects which
parameters are tightly identified, as in figure 18.4.

Dependencies: numpy, scipy.

Run:
    python identifiability_demo.py
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import curve_fit

R_TRUE = 0.7
K_TRUE = 2.0
N0 = 0.05
SIGMA = 0.05


def logistic(t, r, K):
    return K / (1.0 + (K / N0 - 1.0) * np.exp(-r * t))


def run_window(label: str, t_min: float, t_max: float, n: int = 12, seed: int = 0):
    rng = np.random.default_rng(seed)
    t = np.linspace(t_min, t_max, n)
    N = logistic(t, R_TRUE, K_TRUE) + rng.normal(0, SIGMA, size=n)
    popt, pcov = curve_fit(logistic, t, N, p0=(0.5, max(N) * 1.05),
                           bounds=([0.01, 0.1], [5.0, 10.0]))
    r_hat, K_hat = popt
    r_se, K_se = np.sqrt(np.diag(pcov))
    print(f"\nWindow {label}: t in [{t_min}, {t_max}], n={n}")
    print(f"  r_hat = {r_hat:.3f} +/- {r_se:.3f}    "
          f"(truth {R_TRUE}; relative err {(r_hat - R_TRUE)/R_TRUE*100:+.1f}%)")
    print(f"  K_hat = {K_hat:.3f} +/- {K_se:.3f}    "
          f"(truth {K_TRUE}; relative err {(K_hat - K_TRUE)/K_TRUE*100:+.1f}%)")
    print(f"  rel int width: r {r_se/r_hat*100:.1f}%, K {K_se/K_hat*100:.1f}%")


def main() -> None:
    print("Identifiability vs data window. Ground truth: r=0.7/h, K=2.0.")
    print("Same model, three different observation windows.")
    run_window("A (exponential only)", 0.0, 3.0)
    run_window("B (spans inflection)", 0.0, 10.0)
    run_window("C (saturation only)", 8.0, 15.0)
    print("\nReading: A returns r tightly and K barely; C returns K tightly and r barely;")
    print("B returns both. The data window is part of the experimental design.")


if __name__ == "__main__":
    main()
