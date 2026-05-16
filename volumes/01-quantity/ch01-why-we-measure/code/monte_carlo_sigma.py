"""
Monte Carlo demonstration of the 1/sqrt(n) scaling of the standard
deviation of the sample mean, and the failure of that scaling in the
presence of a systematic offset.

Supports:
  - Volume I, Chapter 1, Simulation exercise 1 (sigma/sqrt(n) scaling)
  - Volume I, Chapter 1, Simulation exercise 2 (systematic offset)

Dependencies:
  numpy

Usage:
  python monte_carlo_sigma.py [--systematic DELTA]

The default is no systematic offset. Adding --systematic 2.0 reproduces
the second exercise's setup.
"""

import argparse
import numpy as np


def sigma_of_mean_scaling(mu: float, sigma: float, n_values: list[int],
                          n_trials: int = 10_000, delta: float = 0.0,
                          rng: np.random.Generator | None = None
                          ) -> dict[int, tuple[float, float]]:
    """For each sample size n in n_values, draw n_trials independent
    sample-means and return the empirical (mean, std) of those means.

    Adds a constant systematic offset delta to every measurement when
    delta != 0.
    """
    rng = rng if rng is not None else np.random.default_rng(seed=20260516)
    results: dict[int, tuple[float, float]] = {}
    for n in n_values:
        # Draw n_trials samples of size n each, all in one tensor.
        samples = rng.normal(loc=mu + delta, scale=sigma, size=(n_trials, n))
        means = samples.mean(axis=1)
        results[n] = (float(means.mean()), float(means.std(ddof=1)))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--systematic", type=float, default=0.0,
                        help="Constant systematic offset added to every "
                             "measurement (default: 0)")
    parser.add_argument("--mu", type=float, default=100.0)
    parser.add_argument("--sigma", type=float, default=5.0)
    parser.add_argument("--trials", type=int, default=10_000)
    args = parser.parse_args()

    n_values = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    results = sigma_of_mean_scaling(mu=args.mu, sigma=args.sigma,
                                    n_values=n_values,
                                    n_trials=args.trials,
                                    delta=args.systematic)

    print(f"# Monte Carlo: mu={args.mu}, sigma={args.sigma}, "
          f"trials={args.trials}, systematic={args.systematic}")
    print(f"# Expected sigma/sqrt(n) scaling for the std of the mean.")
    print(f"# Expected apparent mean: mu + systematic = "
          f"{args.mu + args.systematic}")
    print()
    print(f"{'n':>5} {'mean_of_means':>16} {'std_of_means':>16} "
          f"{'sigma/sqrt(n)':>16}")
    for n in n_values:
        mean_m, std_m = results[n]
        analytic = args.sigma / (n ** 0.5)
        print(f"{n:5d} {mean_m:16.4f} {std_m:16.4f} {analytic:16.4f}")


if __name__ == "__main__":
    main()
