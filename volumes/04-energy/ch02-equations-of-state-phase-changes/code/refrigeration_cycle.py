#!/usr/bin/env python3
"""Vapour-compression refrigeration cycle from four state enthalpies.

Given the four cycle-state enthalpies (and the inlet/outlet for the
compressor), compute the specific cooling capacity, the specific
compressor work, the condenser duty, and the coefficient of performance,
then compare to the Carnot bound for the measured evaporator and
condenser temperatures.

The four states follow the worked R-134a example:
  1  saturated vapour at the evaporator pressure
  2  superheated vapour after isentropic compression
  3  saturated liquid at the condenser pressure
  4  two-phase after isenthalpic throttling (h4 = h3)
"""


def cycle_metrics(h1, h2, h3, T_evap_K, T_cond_K):
    h4 = h3  # throttling is isenthalpic
    q_L = h1 - h4          # evaporator duty, cooling capacity
    w_c = h2 - h1          # compressor work
    q_H = h2 - h3          # condenser duty
    cop = q_L / w_c
    cop_carnot = T_evap_K / (T_cond_K - T_evap_K)
    return {
        "q_L": q_L,
        "w_c": w_c,
        "q_H": q_H,
        "COP": cop,
        "COP_Carnot": cop_carnot,
        "fraction_of_Carnot": cop / cop_carnot,
    }


if __name__ == "__main__":
    # R-134a worked example: h in kJ/kg
    m = cycle_metrics(h1=235.3, h2=277.0, h3=107.3,
                      T_evap_K=253.15, T_cond_K=313.15)
    for k, v in m.items():
        print(f"{k:18s} = {v:7.3f}")
    mdot = 0.05  # kg/s
    print(f"cooling power  = {mdot*m['q_L']:.2f} kW")
    print(f"compressor power = {mdot*m['w_c']:.2f} kW")
