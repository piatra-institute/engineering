"""
Statistical-process-control rules applied to daily verification
readings. Implements a subset of the Western Electric/Nelson rules
for detecting drift in a control instrument before formal
recalibration is due.

Supports Volume I, Chapter 3, Design exercise on the verification
routine.

Dependencies:
  numpy

Usage:
  python control_chart.py
"""

import numpy as np


def western_electric_check(readings: np.ndarray, mean: float,
                           sigma: float) -> dict[str, list[int]]:
    """Apply four basic Western Electric rules and return the
    1-based indices of readings that triggered each rule."""
    z = (readings - mean) / sigma
    rules: dict[str, list[int]] = {"rule1": [], "rule2": [],
                                    "rule3": [], "rule4": []}

    # Rule 1: any single point beyond +/-3 sigma
    for i, zi in enumerate(z):
        if abs(zi) > 3:
            rules["rule1"].append(i + 1)

    # Rule 2: 2 of 3 consecutive points beyond +/-2 sigma on same side
    for i in range(len(z) - 2):
        window = z[i:i + 3]
        if (np.sum(window > 2) >= 2) or (np.sum(window < -2) >= 2):
            rules["rule2"].append(i + 1)

    # Rule 3: 4 of 5 consecutive points beyond +/-1 sigma on same side
    for i in range(len(z) - 4):
        window = z[i:i + 5]
        if (np.sum(window > 1) >= 4) or (np.sum(window < -1) >= 4):
            rules["rule3"].append(i + 1)

    # Rule 4: 8 consecutive points on the same side of mean
    for i in range(len(z) - 7):
        window = z[i:i + 8]
        if np.all(window > 0) or np.all(window < 0):
            rules["rule4"].append(i + 1)

    return rules


def main() -> None:
    rng = np.random.default_rng(seed=20260516)
    # Simulate 30 days of readings: nominal then drifting from day 15.
    n_days = 30
    mean = 100.0
    sigma = 1.0
    readings = rng.normal(mean, sigma, n_days)
    # Add linear drift after day 15
    drift = np.where(np.arange(n_days) > 15,
                     0.15 * (np.arange(n_days) - 15),
                     0.0)
    readings = readings + drift

    print("Day-by-day readings (with drift after day 15):")
    for i, r in enumerate(readings, 1):
        z = (r - mean) / sigma
        marker = " *" if abs(z) > 2 else ""
        print(f"  day {i:2d}: {r:7.3f} (z = {z:+.2f}){marker}")

    print()
    rules = western_electric_check(readings, mean, sigma)
    for rule, indices in rules.items():
        if indices:
            print(f"  {rule}: triggered at days {indices}")
        else:
            print(f"  {rule}: no trigger")


if __name__ == "__main__":
    main()
