"""AC frequency sweep of a passive filter, returning a Bode response.

Compute the complex transfer function of a series RLC bandpass filter taken
across the resistor, then return magnitude in decibels and phase in degrees
over a logarithmic frequency grid. The same machinery characterises any
linear two-port once its transfer function is written in terms of the
phasor impedances Z_R = R, Z_L = j w L, Z_C = 1/(j w C).

Units: ohms, henries, farads, hertz.
"""

from __future__ import annotations

import numpy as np


def bandpass_response(R, L, C, f):
    """Voltage transfer function H = V_R / V_in for a series RLC bandpass."""
    w = 2.0 * np.pi * np.asarray(f, dtype=float)
    Zc = 1.0 / (1j * w * C)
    Zl = 1j * w * L
    H = R / (R + Zl + Zc)
    return H


def bode(H):
    mag_db = 20.0 * np.log10(np.abs(H))
    phase_deg = np.degrees(np.angle(H))
    return mag_db, phase_deg


def resonant_summary(R, L, C):
    f0 = 1.0 / (2.0 * np.pi * np.sqrt(L * C))
    Q = (2.0 * np.pi * f0 * L) / R
    bw = f0 / Q
    return f0, Q, bw


if __name__ == "__main__":
    R, L, C = 126.0, 10e-3, 25e-9
    f = np.logspace(3, 5, 400)  # 1 kHz to 100 kHz
    H = bandpass_response(R, L, C, f)
    mag_db, _ = bode(H)
    f0, Q, bw = resonant_summary(R, L, C)
    print(f"f0 = {f0:.1f} Hz, Q = {Q:.2f}, bandwidth = {bw:.1f} Hz")
    print(f"peak magnitude = {mag_db.max():.2f} dB")
