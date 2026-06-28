#!/usr/bin/env python3
"""Compare ideal-gas and van der Waals predictions for a gas.

Given temperature and molar volume, return pressure by the ideal-gas law
and by the van der Waals equation, and report the percent departure. The
van der Waals constants default to nitrogen.

    p_ideal = R T / v_m
    p_vdw   = R T / (v_m - b) - a / v_m**2

The departure is a quick proxy for the compressibility factor Z, which is
tabulated against reduced pressure and temperature in the generalised
chart of the chapter.
"""

R = 8.314  # J/(mol K), universal gas constant

# van der Waals constants for a few gases: (a [Pa m^6/mol^2], b [m^3/mol])
VDW = {
    "N2": (0.137, 3.87e-5),
    "CO2": (0.364, 4.27e-5),
    "CH4": (0.228, 4.28e-5),
    "H2O": (0.5536, 3.049e-5),
}


def p_ideal(T, v_m):
    return R * T / v_m


def p_vdw(T, v_m, a, b):
    return R * T / (v_m - b) - a / v_m**2


def compressibility(T, v_m, gas="N2"):
    a, b = VDW[gas]
    p = p_vdw(T, v_m, a, b)
    return p * v_m / (R * T)


def report(T, v_m, gas="N2"):
    a, b = VDW[gas]
    pi = p_ideal(T, v_m)
    pv = p_vdw(T, v_m, a, b)
    z = pv * v_m / (R * T)
    err = 100.0 * (pi - pv) / pv
    print(f"{gas}: T={T} K, v_m={v_m:.3e} m^3/mol")
    print(f"  p_ideal = {pi/1e6:8.4f} MPa")
    print(f"  p_vdw   = {pv/1e6:8.4f} MPa")
    print(f"  Z       = {z:6.4f}")
    print(f"  ideal-gas error in p = {err:+.2f} %")


if __name__ == "__main__":
    # nitrogen near room temperature, moderate density
    report(300.0, 5.0e-4, "N2")
    # carbon dioxide approaching its critical region
    report(320.0, 1.0e-4, "CO2")
