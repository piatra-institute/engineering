"""Carnot cycle on a p-V diagram for an ideal gas.

Two isothermal segments (at T_h and T_c) and two reversible adiabatic
segments. The script computes the four state points, the heat and work of
each leg, the net work, and the thermal efficiency, then confirms the
efficiency equals the Carnot bound 1 - T_c / T_h.

Sign convention (matches the chapter): work positive when done ON the gas,
so the work done BY the gas over a cycle is the negative of the cycle's W.

Run:
    python carnot_cycle.py
"""

import numpy as np

R = 8.314  # J / (mol K)


def carnot(n=1.0, T_h=600.0, T_c=300.0, V1=1.0e-3, V2=2.0e-3, gamma=1.4):
    """Return state points and per-leg energetics for one mole-cycle.

    States: 1 -> 2 isothermal expansion at T_h (V1 -> V2),
            2 -> 3 adiabatic expansion (T_h -> T_c),
            3 -> 4 isothermal compression at T_c,
            4 -> 1 adiabatic compression (T_c -> T_h).
    """
    # adiabatic relation T V^(gamma-1) = const fixes V3 and V4
    V3 = V2 * (T_h / T_c) ** (1.0 / (gamma - 1.0))
    V4 = V1 * (T_h / T_c) ** (1.0 / (gamma - 1.0))

    # heat absorbed in isothermal expansion at T_h (Q in, by the gas)
    Q_h = n * R * T_h * np.log(V2 / V1)
    # heat rejected in isothermal compression at T_c (negative, by the gas)
    Q_c = n * R * T_c * np.log(V4 / V3)  # V4 < V3, so this is negative

    W_by_gas = Q_h + Q_c  # first law over the cycle: net work done by the gas
    eta = W_by_gas / Q_h
    eta_carnot = 1.0 - T_c / T_h

    return {
        "V": (V1, V2, V3, V4),
        "Q_h": Q_h,
        "Q_c": Q_c,
        "W_by_gas": W_by_gas,
        "eta": eta,
        "eta_carnot": eta_carnot,
    }


if __name__ == "__main__":
    res = carnot()
    print(f"Q_h           = {res['Q_h']:8.2f} J  (absorbed at T_h)")
    print(f"Q_c           = {res['Q_c']:8.2f} J  (rejected at T_c)")
    print(f"net work      = {res['W_by_gas']:8.2f} J  (done by the gas)")
    print(f"efficiency    = {res['eta']:8.4f}")
    print(f"Carnot bound  = {res['eta_carnot']:8.4f}")
    assert abs(res["eta"] - res["eta_carnot"]) < 1e-9, "efficiency must equal bound"
    print("efficiency matches the Carnot bound to machine precision.")
