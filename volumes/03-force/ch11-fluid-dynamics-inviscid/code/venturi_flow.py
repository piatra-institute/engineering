"""Venturi-meter flow-rate calculation from a measured pressure differential.

Bernoulli + continuity for an incompressible inviscid pipe contraction:

    u1 = sqrt( 2 (p1 - p2) / (rho * ((A1/A2)^2 - 1)) )
    Q  = Cd * A1 * u1

The discharge coefficient Cd (about 0.97 for a machined Venturi) folds in
the small real-fluid losses the inviscid analysis omits.

Run:  uv run venturi_flow.py
"""

from __future__ import annotations

import csv
import math
from pathlib import Path


def venturi_flow(d1: float, d2: float, dp: float, rho: float, cd: float) -> dict:
    """Return throat speed, inlet speed, and volume flow rate.

    d1, d2 : inlet and throat diameters (m)
    dp     : measured static pressure difference p1 - p2 (Pa)
    rho    : fluid density (kg/m^3)
    cd     : discharge coefficient (dimensionless)
    """
    a1 = math.pi * (d1 / 2.0) ** 2
    a2 = math.pi * (d2 / 2.0) ** 2
    beta = a1 / a2
    u1 = math.sqrt(2.0 * dp / (rho * (beta**2 - 1.0)))
    q_ideal = a1 * u1
    q = cd * q_ideal
    return {
        "A1": a1,
        "A2": a2,
        "u1": u1,
        "u2": u1 * beta,
        "Q_ideal_Ls": 1000.0 * q_ideal,
        "Q_Ls": 1000.0 * q,
    }


def main() -> None:
    rho = 1000.0  # water, kg/m^3
    cd = 0.97
    d1, d2 = 0.100, 0.040  # 100 mm inlet, 40 mm throat
    # Sweep a range of differential pressures and write a calibration table.
    out = Path(__file__).resolve().parent.parent / "data" / "venturi_calibration.csv"
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["dp_kPa", "u1_m_s", "u2_m_s", "Q_Ls"])
        for dp_kpa in range(2, 51, 2):
            r = venturi_flow(d1, d2, dp_kpa * 1000.0, rho, cd)
            w.writerow(
                [dp_kpa, round(r["u1"], 4), round(r["u2"], 4), round(r["Q_Ls"], 3)]
            )

    # Headline case from the chapter exercise: 30 kPa differential.
    r = venturi_flow(d1, d2, 30_000.0, rho, cd)
    print(f"Inlet speed u1 = {r['u1']:.3f} m/s")
    print(f"Throat speed u2 = {r['u2']:.3f} m/s")
    print(f"Flow rate Q = {r['Q_Ls']:.2f} L/s  (ideal {r['Q_ideal_Ls']:.2f} L/s)")
    print(f"Wrote {out.name}")


if __name__ == "__main__":
    main()
