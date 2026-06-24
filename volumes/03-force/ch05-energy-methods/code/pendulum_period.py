"""Large-amplitude pendulum period versus the small-angle prediction.

Integrates theta'' + (g/L) sin(theta) = 0 with RK4 from rest at an
initial amplitude, measures the period by detecting the return to the
turning point, and compares against the small-angle period and the
first amplitude correction T = T0 (1 + theta0^2 / 16).

Run:
    python pendulum_period.py
writes data/pendulum_period.csv.
"""

from __future__ import annotations
import csv
import math
from pathlib import Path

G = 9.81
L = 1.0


def deriv(state):
    th, w = state
    return (w, -(G / L) * math.sin(th))


def rk4_step(state, h):
    def add(s, k, f):
        return (s[0] + f * k[0], s[1] + f * k[1])
    k1 = deriv(state)
    k2 = deriv(add(state, k1, h / 2))
    k3 = deriv(add(state, k2, h / 2))
    k4 = deriv(add(state, k3, h))
    return (state[0] + (h / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
            state[1] + (h / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]))


def measured_period(theta0, h=1.0e-4):
    """Quarter period = time from amplitude to the first zero crossing."""
    state = (theta0, 0.0)
    t = 0.0
    prev = state[0]
    while True:
        new = rk4_step(state, h)
        # detect crossing theta = 0 (downward)
        if prev > 0.0 >= new[0]:
            # linear interpolation for the crossing time
            frac = prev / (prev - new[0])
            t_cross = t + frac * h
            return 4.0 * t_cross
        state = new
        prev = state[0]
        t += h


def main():
    t0 = 2.0 * math.pi * math.sqrt(L / G)
    rows = []
    for deg in (10, 20, 30, 45, 60, 75, 90, 120, 150):
        th0 = math.radians(deg)
        t_meas = measured_period(th0)
        t_corr = t0 * (1.0 + th0 * th0 / 16.0)
        rows.append((deg, t0, t_corr, t_meas,
                     100.0 * (t_meas - t0) / t0,
                     100.0 * (t_meas - t_corr) / t_meas))

    out = Path(__file__).resolve().parent.parent / "data"
    out.mkdir(exist_ok=True)
    path = out / "pendulum_period.csv"
    with path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["amplitude_deg", "T_small_s", "T_firstcorr_s",
                    "T_measured_s", "smallangle_error_pct",
                    "firstcorr_error_pct"])
        for r in rows:
            w.writerow([r[0]] + [f"{v:.6f}" for v in r[1:]])
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
