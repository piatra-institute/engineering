"""
Monte Carlo simulation of instrument drift plus random variation.
For several recalibration intervals, estimate the probability that
the instrument exceeds tolerance before the next calibration.

Supports Volume I, Chapter 3, Simulation exercise on drift and
recalibration.

Dependencies:
  numpy

Usage:
  python drift_recalibration.py
"""

import numpy as np


def prob_out_of_tolerance(drift_rate: float, sigma: float,
                          tolerance: float, interval: float,
                          n_trials: int = 10_000,
                          rng: np.random.Generator | None = None
                          ) -> float:
    """Probability that the instrument exceeds tolerance at any time
    in [0, interval] given linear drift and Gaussian random component."""
    rng = rng if rng is not None else np.random.default_rng(seed=20260516)
    # Monte Carlo over trials; for each trial, sample drift direction
    # (could be positive or negative; we take linear drift with
    # symmetric sign for the worst case) and check end-of-interval.
    drifts = drift_rate * interval * np.ones(n_trials)
    noise = rng.normal(0, sigma, n_trials)
    final = drifts + noise
    return float(np.mean(np.abs(final) > tolerance))


def main() -> None:
    tolerance = 10.0
    drift_rate = 1.0  # per year
    intervals = np.linspace(0.5, 12.0, 24)
    sigma_ratios = [0.05, 0.1, 0.2]

    print(f"{'interval (yr)':>14} ", end="")
    for sr in sigma_ratios:
        print(f"{'sigma/D='+str(sr):>14}", end=" ")
    print()

    for interval in intervals:
        print(f"{interval:14.2f} ", end="")
        for sr in sigma_ratios:
            sigma = sr * tolerance
            p = prob_out_of_tolerance(drift_rate, sigma, tolerance,
                                      interval)
            print(f"{p:14.4f}", end=" ")
        print()


if __name__ == "__main__":
    main()
