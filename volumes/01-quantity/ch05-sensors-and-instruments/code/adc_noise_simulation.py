# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Simulate ADC noise and report the inferred-temperature standard
deviation across the working range of the thermistor project.

Adds Gaussian noise with sd = 1 LSB at V_cc = 3.3 V on a 10-bit ADC,
then back-solves through the divider and the beta-parameter
thermistor model to recover an inferred temperature for each sample.

Companion to Simulation exercise 2.
"""

from __future__ import annotations

import numpy as np

V_CC = 3.30
R_REF = 10_000.0
R_0 = 10_000.0
T_0_K = 298.15
BETA = 3950.0
ADC_BITS = 10
LSB = V_CC / (2 ** ADC_BITS - 1)
N_SAMPLES = 1_000
RNG = np.random.default_rng(seed=42)


def r_thermistor(t_c: float) -> float:
    t_k = t_c + 273.15
    return R_0 * np.exp(BETA * (1.0 / t_k - 1.0 / T_0_K))


def v_from_t(t_c: float) -> float:
    r = r_thermistor(t_c)
    return V_CC * r / (R_REF + r)


def t_from_v(v: np.ndarray) -> np.ndarray:
    """Invert divider, then invert beta-parameter thermistor model."""
    # Clip to avoid division blow-up at the rails
    v = np.clip(v, 1e-4, V_CC - 1e-4)
    r = R_REF * v / (V_CC - v)
    t_k = 1.0 / (1.0 / T_0_K + np.log(r / R_0) / BETA)
    return t_k - 273.15


def main() -> None:
    print(f"LSB = {LSB*1000:.3f} mV (10-bit at 3.30 V)\n")
    print(f"{'T_true (C)':>12}  {'V_nom (V)':>10}  {'sd(T_inferred) (C)':>20}")
    for t_true in (0.0, 25.0, 50.0, 75.0):
        v_nom = v_from_t(t_true)
        noise = RNG.normal(0.0, LSB, size=N_SAMPLES)
        v_obs = v_nom + noise
        t_inferred = t_from_v(v_obs)
        sd = float(np.std(t_inferred, ddof=1))
        print(f"{t_true:>12.1f}  {v_nom:>10.4f}  {sd:>20.4f}")


if __name__ == "__main__":
    main()
