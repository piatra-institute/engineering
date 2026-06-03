# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Lung compliance and work-of-breathing from a static P-V curve.

The lung's static pressure-volume curve is sigmoidal. A simple two-
parameter sigmoid (Salazar-Knowles 1964) fits well:

    V(P) = V_max / (1 + exp(-(P - P_50) / k))

Compliance at any point is C(P) = dV/dP. The peak compliance (at the
inflection point P = P_50) is C_max = V_max / (4 k).

Work of breathing per cycle is the hysteresis area between inflation
and deflation limbs. The script computes:
  - C at FRC (functional residual capacity)
  - C_max and the inflection pressure P_50
  - Tidal-volume work for a 500-mL tidal breath at the operating point
  - Work-of-breathing rate at typical rest and exercise rates

References:
  - Salazar and Knowles (1964). An analysis of pressure-volume
    characteristics of the lungs. J. Appl. Physiol. 19, 97--104.
  - West (2012). Respiratory Physiology: The Essentials, 9th ed.

Run: uv run lung_compliance_fit.py
"""
from __future__ import annotations
import math


def V_of_P(P_cmH2O: float, V_max_L: float = 5.5, P_50: float = 10.0, k: float = 5.0) -> float:
    return V_max_L / (1.0 + math.exp(-(P_cmH2O - P_50) / k))


def C_of_P(P_cmH2O: float, V_max_L: float = 5.5, P_50: float = 10.0, k: float = 5.0) -> float:
    """dV/dP, in L per cmH2O."""
    x = (P_cmH2O - P_50) / k
    ex = math.exp(-x)
    return V_max_L * ex / (k * (1.0 + ex) ** 2)


def tidal_work_estimate(P_FRC_cmH2O: float = 5.0, Vt_L: float = 0.5,
                        V_max_L: float = 5.5, P_50: float = 10.0, k: float = 5.0,
                        n_steps: int = 200) -> dict:
    """Compute the work to inflate the lung by Vt above FRC and back."""
    # Start volume
    V0 = V_of_P(P_FRC_cmH2O, V_max_L, P_50, k)
    V1 = V0 + Vt_L
    # Find the pressure that produces V1 by bisection
    lo, hi = -5.0, 40.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if V_of_P(mid, V_max_L, P_50, k) < V1:
            lo = mid
        else:
            hi = mid
    P1 = 0.5 * (lo + hi)
    # Inflation work: integral of P dV from V0 to V1
    dV = (V1 - V0) / n_steps
    W_in = 0.0
    P_prev = P_FRC_cmH2O
    for i in range(1, n_steps + 1):
        V = V0 + i * dV
        # Pressure that holds V (no hysteresis modelled here)
        lo2, hi2 = -5.0, 40.0
        for _ in range(40):
            mid = 0.5 * (lo2 + hi2)
            if V_of_P(mid, V_max_L, P_50, k) < V:
                lo2 = mid
            else:
                hi2 = mid
        P = 0.5 * (lo2 + hi2)
        W_in += 0.5 * (P + P_prev) * dV  # cmH2O * L
        P_prev = P
    # 1 cmH2O * L = 98.066 Pa * 1e-3 m^3 = 0.0981 J
    W_in_J = W_in * 0.0981
    return {
        "P_FRC_cmH2O": P_FRC_cmH2O,
        "P_peak_cmH2O": P1,
        "V_FRC_L": V0,
        "V_peak_L": V1,
        "W_inflate_J": W_in_J,
    }


def main() -> None:
    V_max, P_50, k = 5.5, 10.0, 5.0
    print(f"Sigmoid params: V_max = {V_max} L, P_50 = {P_50} cmH2O, k = {k}")
    print(f"  Peak compliance (at P_50)        = {C_of_P(P_50):.3f} L/cmH2O")
    print(f"  Compliance at FRC (P = 5 cmH2O)  = {C_of_P(5.0):.3f} L/cmH2O")
    print(f"  Compliance at TLC (P = 25 cmH2O) = {C_of_P(25.0):.3f} L/cmH2O")
    print()
    res = tidal_work_estimate(P_FRC_cmH2O=5.0, Vt_L=0.5)
    print("Tidal breath, 500 mL above FRC at P_FRC = 5 cmH2O:")
    for k_, v in res.items():
        print(f"  {k_:>25s} = {v:8.4f}")
    rate_rest = 12.0  # breaths/min
    rate_exercise = 30.0
    W_dot_rest_W = res["W_inflate_J"] * rate_rest / 60.0
    W_dot_ex_W = res["W_inflate_J"] * rate_exercise / 60.0
    print(f"\nWork-of-breathing rate at rest      (12 br/min) = {W_dot_rest_W:.3f} W")
    print(f"Work-of-breathing rate at exercise  (30 br/min) = {W_dot_ex_W:.3f} W")


if __name__ == "__main__":
    main()
