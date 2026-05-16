"""
Linear regression of meter reading against reference, with residual
analysis for calibration drift.

Supports the chapter's discussion of calibration and the Diagnosis
exercise on pipette drift.

Dependencies:
  numpy, scipy

Usage:
  python calibration_check.py
"""

import numpy as np
from scipy import stats


def linear_calibration(reference: np.ndarray, indicated: np.ndarray
                       ) -> dict[str, float]:
    """Fit indicated = a + b * reference. Returns the fitted parameters
    and the residual standard deviation."""
    if reference.shape != indicated.shape:
        raise ValueError("reference and indicated must have the same shape")
    result = stats.linregress(reference, indicated)
    fitted = result.intercept + result.slope * reference
    residuals = indicated - fitted
    residual_std = float(np.std(residuals, ddof=2))  # ddof=2 for fitted a,b
    return {
        "intercept": float(result.intercept),
        "intercept_stderr": float(result.intercept_stderr),
        "slope": float(result.slope),
        "slope_stderr": float(result.stderr),
        "r_squared": float(result.rvalue ** 2),
        "residual_std": residual_std,
    }


def main() -> None:
    # Example: a kitchen scale checked against five coin masses.
    # Reference masses are from data/coin_masses.csv (illustrative
    # values for a representative coin set).
    reference = np.array([2.50, 5.00, 7.50, 10.00, 20.00])  # grams
    indicated = np.array([2.48, 4.95, 7.43, 9.92, 19.85])  # grams

    fit = linear_calibration(reference, indicated)
    print("Linear calibration: indicated = a + b * reference")
    print(f"  intercept a = {fit['intercept']:.4f} g "
          f"(stderr {fit['intercept_stderr']:.4f})")
    print(f"  slope     b = {fit['slope']:.6f} "
          f"(stderr {fit['slope_stderr']:.6f})")
    print(f"  R^2        = {fit['r_squared']:.6f}")
    print(f"  residual std = {fit['residual_std']:.4f} g")
    print()

    # Engineering interpretation.
    slope = fit['slope']
    if abs(slope - 1.0) > 3 * fit['slope_stderr']:
        print(f"  WARNING: slope deviates from 1.0 by more than 3 stderr; "
              f"the scale's reading is biased by {(slope - 1.0) * 100:.2f}%")
    else:
        print(f"  slope is consistent with 1.0 within 3 stderr; the scale "
              f"is unbiased to the precision of this check")


if __name__ == "__main__":
    main()
