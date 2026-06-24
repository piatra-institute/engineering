# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Finite-difference solver for the 1D acoustic wave equation in a closed tube.

Solves  p_tt = c^2 p_xx  on [0, L] with hard-wall (Neumann, dp/dx = 0)
boundary conditions using the standard explicit central-difference
leapfrog scheme. The Courant number C = c dt / dx must satisfy C <= 1
for stability. A short FFT of the pressure history at one point recovers
the closed-tube standing-wave frequencies f_n = n c / (2 L).

Run:  uv run wave_1d.py
"""

from __future__ import annotations

import numpy as np

C = 343.0       # speed of sound, m/s
L = 1.0         # tube length, m
NX = 400        # spatial points
COURANT = 0.9   # c dt / dx, must be <= 1


def simulate(t_final: float = 1.0):
    dx = L / (NX - 1)
    dt = COURANT * dx / C
    nt = int(t_final / dt)
    x = np.linspace(0.0, L, NX)

    # initial condition: a broad off-centre bump. A wide Gaussian keeps the
    # spectral energy in the lowest few modes, where we verify the ladder.
    p_prev = np.exp(-((x - 0.37 * L) ** 2) / (0.12 * L) ** 2)
    p = p_prev.copy()
    r2 = COURANT ** 2

    # probe at a wall: a pressure antinode for every closed-tube mode
    probe = np.empty(nt)
    for n in range(nt):
        p_next = np.empty_like(p)
        p_next[1:-1] = (2 * p[1:-1] - p_prev[1:-1]
                        + r2 * (p[2:] - 2 * p[1:-1] + p[:-2]))
        # hard-wall (Neumann): mirror the neighbour so the gradient vanishes
        p_next[0] = p_next[1]
        p_next[-1] = p_next[-2]
        p_prev, p = p, p_next
        probe[n] = p[0]
    return probe, dt


def recover_modes(probe: np.ndarray, dt: float, n_peaks: int = 3):
    spec = np.abs(np.fft.rfft(probe - probe.mean()))
    freqs = np.fft.rfftfreq(len(probe), dt)
    # keep local maxima above a fraction of the largest peak, then take the
    # lowest few: the closed-tube ladder f_n = n c / (2 L) starts at n = 1
    threshold = 0.05 * spec.max()
    found = []
    for i in range(1, len(spec) - 1):
        f = freqs[i]
        if f < 50:
            continue
        if spec[i] > threshold and spec[i] >= spec[i - 1] and spec[i] >= spec[i + 1]:
            found.append(f)
    found.sort()
    return found[:n_peaks]


def main() -> None:
    probe, dt = simulate()
    measured = recover_modes(probe, dt)
    print(f"closed tube L = {L} m, c = {C} m/s, Courant = {COURANT}")
    print("mode   theory (Hz)   measured (Hz)")
    for n, fm in enumerate(measured, start=1):
        ft = n * C / (2 * L)
        print(f"  {n}    {ft:9.1f}    {fm:11.1f}")


if __name__ == "__main__":
    main()
