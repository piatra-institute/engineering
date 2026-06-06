# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""
Coulomb counting: state of charge by integrating a measured cell
current. Supports Volume II, Chapter 6, section 6.10 (case study) and
figure fig-coulomb-counting.

Generates a realistic 1800 s discharge trace at 1 Hz: a nominal 1.5 A
discharge with a 100 s load transient near the middle rising to about
2.2 A, plus 20 mA per-sample Gaussian measurement noise. Integrates
the absolute current by the composite trapezoidal rule to get the
charge removed, converts to amp-hours and a state-of-charge drop on a
3.0 Ah cell, and reports a three-term error budget (gain, offset,
noise).

Writes the trace to data/coulomb_trace.csv (columns: t_s, current_A,
charge_removed_C).

Run directly with uv:
    uv run coulomb_counting.py
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np

DT = 1.0  # sampling interval, seconds
N = 1800  # number of samples (0 .. 1800 s)
Q_RATED_AH = 3.0  # rated capacity, amp-hours
SENSOR_NOISE_A = 0.020  # per-sample current noise, amperes (std)
GAIN_UNCERTAINTY = 0.005  # fractional gain uncertainty (1-sigma)
OFFSET_A = 0.005  # illustrative sensor offset, amperes


def reference_current(t: np.ndarray) -> np.ndarray:
    """Nominal discharge current (positive magnitude), amperes."""
    base = 1.5 * np.ones_like(t)
    # Smooth 100 s load transient centred at t = 900 s, peak ~ +0.7 A.
    transient = 0.7 * np.exp(-((t - 900.0) ** 2) / (2.0 * 40.0**2))
    return base + transient


def trapezoid(y: np.ndarray, dt: float) -> float:
    """Composite trapezoidal integral of samples y at spacing dt."""
    return float(dt * (0.5 * y[0] + y[1:-1].sum() + 0.5 * y[-1]))


def running_charge(y: np.ndarray, dt: float) -> np.ndarray:
    """Cumulative trapezoidal integral, coulombs, sample by sample."""
    out = np.zeros_like(y)
    out[1:] = np.cumsum(0.5 * (y[:-1] + y[1:]) * dt)
    return out


def main() -> None:
    rng = np.random.default_rng(20260606)
    t = np.arange(N + 1, dtype=float) * DT
    i_true = reference_current(t)
    i_meas = i_true + rng.normal(0.0, SENSOR_NOISE_A, size=t.shape)

    q_out = trapezoid(i_meas, DT)  # coulombs removed
    q_out_ah = q_out / 3600.0
    soc_drop = q_out_ah / Q_RATED_AH

    # Convergence-by-halving check on every other sample.
    q_half = trapezoid(i_meas[::2], 2.0 * DT)
    trunc_change = abs(q_half - q_out)

    # Error budget (coulombs).
    err_gain = GAIN_UNCERTAINTY * q_out
    err_offset = OFFSET_A * (N * DT)
    err_noise = SENSOR_NOISE_A * DT * math.sqrt(N)
    err_combined = math.sqrt(err_gain**2 + err_noise**2)  # offset is systematic

    print(f"charge removed       = {q_out:10.2f} C  = {q_out_ah:.4f} Ah")
    print(f"state-of-charge drop = {100*soc_drop:6.2f} %")
    print(f"trapezoid (h=1 s)    = {q_out:10.2f} C")
    print(f"trapezoid (h=2 s)    = {q_half:10.2f} C  "
          f"(change {trunc_change:.3f} C)")
    print("error budget (coulombs):")
    print(f"  gain   (0.5%)      = {err_gain:8.2f} C")
    print(f"  offset (5 mA, sys) = {err_offset:8.2f} C  "
          f"({100*err_offset/q_out:.2f}% coherent)")
    print(f"  noise  (random)    = {err_noise:8.2f} C  "
          f"({100*err_noise/q_out:.3f}%)")
    print(f"  combined random k=2= {2*err_combined:8.2f} C  "
          f"({100*2*err_combined/q_out:.2f}%)")

    charge = running_charge(i_meas, DT)
    out_path = Path(__file__).resolve().parents[1] / "data" / "coulomb_trace.csv"
    with out_path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["t_s", "current_A", "charge_removed_C"])
        for k in range(0, N + 1, 30):  # decimate to 30 s for the committed CSV
            writer.writerow([f"{t[k]:.0f}", f"{i_meas[k]:.4f}",
                             f"{charge[k]:.2f}"])
    print(f"wrote decimated trace to {out_path}")


if __name__ == "__main__":
    main()
