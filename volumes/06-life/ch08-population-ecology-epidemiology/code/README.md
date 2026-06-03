# Vol VI Ch 8 — Code assets

Companion Python scripts for *Engineering*, Volume VI, Chapter 8
(Population biology, ecology, epidemiology).

Each script is self-contained, uses only `numpy`, `scipy`,
`matplotlib`, and `pandas`, and follows the
section / exercise numbering used in `chapter.tex`.

## Files

- `logistic_growth.py` — §8.1. Logistic equation
  `dN/dt = rN(1 - N/K)` and its closed-form solution; comparison to
  exponential growth; harvested-logistic equilibria and MSY.
- `lotka_volterra.py` — §8.2. Numerical integration of the
  Lotka-Volterra and Rosenzweig-MacArthur models; phase-portrait
  plots; Hopf-bifurcation parameter sweep.
- `sir_seir_solve.py` — §8.3. ODE solvers for the SIR and SEIR
  compartmental models; final-size relation; herd-immunity
  threshold; effective $R_t$ from incidence.
- `sir_fit.py` — §8.7 / project. Maximum-likelihood and least-squares
  fitting of an SIR model to daily case-count data; residual
  analysis and 95% CIs by parametric bootstrap. The project track.
- `network_robustness.py` — §8.4. Erdős-Rényi versus scale-free
  network construction; robustness to random failure and targeted
  attack; food-web spillover-extinction simulation.
- `resistance_evolution.py` — §8.5. Deterministic
  selection-coefficient model; stochastic individual-based
  simulation of resistance fixation under constant-drug,
  pulsed-drug, and combination-drug regimens.

## Running

All scripts use the project's `uv`-managed Python environment.
From the repository root:

```
uv run volumes/06-life/ch08-population-ecology-epidemiology/code/logistic_growth.py
```

Each script writes one or more PNGs to the same directory and
prints summary statistics to stdout.

## Data dependencies

`sir_fit.py` reads from `data/covid_nz_first_wave.csv`
(or a comparable epidemic dataset). `resistance_evolution.py`
references `data/resistance_prevalence.csv` for the empirical
calibration overlay. See `data/README.md`.
