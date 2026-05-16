"""Model triangulation: four routes to UK personal-transport energy.

Computes each of the four routes from figure 18.5, propagates each
route's within-route uncertainty, and reports the across-route spread
as the lower bound on the structural uncertainty (section 18.5).

Numbers are from the MacKay 2009 chapter on personal transport,
current as of 2008-09.

Dependencies: numpy.

Run:
    python model_triangulation.py
"""
from __future__ import annotations

import numpy as np


def route1_vkm_intensity():
    """Vehicle-km / yr * energy intensity (cars only)."""
    D = 13_500.0    # km / yr per person
    eta = 0.80      # kWh / km, petrol car
    sigma_rel = 0.20
    E = D * eta
    return E, E * sigma_rel


def route2_fuel_population():
    """Total petrol sales / population."""
    F = 44e9        # L petrol-equivalent / yr (UK transport, illustrative)
    e_L = 9.7       # kWh / L
    N = 61e6        # UK residents
    sigma_rel = 0.05
    E = F * e_L / N
    return E, E * sigma_rel


def route3_time_power():
    """Time-use budget * average mechanical power per car / occupants."""
    t = 1.1 * 365   # hours per year in cars
    P = 15.0        # kW average mechanical (with engine losses)
    occ = 4.0       # occupant correction (drivers averaged across all riders)
    sigma_rel = 0.30
    E = t * P / occ
    return E, E * sigma_rel


def route4_emissions():
    """Transport CO2 emissions / carbon intensity of fuel / population."""
    M = 130e9       # kg CO2 / yr from UK road transport (illustrative)
    I_CO2 = 0.25    # kg CO2 / kWh for petrol
    N = 61e6
    sigma_rel = 0.15
    E = M / I_CO2 / N
    return E, E * sigma_rel


def main() -> None:
    routes = [
        ("R1: vehicle-km x energy intensity", route1_vkm_intensity),
        ("R2: fuel sales / population", route2_fuel_population),
        ("R3: travel-time x power", route3_time_power),
        ("R4: CO2 / carbon intensity", route4_emissions),
    ]
    print("UK personal-transport energy per resident, current as of 2008-09")
    print("(four independent computation routes, after MacKay 2009)\n")
    values = []
    uncerts = []
    for label, fn in routes:
        E, s = fn()
        print(f"  {label:40s}  {E:6.0f} +/- {s:5.0f}  kWh/yr")
        values.append(E)
        uncerts.append(s)
    values = np.array(values)
    uncerts = np.array(uncerts)
    print(f"\n  Across-route mean:        {values.mean():.0f} kWh/yr")
    print(f"  Across-route std dev:     {values.std(ddof=1):.0f} kWh/yr")
    print(f"  Across-route range:       [{values.min():.0f}, {values.max():.0f}] kWh/yr")
    print(f"  Tightest within-route SE: {uncerts.min():.0f} kWh/yr")
    print(f"\nReading: the across-route spread is "
          f"{values.std(ddof=1) / uncerts.min():.1f}x the tightest within-route SE.")
    print("A single-route estimate that reports only the within-route interval understates")
    print("the modelling uncertainty by approximately that factor.")


if __name__ == "__main__":
    main()
