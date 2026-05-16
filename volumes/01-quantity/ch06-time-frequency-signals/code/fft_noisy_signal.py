# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""FFT of a noisy 50 Hz sinusoid at sample rate 10 kHz.

Generates a 1-second record of a 50 Hz sinusoid with additive
white Gaussian noise at SNR = 40 dB, computes the magnitude
spectrum, and reports the bin index and frequency of the peak.
Also reports the bin spacing (frequency resolution) and the
location of the peak after sub-bin parabolic interpolation.

Used by the Simulation exercises that ask the reader to inspect
spectral leakage and peak interpolation.
"""

import numpy as np

RNG = np.random.default_rng(2026)


def main() -> None:
    fs = 10_000.0
    duration = 1.0
    n = int(duration * fs)
    f = 50.0
    snr_db = 40.0

    t = np.arange(n) / fs
    x_clean = np.sin(2.0 * np.pi * f * t)
    signal_power = 0.5  # variance of sin
    noise_power = signal_power / (10.0 ** (snr_db / 10.0))
    noise = RNG.normal(0.0, np.sqrt(noise_power), size=n)
    x = x_clean + noise

    X = np.fft.rfft(x)
    mag = np.abs(X)
    freqs = np.fft.rfftfreq(n, d=1.0 / fs)
    df = freqs[1] - freqs[0]

    k_peak = int(np.argmax(mag))
    f_peak_raw = freqs[k_peak]

    # Parabolic interpolation in log-magnitude
    if 0 < k_peak < len(mag) - 1:
        a = np.log(mag[k_peak - 1] + 1e-30)
        b = np.log(mag[k_peak] + 1e-30)
        c = np.log(mag[k_peak + 1] + 1e-30)
        delta = 0.5 * (a - c) / (a - 2.0 * b + c)
        f_peak_interp = (k_peak + delta) * df
    else:
        f_peak_interp = f_peak_raw

    print(f"sample rate           = {fs:.1f} Hz")
    print(f"record length         = {n} samples ({duration:.1f} s)")
    print(f"bin spacing df        = {df:.4f} Hz")
    print(f"peak bin k_peak       = {k_peak}")
    print(f"peak frequency (raw)  = {f_peak_raw:.4f} Hz")
    print(f"peak (interpolated)   = {f_peak_interp:.4f} Hz")
    print(f"true frequency        = {f:.4f} Hz")


if __name__ == "__main__":
    main()
