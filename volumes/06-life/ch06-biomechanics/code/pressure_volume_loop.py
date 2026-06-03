# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Left-ventricular pressure-volume loop, simple analytic model.

The PV loop is parameterised by:
  - V0 (zero-pressure volume, ~ 20 mL)
  - Ees (end-systolic elastance, ~ 2 mmHg/mL)
  - alpha, beta (passive end-diastolic pressure-volume curve)
  - EDV (end-diastolic volume, ~ 120 mL)
  - ESV (end-systolic volume, ~ 50 mL)
  - P_aortic_dia, P_aortic_sys (aortic diastolic and systolic pressure)

The four phases are computed analytically. Stroke volume, stroke work,
ejection fraction, and cardiac output are reported.

References:
  - Suga and Sagawa (1974). Instantaneous pressure-volume relationships.
    Circ. Res. 35, 117--126.
  - Klabunde (2011). Cardiovascular Physiology Concepts, 2nd ed.

Run: uv run pressure_volume_loop.py
"""
from __future__ import annotations
import math


def edpvr(V_mL: float, V0: float = 5.0, alpha: float = 0.005, beta: float = 2.0) -> float:
    """End-diastolic pressure-volume relation. Returns mmHg."""
    if V_mL <= V0:
        return 0.0
    return alpha * (V_mL - V0) ** beta


def espvr(V_mL: float, V0_es: float = 20.0, Ees: float = 2.0) -> float:
    """End-systolic pressure-volume relation. Returns mmHg."""
    if V_mL <= V0_es:
        return 0.0
    return Ees * (V_mL - V0_es)


def loop_summary(EDV: float = 120.0, ESV: float = 50.0,
                 P_aortic_dia: float = 80.0, P_aortic_sys: float = 120.0,
                 heart_rate_bpm: float = 70.0) -> None:
    SV = EDV - ESV
    EF = SV / EDV
    CO_mLmin = SV * heart_rate_bpm
    # Mean ejection pressure (rough): average aortic during ejection
    P_mean_ejection = 0.5 * (P_aortic_dia + P_aortic_sys)
    # Stroke work: integral of P dV around the loop. Approximate as
    # rectangle for ejection plus triangles for iso phases.
    # rectangle: SV * P_mean_ejection
    # mmHg * mL conversion: 1 mmHg * 1 mL = 133.322 Pa * 1e-6 m^3 = 1.333e-4 J
    SW_mmHg_mL = SV * P_mean_ejection
    SW_J = SW_mmHg_mL * 133.322e-6
    cardiac_power_W = SW_J * heart_rate_bpm / 60.0
    P_ed = edpvr(EDV)
    P_es = espvr(ESV)
    print("=== Left-ventricular PV-loop summary ===")
    print(f"  EDV                       = {EDV:6.1f} mL")
    print(f"  ESV                       = {ESV:6.1f} mL")
    print(f"  Stroke volume             = {SV:6.1f} mL")
    print(f"  Ejection fraction         = {EF*100:6.1f} %")
    print(f"  End-diastolic pressure    = {P_ed:6.1f} mmHg")
    print(f"  End-systolic pressure     = {P_es:6.1f} mmHg")
    print(f"  Mean ejection pressure    = {P_mean_ejection:6.1f} mmHg")
    print(f"  Stroke work               = {SW_J:6.3f} J/beat")
    print(f"  Heart rate                = {heart_rate_bpm:6.1f} bpm")
    print(f"  Cardiac output            = {CO_mLmin/1000:6.2f} L/min")
    print(f"  Cardiac power             = {cardiac_power_W:6.2f} W")


def exercise_versus_rest() -> None:
    print("\n--- Rest ---")
    loop_summary(EDV=120, ESV=50, P_aortic_dia=80, P_aortic_sys=120, heart_rate_bpm=70)
    print("\n--- Heavy exercise (sympathetic activation, increased venous return) ---")
    loop_summary(EDV=145, ESV=40, P_aortic_dia=85, P_aortic_sys=180, heart_rate_bpm=170)
    print("\n--- Heart failure with reduced ejection fraction ---")
    loop_summary(EDV=180, ESV=120, P_aortic_dia=70, P_aortic_sys=100, heart_rate_bpm=85)


def main() -> None:
    exercise_versus_rest()


if __name__ == "__main__":
    main()
