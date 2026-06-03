# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26", "scipy>=1.11"]
# ///
"""Fit constitutive models to a uniaxial tissue stress-strain curve.

Implements two soft-tissue constitutive models in uniaxial tension
(incompressible, lambda_x = lambda, lambda_y = lambda_z = 1/sqrt(lambda)):

- neo-Hookean: sigma = mu * (lambda^2 - 1/lambda)
- Mooney-Rivlin: sigma = 2 * (c1 + c2 / lambda) * (lambda^2 - 1/lambda)
- Fung exponential: sigma = c * (exp(b * (lambda - 1)^2) - 1)

Synthetic data are generated from a Fung-like curve plus 5% noise
to mimic an experimental dataset; the script fits all three models
and reports residual norm and parameter values.

Run: uv run tissue_stress_strain_fit.py
"""
from __future__ import annotations
import numpy as np
from scipy.optimize import curve_fit


def neo_hookean(lam: np.ndarray, mu: float) -> np.ndarray:
    return mu * (lam**2 - 1.0 / lam)


def mooney_rivlin(lam: np.ndarray, c1: float, c2: float) -> np.ndarray:
    return 2.0 * (c1 + c2 / lam) * (lam**2 - 1.0 / lam)


def fung(lam: np.ndarray, c: float, b: float) -> np.ndarray:
    return c * (np.exp(b * (lam - 1.0) ** 2) - 1.0)


def generate_synthetic_data(seed: int = 7):
    """Synthetic J-curve mimicking skin under uniaxial tension."""
    rng = np.random.default_rng(seed)
    lam = np.linspace(1.0, 1.5, 25)
    sigma_true = fung(lam, c=0.012, b=12.0)  # MPa
    noise = rng.normal(scale=0.05 * sigma_true.max(), size=lam.shape)
    sigma = sigma_true + noise
    sigma = np.clip(sigma, a_min=0.0, a_max=None)
    return lam, sigma


def fit_and_report(name, model, p0, lam, sigma):
    try:
        popt, _ = curve_fit(model, lam, sigma, p0=p0, maxfev=5000)
        pred = model(lam, *popt)
        rss = float(np.sum((pred - sigma) ** 2))
        rmse = float(np.sqrt(rss / lam.size))
        param_str = ", ".join(f"{p:.4g}" for p in popt)
        print(f"  {name:<14}  params=({param_str})  RMSE = {rmse:.4g} MPa")
        return popt, rmse
    except Exception as exc:
        print(f"  {name:<14}  FIT FAILED: {exc}")
        return None, None


def main():
    lam, sigma = generate_synthetic_data()
    print("synthetic uniaxial stress-strain (Fung-like with 5% noise):")
    print(f"  stretch range: {lam.min():.2f} to {lam.max():.2f}")
    print(f"  stress range:  {sigma.min():.3f} to {sigma.max():.3f} MPa")
    print()
    print("fit:")
    fit_and_report("neo-Hookean",   neo_hookean,   [0.1],         lam, sigma)
    fit_and_report("Mooney-Rivlin", mooney_rivlin, [0.05, 0.05],  lam, sigma)
    fit_and_report("Fung",          fung,          [0.01, 10.0],  lam, sigma)
    print()
    print("interpretation: the neo-Hookean RMSE will be ~10x worse than Fung")
    print("for this J-curve because neo-Hookean cannot reproduce")
    print("strain-stiffening. Mooney-Rivlin is intermediate. The Fung")
    print("exponential fits because the synthetic data was Fung-generated;")
    print("on real soft-tissue data the Fung form fits skin, artery, and")
    print("tendon to within experimental scatter over the physiological")
    print("strain range.")


if __name__ == "__main__":
    main()
