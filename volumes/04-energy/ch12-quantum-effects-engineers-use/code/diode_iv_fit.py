#!/usr/bin/env python3
"""Fit the Shockley diode equation to a measured I-V sweep.

Reads data/diode_iv_sweep.csv (columns: voltage_V, current_A), restricts the
fit to the exponential region, and recovers the saturation current I_s and the
ideality-scaled thermal voltage from a straight-line fit to ln(I) vs V.

Run from the chapter directory:
    python3 code/diode_iv_fit.py
"""
import csv
import math
import pathlib

DATA = pathlib.Path(__file__).resolve().parents[1] / "data" / "diode_iv_sweep.csv"

# exponential region: above the noise floor, below series-resistance roll-off.
V_LOW, V_HIGH = 0.30, 0.50


def load(path):
    v, i = [], []
    with open(path) as f:
        for row in csv.DictReader(f):
            v.append(float(row["voltage_V"]))
            i.append(float(row["current_A"]))
    return v, i


def linear_fit(xs, ys):
    """Ordinary least squares slope and intercept."""
    n = len(xs)
    sx = sum(xs)
    sy = sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    intercept = (sy - slope * sx) / n
    return slope, intercept


def main():
    v, i = load(DATA)
    xs, ys = [], []
    for vk, ik in zip(v, i):
        if V_LOW <= vk <= V_HIGH and ik > 0.0:
            xs.append(vk)
            ys.append(math.log(ik))
    slope, intercept = linear_fit(xs, ys)
    # slope = 1 / (n * V_T); intercept = ln(I_s)
    vt_eff = 1.0 / slope            # n * V_T, the effective thermal voltage
    i_s = math.exp(intercept)
    decade_mv = math.log(10.0) / slope * 1000.0
    print(f"effective thermal voltage n*V_T = {vt_eff*1000:.1f} mV")
    print(f"saturation current I_s        = {i_s:.2e} A")
    print(f"slope                         = {decade_mv:.1f} mV per decade")


if __name__ == "__main__":
    main()
