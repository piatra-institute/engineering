"""Hour-by-hour household solar-plus-battery dispatch.

Reads an hourly profile of household load and rooftop PV generation,
applies a greedy battery dispatch (charge surplus, discharge deficit),
and reports the annual grid-import fraction and self-consumption.

This is the engine behind the chapter project. It is deliberately
simple: a single battery, a flat round-trip efficiency split evenly
between charge and discharge, and no degradation.

Usage:
    python household_dispatch.py ../data/household_load_pv.csv

The CSV has columns: hour, load_kwh, pv_kwh.
"""

from __future__ import annotations

import csv
import sys


def simulate(load, pv, usable_kwh=10.0, eta_rt=0.90, p_max_kw=5.0):
    """Greedy dispatch over equal one-hour steps.

    Returns a dict of annual energy totals (kWh).
    """
    eta_leg = eta_rt ** 0.5  # split round-trip loss between the two legs
    soc = 0.0
    grid_import = 0.0
    grid_export = 0.0
    direct_use = 0.0
    for L, G in zip(load, pv):
        served_directly = min(L, G)
        direct_use += served_directly
        surplus = G - served_directly
        deficit = L - served_directly
        if surplus > 0:  # charge
            room = (usable_kwh - soc) / eta_leg
            charge = min(surplus, room, p_max_kw)
            soc += charge * eta_leg
            grid_export += surplus - charge
        elif deficit > 0:  # discharge
            avail = soc * eta_leg
            discharge = min(deficit, avail, p_max_kw)
            soc -= discharge / eta_leg
            grid_import += deficit - discharge
    total_load = sum(load)
    return {
        "total_load_kwh": total_load,
        "grid_import_kwh": grid_import,
        "grid_export_kwh": grid_export,
        "self_consumption_frac": 1.0 - grid_import / total_load,
        "import_frac": grid_import / total_load,
    }


def main(path: str) -> None:
    load, pv = [], []
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh):
            load.append(float(row["load_kwh"]))
            pv.append(float(row["pv_kwh"]))
    out = simulate(load, pv)
    for k, v in out.items():
        print(f"{k:24s} {v:10.2f}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "../data/household_load_pv.csv")
