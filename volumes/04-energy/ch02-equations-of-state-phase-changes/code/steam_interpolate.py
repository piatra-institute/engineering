#!/usr/bin/env python3
"""Linear and bilinear interpolation in a property table.

Reads a saturated-water table (data/water_saturation.csv) and returns
saturation properties at an arbitrary temperature by linear interpolation
in the table grid. The two-dimensional bilinear routine interpolates a
superheated-vapour property in both pressure and temperature.

The interpolation error is small in regions of smooth behaviour and grows
near the saturation curve and the critical point, where the underlying
surface curves sharply.
"""

import csv


def load_table(path):
    rows = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            rows.append({k: float(v) for k, v in row.items()})
    return rows


def linterp(x, x1, x2, y1, y2):
    if x2 == x1:
        return y1
    return y1 + (x - x1) * (y2 - y1) / (x2 - x1)


def sat_property(table, T, key, tkey="T_C"):
    """Linearly interpolate property `key` at temperature T."""
    table = sorted(table, key=lambda r: r[tkey])
    if T <= table[0][tkey]:
        return table[0][key]
    if T >= table[-1][tkey]:
        return table[-1][key]
    for lo, hi in zip(table, table[1:]):
        if lo[tkey] <= T <= hi[tkey]:
            return linterp(T, lo[tkey], hi[tkey], lo[key], hi[key])
    return None


def bilinear(p, T, p1, p2, T1, T2, q11, q12, q21, q22):
    """Bilinear interpolation. q_ij is the value at (p_i, T_j)."""
    r1 = linterp(T, T1, T2, q11, q12)
    r2 = linterp(T, T1, T2, q21, q22)
    return linterp(p, p1, p2, r1, r2)


if __name__ == "__main__":
    table = load_table("../data/water_saturation.csv")
    for T in (120.0, 175.0, 215.0):
        hg = sat_property(table, T, "h_g_kJkg")
        psat = sat_property(table, T, "p_sat_kPa")
        print(f"T={T} C: p_sat={psat:8.1f} kPa, h_g={hg:8.1f} kJ/kg")
