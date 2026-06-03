# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Scale-up of k_L a for stirred-tank bioreactors.

Uses the Van't Riet (1979) correlation for water-like media in
agitated, sparged tanks:

    k_L a = c * (P/V)^a * (v_s)^b

with c ~ 0.026, a ~ 0.4, b ~ 0.5 in SI units (k_L a in s^-1,
P/V in W/m^3, v_s in m/s).

Walks a scale-up from a 10 L development reactor at known operating
point to a 10000 L production reactor under three rules:

1. Constant geometry (vessel shape preserved; impeller speed scaled
   to hold geometric similarity, P/V drops).
2. Constant power-per-volume P/V.
3. Constant k_L a.

Reports the impeller-power, gas-flow, and k_L a at each scale.

Run: uv run kla_scale_up.py
"""
from __future__ import annotations
import math


C_VANTRIET = 0.026
A_EXP = 0.4
B_EXP = 0.5


def kla(pv: float, vs: float) -> float:
    """k_L a in s^-1 from P/V (W/m^3) and superficial gas velocity (m/s)."""
    return C_VANTRIET * pv**A_EXP * vs**B_EXP


def kla_per_hour(pv: float, vs: float) -> float:
    return kla(pv, vs) * 3600.0


def scale_up(V_dev_L: float, V_prod_L: float, pv_dev: float, vs_dev: float) -> None:
    print(f"\nScale-up from {V_dev_L:.0f} L to {V_prod_L:.0f} L")
    print(f"  Development point: P/V = {pv_dev:.0f} W/m^3, v_s = {vs_dev:.3f} m/s")
    kla_dev = kla_per_hour(pv_dev, vs_dev)
    print(f"  k_L a (dev)      = {kla_dev:.1f} h^-1")
    factor = V_prod_L / V_dev_L

    # Rule 1: constant geometry => power per volume falls as factor^(-2/3)
    pv_geom = pv_dev * factor ** (-2.0 / 3.0)
    vs_geom = vs_dev
    kla_geom = kla_per_hour(pv_geom, vs_geom)
    print("\n  [Rule 1] Constant geometric similarity:")
    print(f"    P/V (prod) = {pv_geom:.1f} W/m^3   (factor x{pv_geom/pv_dev:.3f})")
    print(f"    k_L a      = {kla_geom:.1f} h^-1   (factor x{kla_geom/kla_dev:.3f})")

    # Rule 2: constant P/V
    pv_pv = pv_dev
    kla_pv = kla_per_hour(pv_pv, vs_dev)
    print("\n  [Rule 2] Constant power per volume:")
    print(f"    P/V (prod) = {pv_pv:.0f} W/m^3")
    print(f"    k_L a      = {kla_pv:.1f} h^-1   (factor x{kla_pv/kla_dev:.3f})")

    # Rule 3: constant k_L a, holding v_s, solve for P/V
    pv_const_kla = (kla_dev / 3600.0 / (C_VANTRIET * vs_dev**B_EXP)) ** (1.0 / A_EXP)
    kla_const = kla_per_hour(pv_const_kla, vs_dev)
    print("\n  [Rule 3] Constant k_L a (v_s held fixed):")
    print(f"    P/V (prod) = {pv_const_kla:.0f} W/m^3   (factor x{pv_const_kla/pv_dev:.3f})")
    print(f"    k_L a      = {kla_const:.1f} h^-1")

    V_prod_m3 = V_prod_L * 1e-3
    P_const_kla = pv_const_kla * V_prod_m3
    print(f"    Impeller power required: {P_const_kla:.0f} W  ({P_const_kla/1000:.1f} kW)")


def main() -> None:
    print("k_L a scale-up using Van't Riet (1979) correlation")
    print(f"  k_L a = {C_VANTRIET} * (P/V)^{A_EXP} * v_s^{B_EXP}   (SI units)")
    # Development reactor: 10 L, 1000 W/m^3, v_s = 0.005 m/s (~0.5 vvm)
    scale_up(V_dev_L=10.0, V_prod_L=1000.0,
             pv_dev=1000.0, vs_dev=0.005)
    scale_up(V_dev_L=10.0, V_prod_L=10000.0,
             pv_dev=1000.0, vs_dev=0.005)


if __name__ == "__main__":
    main()
