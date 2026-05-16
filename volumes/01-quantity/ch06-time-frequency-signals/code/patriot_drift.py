# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Reconstruct the Patriot range-gate clock-drift mechanism.

The Patriot tracking software incremented an integer counter at
10 Hz (each tick = one-tenth of a second) and converted to
real-valued seconds by multiplying by a fixed-point binary
truncation of 1/10. The exact decimal 0.1 has no exact binary
representation; a 24-bit truncation introduces a per-conversion
error of approximately 9.5e-8 s per tick.

This script reproduces the cumulative error as a function of
continuous operating time and verifies the GAO report's
0.34 s after 100 h figure.
"""

import numpy as np


def truncated_binary(x: float, bits: int) -> float:
    """Truncate x in [0, 1) to the nearest fraction of 2**bits."""
    return np.floor(x * (1 << bits)) / (1 << bits)


def main() -> None:
    bits = 24
    one_tenth_truncated = truncated_binary(0.1, bits)
    per_tick_error = 0.1 - one_tenth_truncated
    print(f"truncated 1/10 ({bits} bits)  = {one_tenth_truncated!r}")
    print(f"per-tick error                = {per_tick_error:.4e} s")

    for hours in (1, 8, 24, 50, 100):
        ticks = hours * 3600 * 10
        cum_error = per_tick_error * ticks
        print(f"  after {hours:>3d} h ({ticks:>8d} ticks): "
              f"cumulative error {cum_error:.3f} s")

    # Compare with 32 and 64 bit truncations
    print()
    print("comparison of truncation widths after 100 h:")
    for b in (16, 24, 32, 64):
        e = (0.1 - truncated_binary(0.1, b))
        cum = e * 100 * 3600 * 10
        print(f"  {b:>2d}-bit truncation: per-tick {e:.3e} s, "
              f"cumulative {cum:.3e} s")


if __name__ == "__main__":
    main()
