# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Monte Carlo propagation for an optical-aberration uncertainty budget
with correlated Zernike coefficients.

An optical wavefront error in mirror or lens metrology is commonly
decomposed into Zernike polynomial coefficients (radial orders n,
azimuthal frequency m): defocus, astigmatism, coma, spherical, etc.
The measured coefficients carry correlated uncertainty because the
fitting procedure projects a noisy measured wavefront onto the
Zernike basis, and the orthogonality of the Zernike basis on the
unit aperture is broken at the measurement boundary by a non-circular
aperture mask or by missing-data infill.

This script propagates a representative 4-coefficient budget
(defocus, astigmatism 0/90, coma X, spherical) with a covariance
matrix that includes a +0.45 correlation between defocus and
spherical (the dominant fitting-correlation in many practical
budgets) and zero correlations elsewhere. The output is the RMS
wavefront error.

Run:    uv run zernike_mc.py

The example aligns with JCGM 102:2011 multivariate Monte Carlo;
the Cholesky factorisation of the covariance matrix realises the
correlation structure.
"""

import numpy as np


RNG = np.random.default_rng(827)
N = 100_000

# Mean Zernike coefficients in waves at 632.8 nm.
COEFFS = np.array([0.020, 0.015, 0.012, 0.008])
LABELS = ["defocus Z4", "astig 0/90 Z5", "coma X Z7", "spherical Z11"]

# Per-coefficient standard uncertainties (waves), Type B from the
# interferometer calibration certificate.
SIGMA = np.array([0.005, 0.004, 0.003, 0.004])

# Correlation matrix. Defocus-spherical correlation = +0.45 (the
# fitting cross-talk between Z4 and Z11 in a non-circular-aperture
# measurement); other off-diagonals = 0.
CORR = np.array([
    [1.0,   0.0,  0.0,  0.45],
    [0.0,   1.0,  0.0,  0.0 ],
    [0.0,   0.0,  1.0,  0.0 ],
    [0.45,  0.0,  0.0,  1.0 ],
])
COV = np.outer(SIGMA, SIGMA) * CORR


def rms_wavefront(z):
    """RMS wavefront error in waves: sqrt(sum of squared Zernike coeffs)
    in the absence of cross-coupling (the orthogonality identity).
    """
    return np.sqrt((z ** 2).sum(axis=-1))


def main() -> None:
    print("--- Zernike uncertainty budget ---")
    for name, c, s in zip(LABELS, COEFFS, SIGMA):
        print(f"  {name:20s}: {c:.4f} +/- {s:.4f} waves")
    print(f"  correlation Z4 <-> Z11: {CORR[0, 3]:+.2f}")
    print()

    # Cholesky factorise the covariance.
    L = np.linalg.cholesky(COV)
    # Draw uncorrelated standard normals.
    z_indep = RNG.normal(size=(N, 4))
    # Transform to correlated draws.
    z_corr = COEFFS + z_indep @ L.T

    rms = rms_wavefront(z_corr)
    rms_mean = rms.mean()
    rms_std = rms.std(ddof=1)
    rms_lo = np.quantile(rms, 0.025)
    rms_hi = np.quantile(rms, 0.975)
    print(f"empirical RMS WFE mean   : {rms_mean:.5f} waves")
    print(f"empirical RMS WFE std    : {rms_std:.5f} waves")
    print(f"95% coverage interval    : [{rms_lo:.5f}, {rms_hi:.5f}] waves")

    # Compare against the linear independence assumption: ignore the
    # Z4-Z11 correlation.
    z_naive = COEFFS + RNG.normal(size=(N, 4)) * SIGMA
    rms_naive = rms_wavefront(z_naive)
    print()
    print(f"naive (uncorrelated) std : {rms_naive.std(ddof=1):.5f} waves")
    print(f"correlation inflates std : "
          f"{(rms_std / rms_naive.std(ddof=1) - 1) * 100:.1f}%")


if __name__ == "__main__":
    main()
