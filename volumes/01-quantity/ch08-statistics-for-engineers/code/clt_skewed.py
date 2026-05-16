# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Central limit theorem on a skewed parent.

Empirically verifies that the sample mean of an exponential(1)
parent becomes approximately Gaussian as n grows, while the parent
itself is heavily right-skewed (skewness 2.0). Reports empirical
standard deviation of the sample mean against the theoretical
1/sqrt(n) (since exponential(1) has sd 1).
"""

import numpy as np

RNG = np.random.default_rng(2026)
TRIALS = 10_000


def main() -> None:
    print(f"{'n':>4}  {'mean(means)':>11}  {'sd(means)':>11}  "
          f"{'1/sqrt(n)':>11}  {'skew(means)':>11}")
    for n in (1, 2, 5, 10, 30, 100):
        samples = RNG.exponential(1.0, size=(TRIALS, n))
        means = samples.mean(axis=1)
        sd = means.std(ddof=1)
        # Sample skewness = m3 / m2^(3/2).
        centred = means - means.mean()
        m2 = (centred ** 2).mean()
        m3 = (centred ** 3).mean()
        skew = m3 / (m2 ** 1.5)
        predicted = 1.0 / np.sqrt(n)
        print(f"{n:>4d}  {means.mean():>11.4f}  {sd:>11.4f}  "
              f"{predicted:>11.4f}  {skew:>11.4f}")
    print()
    print("Population skewness of exponential(1) is 2.0; the empirical")
    print("skew(means) column should fall toward zero as n grows.")


if __name__ == "__main__":
    main()
