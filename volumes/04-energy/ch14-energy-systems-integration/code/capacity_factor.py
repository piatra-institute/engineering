"""Capacity factor and annual energy from a generation time series.

Capacity factor is the ratio of energy actually produced to the energy
a plant would produce running at rated power for the whole period:

    CF = E_actual / (P_rated * hours)

The module computes CF either from a measured hourly output series or
directly from a rated power and an annual energy figure, and inverts to
size a plant for a target annual energy.

Usage:
    python capacity_factor.py ../data/generation_mix.csv
"""

from __future__ import annotations

import csv
import sys


def cf_from_series(hourly_kw, p_rated_kw):
    """Capacity factor from an hourly output series (kW per hour-step)."""
    hours = len(hourly_kw)
    e_actual = sum(hourly_kw)  # kW * 1 h = kWh
    e_rated = p_rated_kw * hours
    return e_actual / e_rated


def annual_energy(p_rated_mw, cf):
    """Annual energy in MWh for a rated power and capacity factor."""
    return p_rated_mw * cf * 8760.0


def size_for_energy(target_mwh_yr, cf):
    """Rated power (MW) needed to deliver a target annual energy."""
    return target_mwh_yr / (cf * 8760.0)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "../data/generation_mix.csv"
    with open(path, newline="") as fh:
        rows = list(csv.DictReader(fh))
    print("technology         CF      annual energy (TWh, 1 GW rated)")
    for r in rows:
        cf = float(r["capacity_factor"])
        twh = annual_energy(1000.0, cf) / 1e6  # 1 GW = 1000 MW; MWh -> TWh
        print(f"{r['technology']:18s} {cf:5.2f}   {twh:6.2f}")
    # Example inversion: size wind to match a 1 GW nuclear plant's energy.
    nuke = annual_energy(1000.0, 0.92)
    print(f"\nwind MW to match 1 GW nuclear: {size_for_energy(nuke, 0.35):7.0f} MW")
