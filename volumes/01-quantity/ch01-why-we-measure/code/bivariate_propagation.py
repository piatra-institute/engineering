"""
Bivariate-normal sampling and empirical-vs-analytical variance of
z = x + y under varying correlation.

Supports Volume I, Chapter 1, Simulation exercise 3.

Dependencies:
  numpy

Usage:
  python bivariate_propagation.py
"""

import numpy as np


def variance_of_sum(rho: float, sigma_x: float = 1.0,
                    sigma_y: float = 1.0) -> float:
    """Analytical Var(x+y) for given correlation and standard deviations."""
    return sigma_x ** 2 + sigma_y ** 2 + 2 * rho * sigma_x * sigma_y


def empirical_variance_of_sum(rho: float, n_samples: int = 1000,
                              sigma_x: float = 1.0, sigma_y: float = 1.0,
                              rng: np.random.Generator | None = None
                              ) -> float:
    """Draw n_samples (x,y) pairs from the bivariate normal and return
    the sample variance of x+y."""
    rng = rng if rng is not None else np.random.default_rng(seed=20260516)
    cov = np.array([[sigma_x ** 2, rho * sigma_x * sigma_y],
                    [rho * sigma_x * sigma_y, sigma_y ** 2]])
    samples = rng.multivariate_normal(mean=[0, 0], cov=cov, size=n_samples)
    z = samples[:, 0] + samples[:, 1]
    return float(z.var(ddof=1))


def main() -> None:
    correlations = [-0.9, 0.0, 0.9]
    print(f"# Bivariate-normal: sigma_x = sigma_y = 1, n_samples = 1000")
    print()
    print(f"{'rho':>6} {'Var(z) analytical':>20} "
          f"{'Var(z) empirical':>20} {'sigma_z analytical':>22} "
          f"{'sigma_z empirical':>22}")
    for rho in correlations:
        var_a = variance_of_sum(rho)
        var_e = empirical_variance_of_sum(rho)
        print(f"{rho:6.2f} {var_a:20.4f} {var_e:20.4f} "
              f"{var_a ** 0.5:22.4f} {var_e ** 0.5:22.4f}")


if __name__ == "__main__":
    main()
