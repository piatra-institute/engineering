"""Vapour-compression refrigeration COP from tabulated refrigerant enthalpies.

Rather than embed a full property library, this module takes the four state
enthalpies (read from a refrigerant table or CoolProp) and returns the cooling
and heating coefficients of performance plus the per-kilogram heat and work
quantities. The default example matches the worked R-134a case of section 3.5.
Enthalpies in kJ/kg. Used in section 3.5 and the refrigeration exercises.
"""

from __future__ import annotations


def vc_performance(h1, h2, h3):
    """Return COP and per-kilogram quantities for the ideal cycle.

    h1 saturated-vapour enthalpy at evaporator exit (compressor inlet)
    h2 superheated-vapour enthalpy after isentropic compression
    h3 saturated-liquid enthalpy at condenser exit (h4 = h3 by throttling)
    """
    h4 = h3                                   # isenthalpic throttle
    q_c = h1 - h4                             # cooling effect
    w_c = h2 - h1                             # compressor work
    q_h = h2 - h3                             # heat rejected
    cop_cool = q_c / w_c
    cop_heat = q_h / w_c
    return {
        "q_c": q_c, "w_c": w_c, "q_h": q_h,
        "cop_cool": cop_cool, "cop_heat": cop_heat,
        "check_cop_heat_minus_cool": cop_heat - cop_cool,  # equals 1.0
    }


if __name__ == "__main__":
    # R-134a worked example, evaporator -10 C, condenser 40 C, ideal cycle.
    # Representative table enthalpies (kJ/kg):
    #   h1 sat. vapour at -10 C  ~ 392.4
    #   h2 after isentropic compression to 40 C condenser ~ 425.6
    #   h3 sat. liquid at 40 C   ~ 256.4
    res = vc_performance(392.4, 425.6, 256.4)
    for k, v in res.items():
        print(f"{k:28s} {v:8.3f}")
