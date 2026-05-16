# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Reconstruct the Patriot Dhahran timing-drift model.

The Patriot tracking software stored elapsed time as an integer counter
of tenths of a second. The conversion from the counter to seconds used
a 24-bit fixed-point approximation of 1/10, whose representation error
was approximately 9.54e-8 in the converted seconds value per counter
tick (with the bit pattern documented in the GAO report).

This script writes ../data/patriot-drift.csv with one row per operating
hour and the columns:
  hours, counter, timing_error_s, position_error_m_at_scud_speed

Used by section 16.8.1 and Failure-analysis exercise 1.
"""
from __future__ import annotations

import csv
import pathlib

# Per-tick truncation error (GAO 1992, approximation):
PER_TICK_ERROR_S = 9.5367431640625e-8  # 2^{-20} - the canonical 24-bit residual
SCUD_SPEED_M_PER_S = 1676.0


def main() -> None:
    out_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "patriot-drift.csv"
    rows = []
    for h in range(0, 121, 1):
        counter = h * 36_000  # ticks per hour = 10 * 3600
        err_s = counter * PER_TICK_ERROR_S
        err_m = err_s * SCUD_SPEED_M_PER_S
        rows.append((h, counter, err_s, err_m))

    with out_path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["hours", "counter", "timing_error_s", "position_error_m_at_scud_speed"])
        w.writerows(rows)

    print(f"wrote {len(rows)} rows to {out_path}")
    for hours, counter, err_s, err_m in (rows[0], rows[20], rows[50], rows[100], rows[120]):
        print(f"  h={hours:>3}  counter={counter:>9}  dt={err_s:.4f}s  dx={err_m:.1f}m")


if __name__ == "__main__":
    main()
