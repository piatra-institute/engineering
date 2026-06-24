"""Draining a tank under Torricelli's law: the unsteady free-surface problem.

The instantaneous efflux speed is u = sqrt(2 g h), but as the tank drains the
head h falls, so the drain time needs an integration. With surface area A_s and
orifice area A_o (discharge coefficient Cd), volume conservation gives

    A_s dh/dt = - Cd A_o sqrt(2 g h),

whose closed-form solution from h0 to 0 is

    t_drain = (A_s / (Cd A_o)) * sqrt(2 h0 / g).

This script integrates the ODE numerically (explicit Euler) and compares to the
closed form, then writes the depth history to a CSV.

Run:  uv run tank_drain.py
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

G = 9.81


def closed_form(a_s: float, a_o: float, cd: float, h0: float) -> float:
    return (a_s / (cd * a_o)) * math.sqrt(2.0 * h0 / G)


def integrate(a_s: float, a_o: float, cd: float, h0: float, dt: float):
    """Explicit-Euler depth history; returns list of (t, h)."""
    t, h = 0.0, h0
    hist = [(t, h)]
    while h > 1e-4:
        dhdt = -cd * a_o * math.sqrt(2.0 * G * h) / a_s
        h = max(0.0, h + dt * dhdt)
        t += dt
        hist.append((t, h))
    return hist


def main() -> None:
    # Swimming pool: 25 m x 10 m surface, 2 m deep, 100 mm outlet.
    a_s = 25.0 * 10.0
    a_o = math.pi * (0.050) ** 2  # 100 mm diameter
    cd = 0.62
    h0 = 2.0

    t_cf = closed_form(a_s, a_o, cd, h0)
    hist = integrate(a_s, a_o, cd, h0, dt=5.0)
    t_num = hist[-1][0]

    print(f"Closed-form drain time : {t_cf/3600:.2f} h ({t_cf:.0f} s)")
    print(f"Numerical drain time   : {t_num/3600:.2f} h ({t_num:.0f} s)")

    out = Path(__file__).resolve().parent.parent / "data" / "tank_drain_history.csv"
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["t_s", "h_m", "u_efflux_m_s"])
        for t, h in hist[:: max(1, len(hist) // 60)]:
            w.writerow([round(t, 1), round(h, 4), round(math.sqrt(2 * G * h), 4)])
    print(f"Wrote {out.name}")


if __name__ == "__main__":
    main()
