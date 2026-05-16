# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Fit the Steinhart-Hart equation to a synthetic calibration table
and compare against the beta-parameter approximation.

Steinhart-Hart:
  1/T = A + B ln(R) + C [ln(R)]^3

The fit is linear in (A, B, C) given log resistance and 1/T, so the
ordinary least-squares solution closes in one np.linalg.lstsq call.

Companion to Simulation exercise 3.
"""

from __future__ import annotations

import numpy as np

# Synthetic "true" thermistor (beta model) plus a small higher-order
# perturbation so the Steinhart-Hart fit has something to do.
R_0 = 10_000.0
T_0_K = 298.15
BETA = 3950.0
RNG = np.random.default_rng(seed=7)


def r_true(t_c: np.ndarray) -> np.ndarray:
    t_k = t_c + 273.15
    # Pure beta model plus a small quadratic-in-1/T perturbation
    base = R_0 * np.exp(BETA * (1.0 / t_k - 1.0 / T_0_K))
    perturb = 1.0 + 0.005 * (1.0 / t_k - 1.0 / T_0_K) * 1000.0
    return base * perturb


def t_from_r_beta(r: np.ndarray) -> np.ndarray:
    t_k = 1.0 / (1.0 / T_0_K + np.log(r / R_0) / BETA)
    return t_k - 273.15


def fit_steinhart_hart(r: np.ndarray, t_c: np.ndarray) -> tuple[float, float, float]:
    """Linear least squares for the (A, B, C) coefficients."""
    t_k = t_c + 273.15
    lr = np.log(r)
    a_matrix = np.column_stack([np.ones_like(lr), lr, lr ** 3])
    b_vector = 1.0 / t_k
    coeffs, *_ = np.linalg.lstsq(a_matrix, b_vector, rcond=None)
    return float(coeffs[0]), float(coeffs[1]), float(coeffs[2])


def t_from_r_sh(r: np.ndarray, a: float, b: float, c: float) -> np.ndarray:
    lr = np.log(r)
    inv_t_k = a + b * lr + c * lr ** 3
    return 1.0 / inv_t_k - 273.15


def main() -> None:
    # Calibration points: a sparse set with measurement noise on R
    t_cal = np.array([0.0, 10.0, 25.0, 40.0, 55.0, 70.0])
    r_cal_clean = r_true(t_cal)
    # 0.3% multiplicative noise on R, plus 0.05 C reference noise on T
    r_cal = r_cal_clean * (1.0 + 0.003 * RNG.standard_normal(t_cal.size))
    t_cal_noisy = t_cal + 0.05 * RNG.standard_normal(t_cal.size)

    a, b, c = fit_steinhart_hart(r_cal, t_cal_noisy)
    print(f"fitted Steinhart-Hart: A = {a:.6e}, B = {b:.6e}, C = {c:.6e}")

    # Evaluate residuals on the calibration grid
    t_dense = np.arange(0.0, 80.5, 1.0)
    r_dense = r_true(t_dense)
    t_sh = t_from_r_sh(r_dense, a, b, c)
    t_beta = t_from_r_beta(r_dense)
    print()
    print(f"{'T_true (C)':>10}  {'T_SH (C)':>10}  {'T_beta (C)':>11}  "
          f"{'SH err':>8}  {'beta err':>10}")
    for ti, ts, tb in zip(t_dense[::10], t_sh[::10], t_beta[::10]):
        print(f"{ti:>10.1f}  {ts:>10.3f}  {tb:>11.3f}  "
              f"{ts - ti:>8.3f}  {tb - ti:>10.3f}")
    print()
    max_sh = float(np.max(np.abs(t_sh - t_dense)))
    max_beta = float(np.max(np.abs(t_beta - t_dense)))
    print(f"max |T_SH - T_true|   = {max_sh:.3f} C")
    print(f"max |T_beta - T_true| = {max_beta:.3f} C")


if __name__ == "__main__":
    main()
