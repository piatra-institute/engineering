# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Sample size and power for the two-sample t-test.

Two functions:
  required_n: solve for n per group given alpha, power, and d.
  power_at_n: compute power given n per group, alpha, and d.

Approximate normal-theory formula (Gaussian populations, equal
variances, two-sided test, equal sample sizes):

    n_per_group = ((z_{1 - alpha/2} + z_{1 - beta}) / d)^2 * 2

The chapter's rule of thumb n = 16 / d^2 uses alpha = 0.05 and
power = 0.80, which gives (1.96 + 0.84)^2 * 2 ~ 15.7 in the
numerator.
"""

import math

# Standard normal inverse CDF for a small set of common quantiles.
# Source: standard table (Abramowitz & Stegun 26.2.23 rational
# approximation; here we just hardcode the most-used values to one
# extra decimal than the textbook).
Z_TABLE = {
    0.90: 1.2816,
    0.95: 1.6449,
    0.975: 1.9600,
    0.99: 2.3263,
    0.995: 2.5758,
    0.80: 0.8416,
    0.85: 1.0364,
}


def z_of(p: float) -> float:
    if p not in Z_TABLE:
        raise ValueError(f"add quantile {p} to Z_TABLE before requesting it")
    return Z_TABLE[p]


def required_n(d: float, alpha: float = 0.05, power: float = 0.80) -> float:
    z_alpha = z_of(1.0 - alpha / 2.0)
    z_power = z_of(power)
    return 2.0 * ((z_alpha + z_power) / d) ** 2


def power_at_n(n: int, d: float, alpha: float = 0.05) -> float:
    """Approximate power of two-sample two-sided t-test using
    the normal approximation (large n) for the noncentrality
    parameter delta = d * sqrt(n/2)."""
    z_alpha = z_of(1.0 - alpha / 2.0)
    ncp = d * math.sqrt(n / 2.0)
    # P(Z > z_alpha - ncp) under the alternative
    return 1.0 - _phi(z_alpha - ncp)


def _phi(z: float) -> float:
    """Standard normal CDF via erf."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def main() -> None:
    print("required n per group at alpha = 0.05, power = 0.80")
    for d in (0.2, 0.5, 0.8, 1.0):
        n = required_n(d)
        print(f"  d = {d:.1f}  ->  n ~ {n:6.1f}  "
              f"(rule of thumb 16/d^2 = {16.0 / d**2:6.1f})")
    print()
    print("power at fixed n = 30 per group")
    for d in (0.2, 0.5, 0.8, 1.0):
        p = power_at_n(30, d)
        print(f"  d = {d:.1f}  ->  power ~ {p:.3f}")


if __name__ == "__main__":
    main()
