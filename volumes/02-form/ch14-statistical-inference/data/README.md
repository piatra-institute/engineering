# Data for Volume II Chapter 14

## `flexural-strength.csv`

A small synthetic dataset of $n = 60$ flexural-strength
measurements on an alumina ceramic, with three predictors. The
columns are:

| Column | Meaning | Units |
|---|---|---|
| `porosity_pct` | Apparent porosity from Archimedes immersion | % |
| `grain_size_um` | Mean grain size from intercept method | um |
| `sintering_temp_C` | Sintering temperature held one hour | C |
| `flexural_MPa` | Flexural strength from four-point bend test | MPa |

The data are simulated, not measured. They are generated from a
linear model with negative coefficients on porosity and grain size,
a positive coefficient on sintering temperature, and Gaussian
noise. The dataset is in the chapter for two reasons:

1. The predictors are correlated. Higher sintering temperature
   reduces porosity and slightly increases grain size, exactly
   the kind of design-matrix conditioning that makes ridge
   regression operationally useful.
2. The signal-to-noise ratio is realistic for laboratory
   ceramic-strength data, so the cross-validated mean squared
   error and the in-sample mean squared error differ visibly,
   making the section 14.6 lesson reproducible at the level of
   the dataset.

Suitable both as the reference dataset for `code/kfold_ridge.py`
and as a starting point for the reader's own project, with the
proviso that the reader's project should use real data, not
simulated data.

## `tensile-yield.csv`

The eight-point worked least-squares example of section 14.5. The
predictor `x` is carbon content in hundredths of a percent and the
response `y` is yield strength in arbitrary working units. The
ordinary-least-squares fit is `yhat = 2.293 + 0.907 x` with
residual standard deviation `0.262`, slope 95% confidence interval
`[0.808, 1.006]`, and `R^2 = 0.988`. The eight points are chosen so
the arithmetic of the normal equations is tractable by hand and the
residuals scatter without a systematic pattern, making the dataset
a clean reference for `code/regression_diagnostics.py`.

## Provenance

Authors' synthetic data, generated 2026-05-16, seeded
deterministically. The generating script is held in
the editor's private files and is not part of the deliverable; the
table itself is the artefact.
