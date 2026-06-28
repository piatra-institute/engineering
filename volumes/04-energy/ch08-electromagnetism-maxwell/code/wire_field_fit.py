"""Fit the 1/r law to measured magnetic field around a current-carrying
wire, the analysis half of the chapter project.

Reads data/wire_field_measurements.csv (radial distance, background-subtracted
B for each test current), fits B = A r^-n by linear regression in log-log
space, and reports the exponent n and the inferred current from the
amplitude A against the Ampere prediction A = mu0 I / (2 pi).
"""

import csv
import numpy as np

MU0 = 4.0e-7 * np.pi


def load(path):
    r, b1, b2, b3 = [], [], [], []
    with open(path) as f:
        for row in csv.DictReader(f):
            r.append(float(row["r_cm"]) * 1e-2)
            b1.append(float(row["B_1A_uT"]) * 1e-6)
            b2.append(float(row["B_2A_uT"]) * 1e-6)
            b3.append(float(row["B_3A_uT"]) * 1e-6)
    return (np.array(r), np.array(b1), np.array(b2), np.array(b3))


def fit_power_law(r, b):
    """Return (n, A) for B = A r^-n via least squares on logs."""
    mask = b > 0
    coeffs = np.polyfit(np.log(r[mask]), np.log(b[mask]), 1)
    n = -coeffs[0]
    A = np.exp(coeffs[1])
    return n, A


if __name__ == "__main__":
    r, b1, b2, b3 = load("../data/wire_field_measurements.csv")
    for label, b, I in [("1 A", b1, 1.0), ("2 A", b2, 2.0), ("3 A", b3, 3.0)]:
        n, A = fit_power_law(r, b)
        I_inferred = A * 2.0 * np.pi / MU0
        print(f"{label}: exponent n = {n:.3f}, "
              f"inferred current = {I_inferred:.2f} A "
              f"(set {I:.1f} A)")
