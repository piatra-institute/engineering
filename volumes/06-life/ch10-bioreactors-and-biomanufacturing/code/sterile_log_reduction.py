# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Sterile-process log-reduction calculator.

Kinetics:

    N(t) = N_0 * 10**(-t / D)
    t_nD = n * D

The decimal reduction time D varies with temperature via the z value:

    log10(D2 / D1) = -(T2 - T1) / z

so D at a candidate temperature follows from a reference D at a
reference temperature.

The standard reference is moist-heat sterilisation of Bacillus subtilis
or Geobacillus stearothermophilus spores at 121 degC; D_121 is
0.5 - 2.5 min for typical strains and z is 10 degC.

Run: uv run sterile_log_reduction.py
"""
from __future__ import annotations
import math


def D_at_temperature(D_ref: float, T_ref: float, T_target: float, z: float) -> float:
    """Decimal reduction time at T_target given D at T_ref."""
    return D_ref * 10.0 ** (-(T_target - T_ref) / z)


def time_for_n_log(D: float, n: float) -> float:
    return n * D


def cold_spot_factor(T_cold_C: float, T_set_C: float, z: float = 10.0) -> float:
    """Factor by which cold-spot sterilisation time exceeds setpoint time.

    A cold spot at T_cold sees D_cold = D_set * 10**((T_set - T_cold)/z).
    The hold time needed to deliver the same n-log reduction at the
    cold spot, relative to the setpoint, is exactly the ratio
    D_cold / D_set = 10**((T_set - T_cold)/z).
    """
    return 10.0 ** ((T_set_C - T_cold_C) / z)


def main() -> None:
    print("--- B. subtilis spores, moist heat, 121 degC ---")
    D_121 = 2.1
    z = 10.0
    for n in [3, 6, 9, 12]:
        t = time_for_n_log(D_121, n)
        print(f"  {n}-log reduction: t = {t:.1f} min")

    print("\n--- D at varying temperature (z = 10 degC) ---")
    print("  T(degC)     D(min)")
    for T in [105, 110, 115, 121, 125, 130]:
        D = D_at_temperature(D_121, 121, T, z)
        print(f"   {T:3d}        {D:.2f}")

    print("\n--- Cold-spot correction ---")
    print("  setpoint    cold T    correction factor")
    for T_set, T_cold in [(121, 119), (121, 117), (121, 115)]:
        f = cold_spot_factor(T_cold, T_set, z=10.0)
        print(f"   {T_set} degC   {T_cold} degC        {f:.2f}x")

    print("\n--- Heat-and-hold worked design: 12-log of G. stearothermophilus ---")
    D_121_GS = 1.5
    t_set = time_for_n_log(D_121_GS, 12)
    print(f"  D_121 (G.s.) = {D_121_GS} min")
    print(f"  12-log hold at 121 degC = {t_set:.1f} min")
    cf = cold_spot_factor(T_cold_C=117, T_set_C=121)
    t_design = t_set * cf
    print(f"  Design hold including cold-spot factor of {cf:.2f}: "
          f"{t_design:.1f} min")


if __name__ == "__main__":
    main()
