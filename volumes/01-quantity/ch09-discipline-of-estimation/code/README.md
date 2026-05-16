# Code assets — Volume I, Chapter 9 (The discipline of estimation)

Each script is self-contained and runnable with `uv run`:

```
uv run code/<script>.py
```

## Files

| File | Purpose | Used by |
|---|---|---|
| `piano_tuners.py` | Reference Fermi-decomposition calculator for the Chicago piano-tuner problem, with named input ranges and a low/nominal/high estimate. | Section 9.1, canonical estimate. |
| `fermi_calculator.py` | General Fermi-decomposition calculator: takes branches with their (low, nominal, high) values, propagates by sampling, and reports the product distribution. | Project, Simulation exercise 1, Fermi 50. |
| `brier_score.py` | Brier-score scorer for a list of predicted probabilities and observed binary outcomes; the calibration tool used in section 9.6 mastery box. | Section 9.6 mastery box, exercise 50 reflection. |
| `monte_carlo_fermi.py` | Monte Carlo propagation of multiplicative factor uncertainties for an arbitrary Fermi decomposition; compares Monte Carlo result to the log-quadrature approximation. | Section 9.2, simulation exercise. |

## Conventions

- Random-number generator seeded for reproducibility (per script).
- Sample counts are at the low end of practical Monte Carlo (10^4 to 10^5); production work would increase by an order of magnitude.
- Output is human-readable text on stdout, not files.

## Provenance

Editor's reference implementations. Verify with your own tools.
