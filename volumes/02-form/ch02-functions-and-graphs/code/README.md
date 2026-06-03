# Code assets - Volume II, Chapter 2 (Functions and graphs)

Executable supporting code for the chapter's figures, worked
examples, and simulation exercises. Each file carries PEP 723 inline
metadata and runs under `uv run`.

## Files

| File | Purpose | Used by |
|---|---|---|
| `function_zoo.py` | Tabulates and plots five elementary functions (linear, quadratic, exponential, logarithm, sine) on a shared horizontal range; writes the tabulated values to CSV. | Function-zoo figure cross-check; Section 2.1 reading. |
| `semilog_fit.py` | Fits an exponential decay two ways - on linear axes and on log-transformed data - and reports the recovered time constant. Demonstrates the linear-fit-on-log-data trap from the Simulation exercises. | Simulation exercise (noisy exponential fit); Section 2.3 worked example. |
| `thermistor_calibration.py` | Reads thermistor R-vs-T data from CSV, transforms to Arrhenius axes (ln R vs 1/T), fits a straight line, and reports the B-constant. Writes both the raw and transformed data for plotting. | Thermistor-fit figure cross-check; Design exercise. |
| `bisection_root.py` | Pure-Python bisection root finder; demonstrates the elementary root-finding loop the chapter cites for higher-degree polynomials. | Calculation exercises on polynomial roots; Volume II Chapter 16 forward reference. |

## Running

```
uv run function_zoo.py 0 6 200 ../data/function_zoo.csv
uv run semilog_fit.py 50 0.5 1.0 0.10 ../data/exponential_decay_noisy.csv
uv run thermistor_calibration.py ../data/thermistor_calibration.csv
uv run bisection_root.py
```

All scripts use the standard library only except where noted in the
PEP 723 metadata. Random seeds are fixed (`20260603`) for
reproducibility.

## What these scripts are and are not

Each script demonstrates the chapter's curve-fitting, transform, or
root-finding pattern on a small explicit example. None is a
production tool. The chapter's discipline applies here too: a fit
is a claim, and a claim about a fit needs uncertainty, a residual
plot, and a stated regime of validity. The scripts illustrate the
mechanics; the discipline lives in the prose.
