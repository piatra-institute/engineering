"""Power-factor correction by parallel capacitance.

A load draws apparent power S at power factor cos(phi) lagging from a
supply at line-to-line voltage V_LL and frequency f. This script
computes the real power P, the reactive power Q, the capacitance needed
to raise the power factor to a target value, and the resulting drop in
apparent power and supply current. It tabulates the result for a range
of target power factors, producing the data used in section 3.4.

The model uses the peak/RMS-agnostic apparent-power identity

    S = P + i Q,    P = S cos(phi),    Q = S sin(phi),

and the capacitor reactive-power relation Q_C = omega C V_LL**2 for a
delta-connected three-phase bank across the line-to-line voltage.

Usage:
    uv run --with numpy power_factor_correction.py

Dependencies: numpy.
"""

from __future__ import annotations

import math


def correction_capacitance(
    apparent_kva: float,
    pf_initial: float,
    pf_target: float,
    v_ll: float,
    freq_hz: float,
) -> dict[str, float]:
    """Return the power-factor-correction quantities for one target."""
    s0 = apparent_kva * 1.0e3
    p = s0 * pf_initial
    phi0 = math.acos(pf_initial)
    q0 = s0 * math.sin(phi0)
    phi1 = math.acos(pf_target)
    q1 = p * math.tan(phi1)
    delta_q = q0 - q1
    omega = 2.0 * math.pi * freq_hz
    cap_total = delta_q / (omega * v_ll ** 2)  # delta-connected total
    s1 = p / pf_target
    return {
        "P_kW": p / 1.0e3,
        "Q0_kvar": q0 / 1.0e3,
        "Q1_kvar": q1 / 1.0e3,
        "deltaQ_kvar": delta_q / 1.0e3,
        "C_uF_total": cap_total * 1.0e6,
        "S1_kVA": s1 / 1.0e3,
        "current_reduction_pct": 100.0 * (1.0 - s1 / s0),
    }


def main() -> None:
    # Section 3.4 estimation: 30 kVA, pf 0.78, 400 V LL, 50 Hz.
    base = dict(apparent_kva=30.0, pf_initial=0.78, v_ll=400.0, freq_hz=50.0)
    print("target_pf, P_kW, Q0_kvar, Q1_kvar, deltaQ_kvar, "
          "C_uF_total, S1_kVA, current_reduction_pct")
    for pf_target in [0.85, 0.90, 0.92, 0.95, 0.98, 1.00 - 1e-6]:
        r = correction_capacitance(pf_target=pf_target, **base)
        print(f"{pf_target:.3f}, {r['P_kW']:.2f}, {r['Q0_kvar']:.2f}, "
              f"{r['Q1_kvar']:.2f}, {r['deltaQ_kvar']:.2f}, "
              f"{r['C_uF_total']:.1f}, {r['S1_kVA']:.2f}, "
              f"{r['current_reduction_pct']:.2f}")


if __name__ == "__main__":
    main()
