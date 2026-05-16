# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""
Discrete convolution of an input voltage with an RC low-pass filter
impulse response. Computes the output by direct discrete convolution
and compares it to the closed-form charge-discharge solution.

For input v_in(t) = V0 for 0 <= t <= T_p, 0 elsewhere, and impulse
response h(t) = (1/tau) exp(-t/tau) for t >= 0, the output is:

    v_out(t) = V0 (1 - exp(-t/tau))                 for 0 <= t <= T_p
    v_out(t) = V0 (1 - exp(-T_p/tau)) exp(-(t-T_p)/tau)  for t > T_p

Supports Volume II, Chapter 6:
  - Simulation exercise 3 (discrete convolution vs continuous).
  - Figure fig-rc-convolution.

Run directly with uv:
    uv run rc_convolution.py
"""

from __future__ import annotations

import numpy as np


def rc_impulse(t: np.ndarray, tau: float) -> np.ndarray:
    """RC impulse response: (1/tau) exp(-t/tau), zero for t < 0."""
    h = np.zeros_like(t)
    mask = t >= 0
    h[mask] = (1.0 / tau) * np.exp(-t[mask] / tau)
    return h


def rectangular_pulse(t: np.ndarray, t_start: float, t_end: float,
                      amplitude: float) -> np.ndarray:
    """Rectangular pulse: amplitude on [t_start, t_end], 0 elsewhere."""
    return np.where((t >= t_start) & (t <= t_end), amplitude, 0.0)


def closed_form(t: np.ndarray, V0: float, T_p: float,
                tau: float) -> np.ndarray:
    """Closed-form RC response to a rectangular input of width T_p."""
    out = np.zeros_like(t)
    rising = (t >= 0) & (t <= T_p)
    falling = t > T_p
    out[rising] = V0 * (1.0 - np.exp(-t[rising] / tau))
    out[falling] = V0 * (1.0 - np.exp(-T_p / tau)) * \
        np.exp(-(t[falling] - T_p) / tau)
    return out


def main() -> None:
    tau = 0.5
    V0 = 1.0
    T_p = 1.0

    # Sampling: dt small relative to tau.
    dt = 0.005
    t = np.arange(0.0, 4.0, dt)

    # Discrete convolution: v_out[n] = sum_k v_in[k] h[n-k] * dt.
    v_in = rectangular_pulse(t, 0.0, T_p, V0)
    h = rc_impulse(t, tau)
    v_out_disc = np.convolve(v_in, h, mode="full")[: t.size] * dt

    v_out_cf = closed_form(t, V0, T_p, tau)

    # Sample comparison at a handful of times.
    print(f"{'t':>6} {'discrete':>14} {'closed form':>14} {'abs err':>14}")
    for t_query in (0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0):
        idx = int(round(t_query / dt))
        print(f"{t_query:6.2f} {v_out_disc[idx]:14.6f} "
              f"{v_out_cf[idx]:14.6f} "
              f"{abs(v_out_disc[idx] - v_out_cf[idx]):14.3e}")

    peak_disc = v_out_disc.max()
    peak_cf = v_out_cf.max()
    print()
    print(f"Peak (discrete):   {peak_disc:.6f}")
    print(f"Peak (closed):     {peak_cf:.6f}")
    print(f"Relative error:    {abs(peak_disc - peak_cf) / peak_cf:.3e}")


if __name__ == "__main__":
    main()
