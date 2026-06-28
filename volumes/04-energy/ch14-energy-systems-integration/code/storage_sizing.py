"""Storage sizing for a still-and-cloudy renewable shortfall.

Given a national peak demand, an average-to-peak ratio, and the length
of a low-renewable weather event, the module sizes the energy and power
of the storage needed to ride through, and prices it.

It also computes the round-trip efficiency of a multi-stage storage
chain (e.g. green hydrogen: electrolysis, compression, fuel cell) as
the product of the stage efficiencies.

Usage:
    python storage_sizing.py
"""

from __future__ import annotations

from functools import reduce


def energy_for_event(peak_gw, avg_to_peak, days):
    """Energy (GWh) to serve average load for a multi-day event."""
    avg_gw = peak_gw * avg_to_peak
    return avg_gw * 24.0 * days


def capital_cost(energy_gwh, usd_per_kwh):
    """Capital cost (USD) of the storage energy capacity."""
    return energy_gwh * 1e6 * usd_per_kwh  # GWh -> kWh


def chain_efficiency(stage_efficiencies):
    """Round-trip efficiency of a series chain of stages."""
    return reduce(lambda a, b: a * b, stage_efficiencies, 1.0)


if __name__ == "__main__":
    # UK-scale example, current as of 2024 (order-of-magnitude).
    peak = 45.0          # GW
    e = energy_for_event(peak, avg_to_peak=0.7, days=10)
    cost = capital_cost(e, usd_per_kwh=140.0)
    print(f"energy needed: {e:8.0f} GWh")
    print(f"capital cost : {cost/1e12:6.2f} trillion USD at 140 USD/kWh")

    # Green-hydrogen storage chain round-trip efficiency.
    stages = {
        "electrolysis": 0.65,
        "compression": 0.90,
        "transport/storage": 0.95,
        "fuel cell": 0.55,
    }
    rt = chain_efficiency(stages.values())
    print(f"\nhydrogen chain round-trip efficiency: {rt:5.1%}")
    for name, eff in stages.items():
        print(f"  {name:20s} {eff:5.2f}")
