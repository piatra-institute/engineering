"""Reduce raw Pitot-tube readings to a velocity field downstream of a fan.

The probe constant K relates measured differential pressure to true speed:

    u = K sqrt( 2 dp / rho ).

K is found by least squares against a set of reference (known-speed) points.
The script then applies K to a grid of fan-survey readings and integrates the
axial velocity profile to recover the volume flow rate

    Q = integral u(r) 2 pi r dr   (axisymmetric, trapezoidal).

This is the data-reduction backbone of the chapter project.

Run:  uv run pitot_calibration.py
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

RHO_AIR = 1.20  # kg/m^3 at room conditions


def fit_K(dp_ref, u_ref) -> float:
    """Least-squares K for u = K sqrt(2 dp / rho), forced through origin."""
    x = [math.sqrt(2.0 * dp / RHO_AIR) for dp in dp_ref]
    num = sum(xi * ui for xi, ui in zip(x, u_ref))
    den = sum(xi * xi for xi in x)
    return num / den


def velocity(dp: float, k: float) -> float:
    return k * math.sqrt(2.0 * dp / RHO_AIR)


def flow_rate(r, u) -> float:
    """Axisymmetric trapezoidal integration of Q = int u 2 pi r dr."""
    q = 0.0
    for i in range(len(r) - 1):
        r0, r1 = r[i], r[i + 1]
        f0 = u[i] * 2.0 * math.pi * r0
        f1 = u[i + 1] * 2.0 * math.pi * r1
        q += 0.5 * (f0 + f1) * (r1 - r0)
    return q


def main() -> None:
    # Reference calibration points (dp in Pa, known speed in m/s).
    dp_ref = [12.0, 28.0, 52.0, 80.0, 115.0]
    u_ref = [4.5, 6.8, 9.3, 11.5, 13.8]
    k = fit_K(dp_ref, u_ref)
    print(f"Fitted probe constant K = {k:.3f}")

    # A radial survey one fan-diameter downstream (r in m, dp in Pa).
    r = [0.00, 0.02, 0.04, 0.06, 0.08, 0.10]
    dp = [18.0, 42.0, 55.0, 40.0, 16.0, 2.0]  # hub defect, peak, falloff
    u = [velocity(d, k) for d in dp]
    q = flow_rate(r, u)
    print("r (m)   u (m/s)")
    for ri, ui in zip(r, u):
        print(f"{ri:5.2f}   {ui:6.2f}")
    print(f"Volume flow rate Q = {q:.4f} m^3/s = {q*3600:.1f} m^3/h")

    out = Path(__file__).resolve().parent.parent / "data" / "pitot_fan_survey.csv"
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["r_m", "dp_Pa", "u_m_s"])
        for ri, di, ui in zip(r, dp, u):
            w.writerow([ri, di, round(ui, 3)])
    print(f"Wrote {out.name}")


if __name__ == "__main__":
    main()
