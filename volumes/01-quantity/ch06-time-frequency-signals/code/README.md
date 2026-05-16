# Code assets — Volume I, Chapter 6 (Time, frequency, signals)

Each script is self-contained and runnable with `uv run`:

```
uv run code/<script>.py
```

The scripts use NumPy only; no SciPy dependency.

## Files

| File | Purpose | Used by |
|---|---|---|
| `aliasing_demo.py` | Generates a 7.5 kHz sinusoid sampled at 8 kHz, reports the alias frequency, and verifies bit-identity of the sampled sequence with the corresponding alias-frequency sinusoid. | Section 6.4 (Sampling and aliasing); Simulation exercise on the 7500/8000 Hz alias. |
| `fft_noisy_signal.py` | One-second FFT of a noisy 50 Hz sinusoid at 10 kHz sampling; reports peak bin, peak frequency, parabolic-interpolated peak, and bin spacing. | Section 6.5 (Time-frequency duality preview); Simulation exercise on FFT peak detection and spectral leakage. |
| `patriot_drift.py` | Reproduces the Patriot range-gate clock-drift mechanism: 24-bit truncation of 1/10, per-tick error $9.5 \times 10^{-8}$, cumulative 0.34 s after 100 h. Compares 16/24/32/64-bit truncations. | Section 6.7 (Failure: clock drift and the Patriot missile); Simulation exercise on the Patriot-style integer counter. |
| `allan_variance.py` | Overlapping Allan deviation estimator; demonstrates white FM, flicker FM, and drift regimes on synthetic data. | Section 6.2 (Clocks) and Section 6.3 (Phase noise and jitter); reference for the Allan-deviation figure. |
| `mains_zero_crossing.py` | Zero-crossing-with-linear-interpolation frequency estimator for the chapter project's mains-frequency record; demonstrates on a synthetic 60-second 50.01 Hz signal. | Section 6.4 (Sampling and aliasing) and the chapter project; Simulation exercise on the zero-crossing versus FFT estimator. |
| `clock_comparison.py` | Cumulative time error across the four clock families over one day and one year; compares Patriot 100-h drift against representative atomic-clock specifications. | Section 6.2 (Clocks); Calculation and Estimation exercises on cumulative error. |

## Conventions

- Random-number generator seeded for reproducibility (`np.random.default_rng(2026)`).
- Output is human-readable text on stdout; no files are written.
- Sample counts are at the low end of practical Monte Carlo; production work would increase by an order of magnitude.

## Provenance

Editor's reference implementations, written for pedagogical use. The
Patriot per-tick error and 100-h figure match the GAO report
(`acc:gao-patriot-1992`). The Allan-deviation noise models follow
the convention in `text:ch06-rubiola-2009` and the original
`paper:ch06-allan-1966`.
