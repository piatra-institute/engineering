"""Air-standard Otto-cycle solver with peak temperature, pressure, and MEP.

Given the compression ratio, the inlet state, and the specific heat input,
compute the four state points, the thermal efficiency, and the mean effective
pressure. Cold-air-standard assumption. Used in section 3.4 and the Otto
exercises. SI units throughout: temperatures in K, pressures in kPa.
"""

from __future__ import annotations

R_AIR = 0.287       # kJ/kg.K
CV_AIR = 0.718      # kJ/kg.K
GAMMA = 1.4


def solve_otto(r, t1, p1, q_in, gamma=GAMMA, cv=CV_AIR, r_gas=R_AIR):
    """Return state temperatures, pressures, efficiency, and MEP.

    r    compression ratio
    t1   inlet temperature (K)
    p1   inlet pressure (kPa)
    q_in specific heat addition (kJ/kg)
    """
    t2 = t1 * r ** (gamma - 1.0)             # isentropic compression
    p2 = p1 * r ** gamma
    t3 = t2 + q_in / cv                       # constant-volume heat addition
    p3 = p2 * t3 / t2
    t4 = t3 * r ** (-(gamma - 1.0))           # isentropic expansion
    p4 = p3 * r ** (-gamma)

    eta = 1.0 - r ** (-(gamma - 1.0))
    w_net = eta * q_in

    v1 = r_gas * t1 / p1                       # specific volume at state 1 (m3/kg if kPa)
    v2 = v1 / r
    mep = w_net / (v1 - v2)                    # kPa

    return {
        "T1": t1, "T2": t2, "T3": t3, "T4": t4,
        "p1": p1, "p2": p2, "p3": p3, "p4": p4,
        "eta": eta, "w_net": w_net, "mep_kPa": mep,
    }


if __name__ == "__main__":
    # Worked example: r = 9, T1 = 300 K, p1 = 100 kPa, q_in = 2000 kJ/kg.
    res = solve_otto(9.0, 300.0, 100.0, 2000.0)
    for k, v in res.items():
        print(f"{k:10s} {v:10.2f}")
