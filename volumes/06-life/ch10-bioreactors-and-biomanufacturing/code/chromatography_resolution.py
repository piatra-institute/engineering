# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Chromatography resolution and downstream cumulative-yield calculator.

Resolution between two peaks:

    R_s = 2 * (t_R2 - t_R1) / (w_1 + w_2)

where t_R is the retention time and w is the baseline peak width.
R_s >= 1.5 is the conventional baseline-separation criterion.

Also walks the cumulative yield of an n-step purification train,
reports the worst-step contribution, and runs a sensitivity sweep.

Run: uv run chromatography_resolution.py
"""
from __future__ import annotations
import numpy as np


def resolution(t_R1: float, t_R2: float, w_1: float, w_2: float) -> float:
    return 2.0 * (t_R2 - t_R1) / (w_1 + w_2)


def cumulative_yield(step_yields: list[float]) -> float:
    y = 1.0
    for s in step_yields:
        y *= s
    return y


def worst_step_index(step_yields: list[float]) -> int:
    return int(np.argmin(step_yields))


def lift_one_step(step_yields: list[float], idx: int, new_y: float) -> float:
    new_train = list(step_yields)
    new_train[idx] = new_y
    return cumulative_yield(new_train)


def main() -> None:
    print("--- Resolution example: capture chromatography pair ---")
    t_R1, t_R2 = 12.4, 15.7   # minutes
    w_1, w_2 = 1.8, 2.1       # minutes baseline width
    R_s = resolution(t_R1, t_R2, w_1, w_2)
    print(f"  Peaks at {t_R1} and {t_R2} min; widths {w_1} and {w_2} min")
    print(f"  R_s = {R_s:.2f}   ({'PASS' if R_s >= 1.5 else 'FAIL'} the 1.5 baseline criterion)")

    print("\n--- Downstream yield, 5-step train ---")
    train = [0.92, 0.85, 0.78, 0.88, 0.95]
    labels = ["clarification", "capture", "intermediate",
              "polishing", "concentration / formulation"]
    total = cumulative_yield(train)
    print("  Step yields:")
    for s, lab in zip(train, labels):
        print(f"    {lab:<28}: {s:.3f}")
    print(f"  Cumulative train yield: {total:.3f}  ({total*100:.1f} percent)")
    worst = worst_step_index(train)
    print(f"  Worst step: {labels[worst]} (yield {train[worst]:.3f})")
    new_total = lift_one_step(train, worst, 0.90)
    print(f"  Lifting worst step to 0.90: new total = {new_total:.3f}")
    print(f"  Relative improvement: {(new_total - total)/total*100:.1f} percent")

    print("\n--- Sensitivity sweep over weakest-step yield ---")
    print("  weakest_y    total_yield")
    for y_w in np.arange(0.5, 0.96, 0.05):
        t = lift_one_step(train, worst, float(y_w))
        print(f"     {y_w:.2f}        {t:.3f}")


if __name__ == "__main__":
    main()
