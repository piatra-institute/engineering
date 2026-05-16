# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Zero-crossing frequency estimator for a near-50 Hz mains signal.

Given an array of samples and a sample rate, this script estimates
the average frequency in a window by detecting sign changes,
interpolating the zero-crossing time linearly between bracketing
samples, and dividing the number of cycles by the elapsed time.

Used by the chapter project (24-hour mains-frequency record) as a
reference implementation. The default invocation generates a
synthetic 60-second 50.01 Hz signal at 10 kHz sampling, adds
modest noise, and prints the estimator's output for a sequence of
one-second windows.
"""

import numpy as np

RNG = np.random.default_rng(2026)


def zero_crossing_freq(
    samples: np.ndarray, fs: float, window_seconds: float
) -> list[float]:
    """Estimate frequency in successive windows of window_seconds."""
    n_per_window = int(window_seconds * fs)
    n_windows = len(samples) // n_per_window
    freqs: list[float] = []
    for w in range(n_windows):
        seg = samples[w * n_per_window:(w + 1) * n_per_window]
        # Find positive-going zero crossings: seg[i] < 0 <= seg[i+1]
        signs = seg >= 0.0
        rising = (~signs[:-1]) & signs[1:]
        idx = np.where(rising)[0]
        if len(idx) < 2:
            freqs.append(float("nan"))
            continue
        # Linear-interpolated crossing times
        crossings = []
        for i in idx:
            x0, x1 = seg[i], seg[i + 1]
            frac = -x0 / (x1 - x0) if (x1 - x0) != 0 else 0.0
            crossings.append((i + frac) / fs)
        cycles = len(crossings) - 1
        elapsed = crossings[-1] - crossings[0]
        freqs.append(cycles / elapsed if elapsed > 0 else float("nan"))
    return freqs


def main() -> None:
    fs = 10_000.0
    f_true = 50.01
    duration = 60.0
    n = int(duration * fs)
    t = np.arange(n) / fs

    x_clean = np.sin(2.0 * np.pi * f_true * t)
    snr_db = 35.0
    noise_power = 0.5 / (10.0 ** (snr_db / 10.0))
    x = x_clean + RNG.normal(0.0, np.sqrt(noise_power), size=n)

    freqs = zero_crossing_freq(x, fs, window_seconds=1.0)
    arr = np.array(freqs)
    print(f"true frequency           = {f_true:.4f} Hz")
    print(f"estimator mean           = {np.nanmean(arr):.4f} Hz")
    print(f"estimator stdev          = {np.nanstd(arr, ddof=1):.4f} Hz")
    print(f"first ten window outputs = {arr[:10]}")


if __name__ == "__main__":
    main()
