# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Volume-by-water-displacement uncertainty.

A reader performs five repeated displacement readings on the same
object using a graduated cylinder with a known graduation interval.
The script combines two uncertainty components:

    (1) repeatability spread from the five readings, evaluated by
        the standard deviation of the sample mean,
    (2) resolution uncertainty from the cylinder's finite graduation,
        treated as uniformly distributed in +- half a graduation and
        contributing u_res = (delta / 2) / sqrt(3) per reading.

Both contributions enter the combined standard uncertainty in
quadrature. The script prints the breakdown and the expanded
uncertainty at coverage factor k = 2.
"""

from __future__ import annotations

import math
import statistics

# Graduation interval of the cylinder, in millilitres.
GRADUATION_ML = 1.0

# Five repeated displacement-volume readings, in millilitres.
# Illustrative values; replace with the reader's own measurements.
READINGS_ML = [47.5, 47.0, 47.5, 48.0, 47.5]


def displacement_uncertainty(readings_ml: list[float], graduation_ml: float) -> dict:
    """Combine repeatability and resolution components of u(V)."""
    n = len(readings_ml)
    mean_ml = statistics.fmean(readings_ml)

    # Type A: standard deviation of the mean
    sd_sample = statistics.stdev(readings_ml)
    u_repeat = sd_sample / math.sqrt(n)

    # Type B: resolution as uniform on +- delta/2
    u_resolution = (graduation_ml / 2.0) / math.sqrt(3.0)

    u_combined = math.sqrt(u_repeat**2 + u_resolution**2)
    U_k2 = 2.0 * u_combined

    return {
        "n": n,
        "mean_ml": mean_ml,
        "sd_sample_ml": sd_sample,
        "u_repeatability_ml": u_repeat,
        "u_resolution_ml": u_resolution,
        "u_combined_ml": u_combined,
        "U_k2_ml": U_k2,
        "U_k2_relative": U_k2 / mean_ml if mean_ml > 0 else float("nan"),
    }


def main() -> None:
    r = displacement_uncertainty(READINGS_ML, GRADUATION_ML)

    print(f"n readings              : {r['n']}")
    print(f"mean V                  : {r['mean_ml']:.3f}  mL")
    print(f"sample sd               : {r['sd_sample_ml']:.3f}  mL")
    print(f"u (repeatability)       : {r['u_repeatability_ml']:.3f}  mL")
    print(f"u (resolution)          : {r['u_resolution_ml']:.3f}  mL")
    print(f"u (combined, k=1)       : {r['u_combined_ml']:.3f}  mL")
    print(f"U (expanded, k=2)       : {r['U_k2_ml']:.3f}  mL")
    print(f"relative U (k=2)        : {r['U_k2_relative']:.2%}")


if __name__ == "__main__":
    main()
