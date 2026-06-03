# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Read a thermistor calibration CSV (columns: temperature in degrees
Celsius, resistance in ohms), transform to Arrhenius axes (ln(R/R25)
vs 1/T - 1/T25), fit a straight line by ordinary least squares, and
report the recovered B-constant. Writes the transformed data to a
sibling CSV for plotting.

The chapter's design exercise asks the reader to set up this plot
for an NTC thermistor; this script is the worked instance.

Supports Volume II, Chapter 2, Section 2.6 and Section 2.7 design
exercise on thermistor calibration.

Usage:
  python thermistor_calibration.py <in_csv>

  python thermistor_calibration.py ../data/thermistor_calibration.csv

Output:
  Writes <in_csv stem>_arrhenius.csv next to the input, with the
  transformed columns. Prints recovered B and R25.
"""

from __future__ import annotations

import csv
import math
import sys
from pathlib import Path


def lin_fit(xs: list[float], ys: list[float]) -> tuple[float, float]:
    """Ordinary least squares fit y = m x + b."""
    n = len(xs)
    sx = sum(xs)
    sy = sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    denom = n * sxx - sx * sx
    if denom == 0.0:
        raise ValueError("singular fit")
    m = (n * sxy - sx * sy) / denom
    b = (sy - m * sx) / n
    return m, b


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    in_path = Path(sys.argv[1])
    if not in_path.exists():
        print(f"missing input: {in_path}")
        return 1

    Ts_C: list[float] = []
    Rs: list[float] = []
    with in_path.open() as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            Ts_C.append(float(row["temperature_C"]))
            Rs.append(float(row["resistance_ohm"]))

    # Convert to kelvin
    Ts_K = [T + 273.15 for T in Ts_C]
    # Reference: pick the row closest to 25 C
    idx_ref = min(range(len(Ts_C)), key=lambda i: abs(Ts_C[i] - 25.0))
    T_ref = Ts_K[idx_ref]
    R_ref = Rs[idx_ref]

    xs = [1.0 / T - 1.0 / T_ref for T in Ts_K]
    ys = [math.log(R / R_ref) for R in Rs]

    B, intercept = lin_fit(xs, ys)

    # Write transformed CSV
    out_path = in_path.with_name(in_path.stem + "_arrhenius.csv")
    with out_path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            ["temperature_K", "inv_T_minus_inv_Tref", "ln_R_over_Rref"]
        )
        for TK, x, y in zip(Ts_K, xs, ys):
            writer.writerow([f"{TK:.3f}", f"{x:.6e}", f"{y:.6f}"])

    print(f"wrote {out_path} with {len(xs)} rows.")
    print(f"  R25 (reference, closest to 25 C): {R_ref:.1f} ohm")
    print(f"  T_ref: {T_ref:.2f} K")
    print(f"  fitted B-constant: {B:.1f} K")
    print(f"  intercept (should be near 0): {intercept:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
