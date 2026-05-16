"""Phasor adder for two sinusoids at the same frequency.

Given two sinusoids x_k(t) = A_k cos(omega t + phi_k), k = 1, 2,
this script converts each to its phasor A_k exp(i phi_k), adds them
as complex numbers, and reports the amplitude and phase of the
resulting sinusoid. It also plots the three time-domain waveforms.

Usage:
    uv run --with numpy --with matplotlib phasor_add.py

Dependencies: numpy, matplotlib.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def phasor_sum(
    amplitude_1: float,
    phase_1: float,
    amplitude_2: float,
    phase_2: float,
) -> tuple[float, float]:
    """Return the (amplitude, phase) of the sum of two same-frequency cosines.

    The inputs are A_1, phi_1, A_2, phi_2 with phases in radians.
    The output is (A, phi) such that
        A_1 cos(omega t + phi_1) + A_2 cos(omega t + phi_2)
            = A cos(omega t + phi).
    """
    phasor_1 = amplitude_1 * np.exp(1j * phase_1)
    phasor_2 = amplitude_2 * np.exp(1j * phase_2)
    phasor_sum_val = phasor_1 + phasor_2
    return float(np.abs(phasor_sum_val)), float(np.angle(phasor_sum_val))


def main() -> None:
    # The worked example of section 3.4:
    #     x_1 = 3 cos(omega t),  x_2 = 4 cos(omega t + pi/2)
    # Expected:  A = 5,  phi = arctan(4/3) ~ 0.9273 rad (53.13 deg).
    a1, p1 = 3.0, 0.0
    a2, p2 = 4.0, np.pi / 2
    a_sum, p_sum = phasor_sum(a1, p1, a2, p2)
    print(f"A = {a_sum:.6f}")
    print(f"phi = {p_sum:.6f} rad = {np.degrees(p_sum):.4f} deg")

    # Plot the three waveforms over two periods.
    omega = 2 * np.pi
    t = np.linspace(0.0, 2.0, 1001)
    x1 = a1 * np.cos(omega * t + p1)
    x2 = a2 * np.cos(omega * t + p2)
    x_sum = a_sum * np.cos(omega * t + p_sum)
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(t, x1, label=f"x_1 = {a1} cos(omega t + {p1:.2f})", linewidth=1.2)
    ax.plot(t, x2, label=f"x_2 = {a2} cos(omega t + {p2:.2f})", linewidth=1.2)
    ax.plot(t, x_sum, label=f"sum = {a_sum:.3f} cos(omega t + {p_sum:.3f})",
            linewidth=2.0, color="black")
    ax.set_xlabel("t / T")
    ax.set_ylabel("signal")
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("phasor_add.png", dpi=120)
    print("Wrote phasor_add.png")


if __name__ == "__main__":
    main()
