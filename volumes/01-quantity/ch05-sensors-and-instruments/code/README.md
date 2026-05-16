# Code assets - Volume I, Chapter 5 (Sensors and instruments)

Each script is self-contained and runnable with `uv run`:

```
uv run code/<script>.py
```

All scripts seed their random-number generators for reproducibility,
write human-readable text to stdout (no files), and use only numpy
where numpy is needed. The Steinhart-Hart fit uses only
`numpy.linalg.lstsq`; no scipy dependency.

## Files

| File | Purpose | Used by |
|---|---|---|
| `thermistor_divider.py` | Transfer curve V_out vs T for the chapter project's voltage divider; reports the temperature of maximum sensitivity. | Section 5.4 thermistor case; Simulation exercise 1; project. |
| `adc_noise_simulation.py` | Adds Gaussian noise at 1 LSB on a 10-bit ADC and reports the standard deviation of the inferred temperature at 0, 25, 50, 75 C. | Simulation exercise 2; project. |
| `steinhart_hart_fit.py` | Linear least-squares fit of the Steinhart-Hart equation to a synthetic calibration table; comparison with the beta-parameter approximation. | Simulation exercise 3; project. |
| `redundancy_correlation.py` | Standard uncertainty of the mean of three sensors with pairwise correlation rho; closed-form vs Monte Carlo verification. | Simulation exercise 4; Failure section (common-mode); Air France 447 illustration. |
| `johnson_noise.py` | Johnson noise voltage for a resistor over a measurement bandwidth at room temperature; tabulates several R and Delta f. | Estimation exercise 3. |

## Conventions

- Random-number generator seeded per script (`np.random.default_rng(seed)`).
- Sample counts at the low end of practical Monte Carlo (10^3 to 10^5);
  production work would increase by an order of magnitude.
- All physical constants taken from CODATA 2018 / SI 2019.
- Output is human-readable text on stdout, not files.

## Provenance

Editor's reference implementations. The reader is expected to
re-derive and re-run them as part of working the exercises and the
project.
