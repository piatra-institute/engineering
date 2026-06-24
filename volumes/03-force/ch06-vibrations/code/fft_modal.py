#!/usr/bin/env python3
"""Spectral analysis of a measured vibration time history.

Reads an accelerometer time history (CSV: time_s, accel_g), removes the
mean, applies a Hann window, computes the single-sided amplitude
spectrum, finds the dominant peaks, and estimates the damping ratio of
the strongest peak by the half-power (3 dB) bandwidth method.

Run:  python3 fft_modal.py ../data/cantilever_decay.csv
"""

import sys
import numpy as np


def load_history(path):
    data = np.genfromtxt(path, delimiter=",", names=True)
    t = data["time_s"]
    a = data["accel_g"]
    return t, a


def amplitude_spectrum(t, a):
    """Single-sided amplitude spectrum with a Hann window."""
    n = len(a)
    dt = np.mean(np.diff(t))
    fs = 1.0 / dt
    a = a - np.mean(a)
    window = np.hanning(n)
    coherent_gain = np.mean(window)  # corrects amplitude for the window
    spec = np.fft.rfft(a * window)
    freq = np.fft.rfftfreq(n, d=dt)
    amp = (2.0 / n) * np.abs(spec) / coherent_gain
    return freq, amp, fs


def find_peaks(freq, amp, n_peaks=3, f_min=1.0):
    """Return the strongest peaks above f_min, sorted by frequency."""
    mask = freq >= f_min
    f, A = freq[mask], amp[mask]
    is_peak = np.r_[False, (A[1:-1] > A[:-2]) & (A[1:-1] > A[2:]), False]
    idx = np.where(is_peak)[0]
    idx = idx[np.argsort(A[idx])[::-1][:n_peaks]]
    idx = np.sort(idx)
    return f[idx], A[idx]


def half_power_zeta(freq, amp, f_peak):
    """Damping ratio from the half-power bandwidth around a peak."""
    i_peak = int(np.argmin(np.abs(freq - f_peak)))
    a_peak = amp[i_peak]
    a_half = a_peak / np.sqrt(2.0)
    # walk left and right to the half-power crossings
    li = i_peak
    while li > 0 and amp[li] > a_half:
        li -= 1
    ri = i_peak
    while ri < len(amp) - 1 and amp[ri] > a_half:
        ri += 1
    f1, f2 = freq[li], freq[ri]
    return (f2 - f1) / (2.0 * f_peak), f1, f2


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "../data/cantilever_decay.csv"
    t, a = load_history(path)
    freq, amp, fs = amplitude_spectrum(t, a)
    print(f"sample rate = {fs:.1f} Hz   record = {t[-1]-t[0]:.2f} s   "
          f"resolution = {1.0/(t[-1]-t[0]):.3f} Hz")
    fpk, apk = find_peaks(freq, amp, n_peaks=3)
    for f, A in zip(fpk, apk):
        print(f"peak at {f:7.2f} Hz   amplitude {A:.4e}")
    if len(fpk):
        zeta, f1, f2 = half_power_zeta(freq, amp, fpk[np.argmax(apk)])
        print(f"half-power damping ratio = {zeta:.4f}  "
              f"(band {f1:.2f}-{f2:.2f} Hz)")
