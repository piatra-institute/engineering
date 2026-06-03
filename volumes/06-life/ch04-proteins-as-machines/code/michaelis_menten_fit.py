# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "scipy"]
# ///
"""Least-squares fit of v versus [S] for the Michaelis-Menten model.

Reads ../data/mm_kinetics_example.csv and reports Vmax, Km, and the
standard errors. Also reports the equivalent Lineweaver-Burk
linearisation as a cross-check.

Engineering reading: the nonlinear least-squares fit is the standard
of practice; the Lineweaver-Burk double-reciprocal plot is a teaching
diagnostic and a poor estimator because the reciprocal transform
amplifies error at low substrate concentrations.
"""

from __future__ import annotations

import csv
import pathlib

import numpy as np
from scipy.optimize import curve_fit


HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent / "data" / "mm_kinetics_example.csv"


def mm_rate(substrate: np.ndarray, vmax: float, km: float) -> np.ndarray:
    return vmax * substrate / (km + substrate)


def load_csv(path: pathlib.Path) -> tuple[np.ndarray, np.ndarray]:
    substrate: list[float] = []
    velocity: list[float] = []
    with path.open() as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            substrate.append(float(row["substrate_M"]))
            velocity.append(float(row["velocity_uM_per_min"]))
    return np.asarray(substrate), np.asarray(velocity)


def nonlinear_fit(s: np.ndarray, v: np.ndarray) -> tuple[float, float, float, float]:
    popt, pcov = curve_fit(mm_rate, s, v, p0=(max(v), np.median(s)))
    vmax, km = popt
    perr = np.sqrt(np.diag(pcov))
    return vmax, perr[0], km, perr[1]


def lineweaver_burk(s: np.ndarray, v: np.ndarray) -> tuple[float, float]:
    inv_s = 1.0 / s
    inv_v = 1.0 / v
    slope, intercept = np.polyfit(inv_s, inv_v, 1)
    vmax_lb = 1.0 / intercept
    km_lb = slope * vmax_lb
    return vmax_lb, km_lb


def main() -> None:
    s, v = load_csv(DATA)
    vmax, dvmax, km, dkm = nonlinear_fit(s, v)
    vmax_lb, km_lb = lineweaver_burk(s, v)

    print("Michaelis-Menten fit (nonlinear least squares):")
    print(f"  Vmax = {vmax:7.2f} +/- {dvmax:.2f} uM/min")
    print(f"  Km   = {km:.3e} +/- {dkm:.1e} M")
    print()
    print("Lineweaver-Burk linearisation (teaching diagnostic):")
    print(f"  Vmax = {vmax_lb:7.2f} uM/min")
    print(f"  Km   = {km_lb:.3e} M")
    print()

    residuals = v - mm_rate(s, vmax, km)
    rms = float(np.sqrt(np.mean(residuals**2)))
    print(f"Residual RMS: {rms:.3f} uM/min ({100 * rms / vmax:.1f}% of Vmax)")


if __name__ == "__main__":
    main()
