"""Power-factor correction sizing for a single-phase inductive load.

Given a real power, an RMS line voltage, a line frequency, and an initial
lagging power factor, compute the reactive power and the parallel capacitance
needed to raise the power factor to a target value. The arithmetic is the
working basis of every industrial capacitor-bank specification.

Units: watts, volts (RMS), hertz, farads.
"""

from __future__ import annotations

import math


def correction_capacitance(P, V_rms, f, pf_initial, pf_target):
    """Return (Q_initial, Q_target, C) for parallel power-factor correction."""
    phi1 = math.acos(pf_initial)
    phi2 = math.acos(pf_target)
    Q1 = P * math.tan(phi1)
    Q2 = P * math.tan(phi2)
    Qc = Q1 - Q2                       # reactive power the capacitor must supply
    C = Qc / (2.0 * math.pi * f * V_rms ** 2)
    return Q1, Q2, C, Qc


if __name__ == "__main__":
    # Motor: 50 A at 230 V, pf 0.75 lagging, 50 Hz; correct to 0.95.
    V = 230.0
    I = 50.0
    pf1 = 0.75
    P = V * I * pf1
    Q1, Q2, C, Qc = correction_capacitance(P, V, 50.0, pf1, 0.95)
    print(f"P = {P:.0f} W, S = {V * I:.0f} VA")
    print(f"Q_initial = {Q1:.0f} VAR, Q_target = {Q2:.0f} VAR")
    print(f"capacitor must supply {Qc:.0f} VAR, C = {C * 1e6:.1f} uF")
