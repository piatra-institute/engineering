# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Sample mean of n Cauchy variables: the CLT fails.

The Cauchy distribution has no finite mean and no finite variance.
The sample mean of n independent Cauchy(0, 1) variables is itself
distributed Cauchy(0, 1); increasing n does not concentrate the mean.

This script demonstrates the failure by reporting the spread of
1000 trial sample-means for several values of n. Compare to the
1/sqrt(n) reduction that would obtain for a Gaussian parent.
"""

import numpy as np

RNG = np.random.default_rng(7)
TRIALS = 1_000


def main() -> None:
    print(f"{'n':>5}  {'25th pct mean':>15}  {'75th pct mean':>15}  {'mad':>10}")
    for n in (1, 5, 50, 500, 5000):
        # Cauchy samples via ratio of two independent normals
        samples = RNG.standard_cauchy(size=(TRIALS, n))
        means = samples.mean(axis=1)
        # Median absolute deviation, robust to the heavy tails
        mad = np.median(np.abs(means - np.median(means)))
        q25 = np.quantile(means, 0.25)
        q75 = np.quantile(means, 0.75)
        print(f"{n:>5d}  {q25:>15.4f}  {q75:>15.4f}  {mad:>10.4f}")


if __name__ == "__main__":
    main()
