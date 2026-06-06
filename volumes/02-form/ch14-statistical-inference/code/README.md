# Code for Volume II Chapter 14

Two self-contained Python scripts that accompany the chapter. Both
carry PEP 723 inline metadata and run under `uv` without any
explicit virtualenv management.

## `bootstrap_demo.py`

Bootstrap resampling for the sample median of an $n = 80$
log-normal sample. Reports the bootstrap standard error of the
median, the standard error of the mean (bootstrap and classical),
and percentile-method 95% confidence intervals for both. The
output makes the bootstrap-versus-classical comparison the section
14.1 mastery box invokes.

```
uv run bootstrap_demo.py
```

## `kfold_ridge.py`

Five-fold cross-validation of ridge regression on the synthetic
`flexural-strength.csv` dataset. The script hand-rolls
standardisation and the fold loop so the structure of
cross-validation is visible. Every pre-processing operation sits
inside the loop, fold by fold, exactly as the principle box at the
close of section 14.6 requires.

```
uv run kfold_ridge.py ../data/flexural-strength.csv
```

## `regression_diagnostics.py`

Closed-form ordinary-least-squares fit on `tensile-yield.csv`, the
section 14.5 worked example. Reports the slope, intercept, residual
standard deviation, the slope's 95% confidence interval, R^2, and
the residuals against fitted values. Hand-rolls the normal
equations and carries a short Student-t lookup table so the script
has no dependencies.

```
uv run regression_diagnostics.py ../data/tensile-yield.csv
```

## `classical_tests.py`

The four classical tests of section 14.2 worked from primitives:
the one-sample t-test (machined shafts), the pooled-variance
two-sample t-test (two ceramic batches), the Pearson chi-square
goodness-of-fit (a die), and the one-way ANOVA F statistic (three
catalysts). The script prints each statistic against its tabulated
critical value; the numbers match the prose exactly.

```
uv run classical_tests.py
```

## `casestudy_fatigue.py`

The end-to-end fatigue S-N case study of section 14.7. Reads
`../data/fatigue-sn.csv`, fits the log-log Basquin model, runs a
Shapiro-Wilk residual normality check as a numeric companion to the
quantile-quantile plot, and reports both a parametric prediction
interval and a residual-bootstrap prediction interval for the life
at a query stress of 260 MPa. The printed numbers match the chapter
prose: slope `-6.20`, `sigma = 0.115`, `R^2 = 0.94`, point life
`7.6e4` cycles, parametric 95% PI `[4.3e4, 1.3e5]` cycles.

```
uv run casestudy_fatigue.py
```

## Conventions

- The random-number generator is seeded explicitly in every script.
- The bootstrap and cross-validation procedures are implemented
  from primitives rather than imported from `scipy.stats` or
  `sklearn`. The point is to make the procedure inspectable, not
  to demonstrate library competence.
- The reference solutions in the project block use the same data
  conventions and produce comparable numbers; the reader is
  expected to extend the scripts to their own dataset, not to
  reproduce these results exactly.
