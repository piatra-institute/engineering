# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Toy recombinant-insulin mass-balance calculator.

Closes the worked example in the chapter. Inputs:

- target finished-product mass (kg)
- culture titer at harvest (g insulin / L broth)
- per-step downstream yields (clarification, capture, refolding,
  polishing/formulation)
- batch volume and batch rejection rate

Outputs:

- required culture volume per kg product
- expected number of successful batches
- expected number of batches attempted
- sensitivity of total yield to the weakest downstream step

Run: uv run insulin_yield_calc.py
"""
from __future__ import annotations
import numpy as np


def total_recovery(step_yields: list[float]) -> float:
    out = 1.0
    for y in step_yields:
        out *= y
    return out


def required_volume_L(target_kg: float, titer_g_per_L: float,
                       recovery: float) -> float:
    target_g = target_kg * 1000.0
    return target_g / (recovery * titer_g_per_L)


def batches_attempted(n_successful: float, rejection: float) -> float:
    return n_successful / (1.0 - rejection)


def main() -> None:
    print("--- Toy recombinant insulin mass balance ---")
    target_kg = 1.0
    titer = 1.0   # g / L
    steps = [0.90, 0.80, 0.75, 0.75]
    labels = ["clarification / harvest", "capture chromatography",
              "refolding / cleavage", "polishing / formulation"]
    recovery = total_recovery(steps)
    V_required = required_volume_L(target_kg, titer, recovery)
    print(f"  Target: {target_kg:.2f} kg purified product")
    print(f"  Culture titer: {titer:.2f} g / L")
    print("  Downstream step yields:")
    for s, lab in zip(steps, labels):
        print(f"    {lab:<28}: {s:.3f}")
    print(f"  Cumulative downstream yield: {recovery:.3f} ({recovery*100:.1f} percent)")
    print(f"  Required culture volume: {V_required:.0f} L")

    batch_volume = 500.0
    n_succ = V_required / batch_volume
    rejection = 0.10
    n_att = batches_attempted(n_succ, rejection)
    print(f"\n  Batch volume: {batch_volume:.0f} L")
    print(f"  Successful batches needed: {n_succ:.1f}")
    print(f"  Expected batches attempted "
          f"(rejection rate {rejection:.0%}): {n_att:.1f}")

    print("\n--- Sensitivity: lift the weakest step ---")
    worst = int(np.argmin(steps))
    print(f"  Weakest step: {labels[worst]}  (current yield {steps[worst]:.3f})")
    for new_y in np.arange(0.75, 0.96, 0.05):
        steps_new = list(steps)
        steps_new[worst] = float(new_y)
        rec_new = total_recovery(steps_new)
        V_new = required_volume_L(target_kg, titer, rec_new)
        print(f"    weakest -> {new_y:.2f} : total recovery = "
              f"{rec_new:.3f}, volume required = {V_new:.0f} L "
              f"(saving {V_required - V_new:.0f} L)")

    print("\n--- Titer sensitivity (recovery held at design 40 percent) ---")
    rec0 = 0.40
    for t in [0.5, 1.0, 2.0, 4.0, 8.0]:
        V = required_volume_L(target_kg, t, rec0)
        print(f"  titer {t:.1f} g/L -> volume {V:.0f} L")


if __name__ == "__main__":
    main()
