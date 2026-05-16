"""
Cost model for recalibration-interval choice.

Combines per-calibration cost with the expected cost of discovering
an out-of-tolerance condition; identifies the cost-minimising
interval.

Supports Volume I, Chapter 3, Simulation exercise on cost-of-
recalibration.

Dependencies:
  numpy

Usage:
  python recalibration_cost.py
"""

import numpy as np

from drift_recalibration import prob_out_of_tolerance


def expected_annual_cost(interval: float, cal_cost: float,
                         oot_cost: float, drift_rate: float,
                         sigma: float, tolerance: float) -> float:
    """Expected annual cost: amortised calibration plus expected loss
    from out-of-tolerance discovery."""
    p_oot = prob_out_of_tolerance(drift_rate, sigma, tolerance,
                                  interval)
    return cal_cost / interval + p_oot * oot_cost / interval


def main() -> None:
    tolerance = 10.0
    drift_rate = 1.0
    sigma = 1.0  # sigma/tolerance = 0.1
    cal_cost = 300.0
    oot_cost = 10000.0

    intervals = np.arange(0.5, 10.0, 0.25)
    print(f"{'interval (yr)':>14} {'expected cost ($/yr)':>22}")
    best_int, best_cost = 0.0, float("inf")
    for interval in intervals:
        c = expected_annual_cost(interval, cal_cost, oot_cost,
                                 drift_rate, sigma, tolerance)
        if c < best_cost:
            best_cost = c
            best_int = interval
        print(f"{interval:14.2f} {c:22.2f}")

    print()
    print(f"Optimal interval: {best_int:.2f} yr at ${best_cost:.2f}/yr")


if __name__ == "__main__":
    main()
