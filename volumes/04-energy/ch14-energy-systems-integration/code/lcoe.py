"""Levelized cost of energy (LCOE).

LCOE is the constant per-unit electricity price that makes the
discounted revenue equal the discounted lifetime cost of a generator.
It is the standard first-order comparison of generation technologies.

    LCOE = (sum_t (C_t / (1+r)^t)) / (sum_t (E_t / (1+r)^t))

with C_t the cost in year t (capital, fixed O&M, fuel, variable O&M)
and E_t the energy produced in year t. Capital is charged in year 0.

Run:
    python lcoe.py
"""

from __future__ import annotations


def lcoe(
    capex_per_kw: float,
    fixed_om_per_kw_yr: float,
    var_om_per_mwh: float,
    fuel_per_mwh: float,
    capacity_factor: float,
    lifetime_yr: int,
    discount_rate: float,
) -> float:
    """LCOE in USD/MWh for a 1 kW reference plant.

    capacity_factor is a fraction in [0, 1]; fuel_per_mwh already folds
    in the heat rate and fuel price (set to 0 for wind/solar).
    """
    energy_mwh_per_yr = 1.0 * capacity_factor * 8760.0 / 1000.0  # 1 kW -> MWh
    pv_cost = capex_per_kw  # charged at t = 0
    pv_energy = 0.0
    for t in range(1, lifetime_yr + 1):
        discount = (1.0 + discount_rate) ** t
        annual_cost = (
            fixed_om_per_kw_yr
            + energy_mwh_per_yr * (var_om_per_mwh + fuel_per_mwh)
        )
        pv_cost += annual_cost / discount
        pv_energy += energy_mwh_per_yr / discount
    return pv_cost / pv_energy


if __name__ == "__main__":
    # Representative inputs, current as of 2024 (order-of-magnitude).
    techs = {
        "solar PV (utility)": dict(
            capex_per_kw=900, fixed_om_per_kw_yr=15, var_om_per_mwh=0,
            fuel_per_mwh=0, capacity_factor=0.18, lifetime_yr=30,
        ),
        "wind onshore": dict(
            capex_per_kw=1300, fixed_om_per_kw_yr=40, var_om_per_mwh=0,
            fuel_per_mwh=0, capacity_factor=0.35, lifetime_yr=25,
        ),
        "gas combined-cycle": dict(
            capex_per_kw=1100, fixed_om_per_kw_yr=25, var_om_per_mwh=2,
            fuel_per_mwh=45, capacity_factor=0.55, lifetime_yr=30,
        ),
        "nuclear (new)": dict(
            capex_per_kw=8000, fixed_om_per_kw_yr=130, var_om_per_mwh=3,
            fuel_per_mwh=8, capacity_factor=0.92, lifetime_yr=40,
        ),
    }
    r = 0.07
    for name, kw in techs.items():
        print(f"{name:24s}  {lcoe(discount_rate=r, **kw):6.1f} USD/MWh")
