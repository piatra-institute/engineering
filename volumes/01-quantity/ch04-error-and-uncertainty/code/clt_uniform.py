# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Empirical distribution of the sample mean of n uniform samples.

Verifies the CLT: as n grows, the distribution of the sample mean
becomes Gaussian regardless of the (well-behaved) parent
distribution. The uniform on [-1, 1] has variance 1/3, so the
predicted standard deviation of the n-sample mean is 1/sqrt(3n).
"""

import numpy as np

RNG = np.random.default_rng(2026)
TRIALS = 10_000


def main() -> None:
    print(f"{'n':>4}  {'empirical sd':>14}  {'predicted sd':>14}")
    for n in (1, 5, 10, 50, 100):
        samples = RNG.uniform(-1, 1, size=(TRIALS, n))
        means = samples.mean(axis=1)
        predicted = 1.0 / np.sqrt(3.0 * n)
        print(f"{n:>4d}  {means.std(ddof=1):>14.5f}  {predicted:>14.5f}")


if __name__ == "__main__":
    main()
