# Code assets — Volume I, Chapter 1 (Why we measure)

Executable supporting code for the chapter's worked examples and
exercises. Files are runnable from this directory with a recent Python
3 interpreter and the dependencies listed in each file's header.

## Files

| File | Purpose | Used by |
|---|---|---|
| `uncertainty_propagation.py` | Type A and Type B uncertainty evaluation; linear and product propagation rules per ISO/IEC GUM. | Exercise (Derivation, propagation); the measurement habit section. |
| `monte_carlo_sigma.py` | Sample-size scaling demonstration: $\sigma/\sqrt{n}$ verified by Monte Carlo. Includes the systematic-offset variant. | Simulation exercises 1 and 2. |
| `bivariate_propagation.py` | Bivariate normal sampling and analytical-vs-empirical variance comparison for $z = x + y$ under varying correlation. | Simulation exercise 3. |
| `calibration_check.py` | Linear regression of meter reading against reference; residual analysis for calibration drift. | Estimation-block reasoning; Diagnosis exercise on pipette drift. |
| `measurement_log.py` | CLI utility: records the seven-component measurement habit entry per the chapter's section 1.5. Stores entries as JSON Lines. | Project (Instrument the home, one week). |

## Running

Each file's docstring states its dependencies and the command to run.
The Monte Carlo files require only `numpy`. The calibration regression
requires `numpy` and `scipy`. The measurement log is standard-library
only.

## License

Code is provided under the project's overall license (TBD) for
illustrative and pedagogical use. The values produced are
illustrative; production use requires verification against the
intended application.
