"""Fit Young's modulus from a tensile-test dataset and locate the yield point.

Reads a CSV of (strain, stress) pairs, fits a straight line through the elastic
region by least squares to recover E, then applies the 0.2 percent offset
construction to estimate the yield stress. Used for figure
fig-tensile-test-fit and the cantilever-beam project analysis.
"""

from __future__ import annotations

import csv
import sys


def read_csv(path):
    strain, stress = [], []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            strain.append(float(row["strain"]))
            stress.append(float(row["stress_MPa"]))
    return strain, stress


def linear_fit(x, y):
    """Least-squares slope and intercept of y = m x + b (no numpy needed)."""
    n = len(x)
    sx, sy = sum(x), sum(y)
    sxx = sum(xi * xi for xi in x)
    sxy = sum(xi * yi for xi, yi in zip(x, y))
    denom = n * sxx - sx * sx
    m = (n * sxy - sx * sy) / denom
    b = (sy - m * sx) / n
    return m, b


def fit_modulus(strain, stress, elastic_fraction=0.5):
    """Fit E on the lowest `elastic_fraction` of the data by stress."""
    peak = max(stress)
    pts = [(e, s) for e, s in zip(strain, stress) if s <= elastic_fraction * peak]
    xs = [e for e, _ in pts]
    ys = [s for _, s in pts]
    m, b = linear_fit(xs, ys)
    return m  # MPa per unit strain = Young's modulus in MPa


def offset_yield(strain, stress, E, offset=0.002):
    """0.2 percent offset yield: intersection of the offset line with the curve."""
    # offset line: sigma = E (eps - offset). Find first data point where the
    # measured stress drops below the offset line (curve has crossed it).
    prev = None
    for e, s in zip(strain, stress):
        line = E * (e - offset)
        if line > 0 and s <= line and prev is not None:
            return 0.5 * (prev[1] + s)   # crude midpoint estimate
        prev = (e, s)
    return None


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "../data/aluminum_6061_tensile.csv"
    strain, stress = read_csv(path)
    E = fit_modulus(strain, stress)
    sy = offset_yield(strain, stress, E)
    print(f"Young's modulus E = {E/1000:.1f} GPa")
    if sy is not None:
        print(f"0.2% offset yield ~ {sy:.0f} MPa")
