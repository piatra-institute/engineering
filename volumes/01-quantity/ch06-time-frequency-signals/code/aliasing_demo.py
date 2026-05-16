# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Demonstrate aliasing of a sinusoid sampled below the Nyquist rate.

Generates a 7500 Hz sinusoid sampled at 8000 Hz and prints the
expected alias frequency. Numerical verification: the sampled
sequence is bit-identical to a sinusoid at the alias frequency
within numerical round-off (modulo amplitude and phase).
"""

import numpy as np

RNG = np.random.default_rng(2026)


def main() -> None:
    fs = 8_000.0  # sample rate, Hz
    f = 7_500.0   # signal frequency, Hz; well above fs/2 = 4000 Hz
    duration = 0.01  # 10 ms
    n_samples = int(duration * fs)

    t = np.arange(n_samples) / fs
    x = np.sin(2.0 * np.pi * f * t)

    # Alias frequency: |f - n*fs| for integer n placing the result in [0, fs/2]
    alias = abs(f - fs)
    while alias > fs / 2:
        alias = abs(alias - fs)

    print(f"sample rate fs        = {fs:.1f} Hz")
    print(f"signal frequency f    = {f:.1f} Hz")
    print(f"Nyquist frequency     = {fs/2:.1f} Hz")
    print(f"alias frequency       = {alias:.1f} Hz")

    # Construct the alias sinusoid; should be (up to sign) numerically identical
    # to the original sampled sequence.
    y = np.sin(2.0 * np.pi * alias * t)
    # Allow for an overall sign (the alias mirrors phase across fs/2)
    err_pos = np.max(np.abs(x - y))
    err_neg = np.max(np.abs(x + y))
    err = min(err_pos, err_neg)
    print(f"max |x - (+/-)y|      = {err:.3e}")


if __name__ == "__main__":
    main()
