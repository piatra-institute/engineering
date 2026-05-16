# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Thermistor voltage-divider transfer curve.

Computes V_out vs T for an NTC thermistor (beta-parameter model) in
the divider configuration of Chapter 5, where the fixed reference
resistor is the upper leg and the thermistor is the lower leg.

Reference values:
  V_cc       = 3.30 V
  R_ref      = 10.00 kOhm
  R_0        = 10.00 kOhm at T_0 = 25 C
  beta       = 3950 K
  T sweep    = 0 ... 80 C

Output (stdout): T, R_th, V_out at sampled temperatures.

Companion to Simulation exercise 1 and the chapter project.
"""

from __future__ import annotations

import numpy as np

V_CC = 3.30  # V
R_REF = 10_000.0  # ohm
R_0 = 10_000.0  # ohm at T_0
T_0_K = 298.15  # K (25 C)
BETA = 3950.0  # K


def r_thermistor(t_celsius: np.ndarray) -> np.ndarray:
    """NTC thermistor resistance (ohm) at temperature T (Celsius)."""
    t_k = t_celsius + 273.15
    return R_0 * np.exp(BETA * (1.0 / t_k - 1.0 / T_0_K))


def v_divider(r_th: np.ndarray) -> np.ndarray:
    """Divider output: thermistor as lower leg, R_ref as upper leg."""
    return V_CC * r_th / (R_REF + r_th)


def main() -> None:
    t = np.arange(0.0, 81.0, 5.0)
    r = r_thermistor(t)
    v = v_divider(r)
    print(f"{'T (C)':>8}  {'R_th (Ohm)':>12}  {'V_out (V)':>10}")
    for t_i, r_i, v_i in zip(t, r, v):
        print(f"{t_i:>8.1f}  {r_i:>12.1f}  {v_i:>10.4f}")
    # Find temperature of maximum |dV/dT| (numerical)
    dv = np.gradient(v, t)
    idx = int(np.argmax(np.abs(dv)))
    print()
    print(f"steepest |dV/dT| at T = {t[idx]:.1f} C: dV/dT = {dv[idx]:.4f} V/K")


if __name__ == "__main__":
    main()
