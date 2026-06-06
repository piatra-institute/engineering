#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""
Load-strength (stress-strength) interference reliability for the case
study of section 13.9. Computes the reliability index beta and the
failure probability p_f for three models:

    1. Gaussian load and strength, independent.
    2. Lognormal load and strength, independent.
    3. Gaussian load and strength with correlation rho (a common-cause
       coupling between load and strength).

Each closed-form result is cross-checked against a Monte Carlo
estimate of p_f = Pr(L >= S), so the reader can confirm the
interference integral on input distributions where no closed form
exists.

The worked pressure-vessel numbers (in bar) are the defaults:
    strength S: mean 600, sd 40
    load     L: mean 400, sd 30
giving safety factor 1.5 and Gaussian beta = 4.0.

Dependencies:
    numpy

Usage:
    uv run load_strength.py
    uv run load_strength.py --mu-s 600 --sd-s 80 --mu-l 400 --sd-l 30
    uv run load_strength.py --rho -0.5
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def _phi(z: float) -> float:
    """Standard-normal CDF via the error function."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def gaussian_case(mu_s, sd_s, mu_l, sd_l, rho=0.0):
    """Reliability index and p_f for Gaussian load and strength.

    The margin M = S - L is Gaussian with mean mu_s - mu_l and variance
    sd_s^2 + sd_l^2 - 2 rho sd_s sd_l. Failure is M <= 0.
    """
    var_m = sd_s**2 + sd_l**2 - 2.0 * rho * sd_s * sd_l
    beta = (mu_s - mu_l) / math.sqrt(var_m)
    return beta, _phi(-beta)


def lognormal_params(mean, sd):
    """Log-space mean and sd of a lognormal with the given mean and sd."""
    cv2 = (sd / mean) ** 2
    sigma_ln = math.sqrt(math.log(1.0 + cv2))
    mu_ln = math.log(mean) - 0.5 * sigma_ln**2
    return mu_ln, sigma_ln


def lognormal_case(mu_s, sd_s, mu_l, sd_l):
    """Reliability index and p_f for independent lognormal inputs.

    In log space ln S and ln L are normal, so ln S - ln L is normal and
    the failure event S > L maps to ln S > ln L.
    """
    mu_ls, sd_ls = lognormal_params(mu_s, sd_s)
    mu_ll, sd_ll = lognormal_params(mu_l, sd_l)
    beta = (mu_ls - mu_ll) / math.sqrt(sd_ls**2 + sd_ll**2)
    return beta, _phi(-beta)


def monte_carlo_gaussian(mu_s, sd_s, mu_l, sd_l, rho, n, rng):
    """Monte Carlo estimate of p_f for correlated Gaussian inputs."""
    cov = [[sd_s**2, rho * sd_s * sd_l],
           [rho * sd_s * sd_l, sd_l**2]]
    draws = rng.multivariate_normal([mu_s, mu_l], cov, size=n)
    s, ell = draws[:, 0], draws[:, 1]
    return float(np.mean(ell >= s))


def monte_carlo_lognormal(mu_s, sd_s, mu_l, sd_l, n, rng):
    """Monte Carlo estimate of p_f for independent lognormal inputs."""
    mu_ls, sd_ls = lognormal_params(mu_s, sd_s)
    mu_ll, sd_ll = lognormal_params(mu_l, sd_l)
    s = rng.lognormal(mu_ls, sd_ls, size=n)
    ell = rng.lognormal(mu_ll, sd_ll, size=n)
    return float(np.mean(ell >= s))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mu-s", type=float, default=600.0)
    parser.add_argument("--sd-s", type=float, default=40.0)
    parser.add_argument("--mu-l", type=float, default=400.0)
    parser.add_argument("--sd-l", type=float, default=30.0)
    parser.add_argument("--rho", type=float, default=-0.5,
                        help="correlation between load and strength")
    parser.add_argument("--n", type=int, default=2_000_000)
    args = parser.parse_args()

    rng = np.random.default_rng(2026)

    sf = args.mu_s / args.mu_l
    print(f"Strength S ~ mean {args.mu_s}, sd {args.sd_s}")
    print(f"Load     L ~ mean {args.mu_l}, sd {args.sd_l}")
    print(f"Nominal safety factor mu_S / mu_L = {sf:.3f}\n")

    # 1. Gaussian, independent.
    beta_g, pf_g = gaussian_case(args.mu_s, args.sd_s, args.mu_l, args.sd_l)
    mc_g = monte_carlo_gaussian(args.mu_s, args.sd_s, args.mu_l, args.sd_l,
                                0.0, args.n, rng)
    print("Gaussian, independent:")
    print(f"    beta = {beta_g:.3f}   p_f = {pf_g:.3e}   MC = {mc_g:.3e}")

    # 2. Lognormal, independent.
    beta_ln, pf_ln = lognormal_case(args.mu_s, args.sd_s, args.mu_l, args.sd_l)
    mc_ln = monte_carlo_lognormal(args.mu_s, args.sd_s, args.mu_l, args.sd_l,
                                  args.n, rng)
    print("Lognormal, independent:")
    print(f"    beta = {beta_ln:.3f}   p_f = {pf_ln:.3e}   MC = {mc_ln:.3e}")

    # 3. Gaussian, correlated.
    beta_c, pf_c = gaussian_case(args.mu_s, args.sd_s, args.mu_l, args.sd_l,
                                 rho=args.rho)
    mc_c = monte_carlo_gaussian(args.mu_s, args.sd_s, args.mu_l, args.sd_l,
                                args.rho, args.n, rng)
    print(f"Gaussian, rho = {args.rho:+.2f}:")
    print(f"    beta = {beta_c:.3f}   p_f = {pf_c:.3e}   MC = {mc_c:.3e}")

    print(
        "\nThe failure probability lives in the overlap of the two"
        " densities, not in the gap between the means. Doubling sd_S at"
        " fixed means leaves the safety factor untouched but moves p_f by"
        " orders of magnitude, and an adverse correlation (rho < 0) cuts"
        " the reliability index further. The Monte Carlo column confirms"
        " each closed-form tail."
    )


if __name__ == "__main__":
    main()
