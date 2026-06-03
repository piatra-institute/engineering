# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26", "scipy>=1.11"]
# ///
"""Fit Mooney-Rivlin and Ogden hyperelastic models to uniaxial data.

For an incompressible isotropic hyperelastic material under uniaxial
extension with stretch lambda, the engineering (1st-Piola) stress is:

  Mooney-Rivlin:
      sigma_eng(lambda) = 2 (lambda - lambda^(-2)) (C10 + C01 / lambda)

  Ogden (N=1):
      sigma_eng(lambda) = (mu / alpha) * (lambda^(alpha-1) - lambda^(-1 - alpha/2))

(For a one-term Ogden the alpha = 2 case reduces to neo-Hookean.)

This script fits both models to a synthetic data set representing a
soft-tissue uniaxial test (skin or arterial wall) and reports the
fitted parameters, RMS residual, and a small extrapolation table.

References:
  - Mooney (1940). J. Appl. Phys. 11, 582--592.
  - Rivlin (1948). Phil. Trans. R. Soc. A 241, 379--397.
  - Ogden (1972). Proc. R. Soc. A 326, 565--584.
  - Holzapfel (2000). Nonlinear solid mechanics, chapter 6.

Run: uv run mooney_rivlin_fit.py
"""
from __future__ import annotations
import numpy as np
from scipy.optimize import curve_fit


def mooney_rivlin_uniaxial(lam: np.ndarray, C10: float, C01: float) -> np.ndarray:
    return 2.0 * (lam - lam ** (-2)) * (C10 + C01 / lam)


def ogden_one_term_uniaxial(lam: np.ndarray, mu: float, alpha: float) -> np.ndarray:
    return (mu / alpha) * (lam ** (alpha - 1.0) - lam ** (-1.0 - alpha / 2.0))


def synth_data(seed: int = 0, n: int = 30) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    lam = np.linspace(1.01, 1.55, n)
    # Truth: Ogden alpha = 6, mu = 0.08 MPa, a stiff strain-stiffening tissue
    sigma_true = ogden_one_term_uniaxial(lam, 0.08, 6.0)
    # Multiplicative noise
    sigma = sigma_true * (1.0 + 0.04 * rng.standard_normal(n))
    return lam, sigma


def main() -> None:
    lam, sigma = synth_data()
    # Mooney-Rivlin fit
    popt_mr, _ = curve_fit(mooney_rivlin_uniaxial, lam, sigma, p0=[0.05, 0.05])
    sigma_mr = mooney_rivlin_uniaxial(lam, *popt_mr)
    rms_mr = float(np.sqrt(np.mean((sigma - sigma_mr) ** 2)))
    # Ogden (one term) fit
    popt_og, _ = curve_fit(ogden_one_term_uniaxial, lam, sigma, p0=[0.05, 4.0],
                           bounds=([1e-5, 1.0], [10.0, 30.0]))
    sigma_og = ogden_one_term_uniaxial(lam, *popt_og)
    rms_og = float(np.sqrt(np.mean((sigma - sigma_og) ** 2)))

    print("=== Mooney-Rivlin fit ===")
    print(f"  C10 = {popt_mr[0]:.4f} MPa, C01 = {popt_mr[1]:.4f} MPa")
    print(f"  RMS residual = {rms_mr:.5f} MPa")
    print("\n=== Ogden (one-term) fit ===")
    print(f"  mu = {popt_og[0]:.4f} MPa, alpha = {popt_og[1]:.3f}")
    print(f"  RMS residual = {rms_og:.5f} MPa")
    print("\n=== Sample comparison (uniaxial) ===")
    print(f"{'lambda':>8} {'sigma_obs (MPa)':>18} {'sigma_MR (MPa)':>17} {'sigma_Og (MPa)':>17}")
    for L, s in zip(lam[::5], sigma[::5]):
        print(f"{L:>8.3f} {s:>18.4f} "
              f"{mooney_rivlin_uniaxial(np.array([L]), *popt_mr)[0]:>17.4f} "
              f"{ogden_one_term_uniaxial(np.array([L]), *popt_og)[0]:>17.4f}")


if __name__ == "__main__":
    main()
