# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Compare cumulative time error across the four clock families.

For a one-year continuous operation, this script reports the
expected accumulated time error of a representative clock from
each of the four families catalogued in Section 6.2:

  - regulator pendulum (fractional accuracy 1e-7)
  - quartz wristwatch (1e-6)
  - chip-scale atomic (1e-11)
  - caesium fountain (1e-16)

The cumulative error is (fractional accuracy) * (elapsed time).
"""

import numpy as np


def main() -> None:
    seconds_per_year = 365.25 * 24 * 3600
    seconds_per_day = 24 * 3600

    print("Cumulative time error after one year of continuous operation:")
    print(f"{'family':>26}  {'sigma_y':>10}  {'1 day':>14}  {'1 year':>14}")
    rows = (
        ("regulator pendulum", 1.0e-7),
        ("quartz wristwatch",  1.0e-6),
        ("quartz TCXO",        3.0e-8),
        ("quartz OCXO",        1.0e-10),
        ("chip-scale atomic",  1.0e-11),
        ("caesium beam",       5.0e-13),
        ("caesium fountain",   1.0e-16),
        ("optical (lab)",      1.0e-18),
    )
    for name, sigma in rows:
        e_day = sigma * seconds_per_day
        e_year = sigma * seconds_per_year
        print(f"{name:>26}  {sigma:>10.1e}  "
              f"{e_day:>14.3e}  {e_year:>14.3e}")

    # Compare against Patriot per-100h accumulated error
    patriot_per_tick = 9.5e-8
    patriot_100h = patriot_per_tick * (100 * 3600 * 10)
    print()
    print(f"Patriot 100-h accumulated error (24-bit truncation of 1/10): "
          f"{patriot_100h:.3f} s")


if __name__ == "__main__":
    main()
