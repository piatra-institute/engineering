# Code assets — Volume II, Chapter 18 (Mathematical modelling)

Executable supporting code for the chapter's worked examples,
estimation blocks, and simulation exercises. Files are runnable from
this directory with Python 3.10+ and the dependencies listed in each
file's header.

## Files

| File | Purpose | Used by |
|---|---|---|
| `cooling_fit.py` | Linearised fit of Newton's law of cooling to the cooling-cup notebook (`data/cooling_cup.csv`). Reports point estimate, 95% confidence interval, predicted time to 60$^\circ$C, and the propagated interval on the prediction. | Worked example 18.6 (cooling cup, from notebook to model); Exercises 18.11 and 18.12 (Calculation). |
| `logistic_fit.py` | Nonlinear least-squares fit of $\dot N = rN(1 - N/K)$ to the bacterial-growth data (`data/logistic_growth.csv`), reporting $\hat r$, $\hat K$, their intervals from the Hessian, and an identifiability diagnostic (the condition number of the Jacobian). | Worked example 18.7 (biological system); Exercise 18.14 (Calculation). |
| `identifiability_demo.py` | Synthetic demonstration of the figure 18.4 regime map: generates logistic data restricted to (A) exponential-only, (B) inflection-spanning, (C) saturation-only windows and shows that the resulting (r, K) confidence ellipses widen and rotate. Produces a PNG matching the figure. | Exercise 18.18 (Design an identification experiment); section 18.3 deepening on identifiability. |
| `bootstrap_interval.py` | Nonparametric bootstrap of any one of the chapter's fits (cooling-cup, pendulum, logistic, beam). Resamples with replacement, computes the bootstrap distribution of the parameter, and reports the 2.5th and 97.5th percentiles alongside the analytical interval. | Exercise 18.15 (Bootstrap interval). |
| `cross_validation.py` | k-fold cross-validation on the cooling-cup data: partitions, fits on k-1 folds, validates on the held-out fold, aggregates validation residuals, and compares to the in-sample residuals. Reports the inflation factor for the structural-error correction to the prediction interval. | Section 18.5 (model uncertainty and structural error); Exercise 18.10 (Derivation, cross-validation as variance estimator). |
| `overfit_demo.py` | Generates 12 points from a quadratic ground truth plus noise, fits a quadratic and a degree-10 polynomial, reports both fits' training residuals, then evaluates both on 5 held-out points. The ratio of held-out to training residuals exposes the overfit. | Exercise 18.16 (Overfit, by construction); section 18.8 (failure mode: calibration that overfit). |
| `dimensional_analysis.py` | Buckingham-Pi automation: given a list of variables and their dimensions in SI base units, computes a maximal set of independent dimensionless groups. Demonstrates on the pendulum, the beam, and the cooling cup. | Section 18.2 (Rule three: nondimensionalise); supports any future modelling project where the reader has variables but not yet a candidate equation. |
| `sensitivity_propagation.py` | Computes relative sensitivities $\tilde S_i = (\theta_i/y) \partial y / \partial \theta_i$ analytically (symbolic differentiation) and by finite difference. Produces the tornado-diagram data for the beam-deflection example. | Exercise 18.5 (Beam deflection, sensitivity); Exercise 18.17 (Sensitivity by perturbation); figure 18.6 (tornado diagram). |
| `model_triangulation.py` | Implements the four-route triangulation of figure 18.5: computes each route's estimate from the input data, propagates each route's stated uncertainty, and produces the comparison plot. | Section 18.5 (model triangulation); supports the project's structural-uncertainty section. |

## Running

Each file's docstring states its dependencies and a sample invocation.
The scipy-based fits require `numpy` and `scipy`. The bootstrap and
cross-validation files require only `numpy`. The dimensional-analysis
tool requires `sympy` for the null-space computation. The plotting
files optionally use `matplotlib` to write a PNG; the numerical output
is printed regardless.

## A note on numerical reproducibility

The synthetic-data demonstrations seed `numpy.random.default_rng(0)` at
the top so that the printed numbers are stable across runs. The
real-data fits (cooling cup, logistic growth) read from `../data/` and
should produce identical numerical output on any compliant numpy/scipy
installation.

## License

Code is provided under the project's overall license (TBD) for
illustrative and pedagogical use. The values produced are
illustrative; production use requires verification against the
intended application.
