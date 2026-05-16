"""Wrap and unwrap a phase signal; demonstrate aliasing failure.

Generates a linearly advancing physical phase, wraps it to the
principal range (-pi, pi], and runs a first-order unwrap algorithm
that adds 2 pi k to each sample so consecutive samples differ by
less than pi. Shows that the unwrap fails silently when the
sample-to-sample phase change exceeds pi.

Usage:
    uv run --with numpy --with matplotlib phase_unwrap.py

Dependencies: numpy, matplotlib.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def wrap(phi: np.ndarray) -> np.ndarray:
    """Wrap to (-pi, pi]."""
    return np.angle(np.exp(1j * phi))


def unwrap_first_order(phi_wrapped: np.ndarray) -> np.ndarray:
    """Add 2 pi k so successive differences are at most pi in magnitude."""
    out = np.zeros_like(phi_wrapped)
    out[0] = phi_wrapped[0]
    k = 0
    for n in range(1, len(phi_wrapped)):
        d = phi_wrapped[n] - phi_wrapped[n - 1]
        if d > np.pi:
            k -= 1
        elif d < -np.pi:
            k += 1
        out[n] = phi_wrapped[n] + 2 * np.pi * k
    return out


def main() -> None:
    # Case 1: dense sampling, unwrap recovers truth.
    t = np.linspace(0, 5.0, 5001)
    omega = 2 * np.pi
    phi_true = omega * t
    phi_w = wrap(phi_true)
    phi_u = unwrap_first_order(phi_w)
    err = np.max(np.abs(phi_u - phi_true))
    print(f"Dense case: max |unwrap - truth| = {err:.4e} rad")

    # Case 2: sparse sampling, sample-to-sample change > pi, fails.
    t_sparse = np.linspace(0, 5.0, 9)
    phi_true_s = omega * t_sparse
    phi_w_s = wrap(phi_true_s)
    phi_u_s = unwrap_first_order(phi_w_s)
    err_sparse = np.max(np.abs(phi_u_s - phi_true_s))
    print(f"Sparse case (9 samples): max |unwrap - truth| = {err_sparse:.4f} rad")

    fig, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(7, 5),
                                          sharex=True)
    ax_top.plot(t, phi_true, label="true unwrapped",
                color="blue", linewidth=1.4)
    ax_top.plot(t, phi_w, label="wrapped",
                color="red", linewidth=0.9)
    ax_top.set_ylabel("phase (rad)")
    ax_top.legend(loc="best", fontsize=8)
    ax_top.grid(True, alpha=0.3)

    ax_bot.plot(t, phi_u, label="unwrapped (dense, 5001 samples)",
                color="black", linewidth=1.4)
    ax_bot.plot(t_sparse, phi_u_s, "o-",
                label="unwrapped (sparse, 9 samples; FAILS)",
                color="orange", linewidth=1.6, markersize=6)
    ax_bot.set_xlabel("t (s)")
    ax_bot.set_ylabel("recovered phase (rad)")
    ax_bot.legend(loc="best", fontsize=8)
    ax_bot.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("phase_unwrap.png", dpi=120)
    print("Wrote phase_unwrap.png")


if __name__ == "__main__":
    main()
