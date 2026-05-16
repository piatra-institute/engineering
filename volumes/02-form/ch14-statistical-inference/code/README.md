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
