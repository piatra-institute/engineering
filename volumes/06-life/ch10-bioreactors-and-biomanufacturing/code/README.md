# Code assets for Vol VI Ch 10 (Bioreactors and biomanufacturing)

Six Python scripts, each runnable with `uv run <script>.py` thanks to
PEP 723 inline metadata. The scripts implement the quantitative
arguments of the chapter at a level a working engineer can audit and
extend.

- `monod_growth_fit.py`: fits Monod parameters $\mu_{\max}$ and $K_S$
  to synthetic specific-growth-rate-versus-substrate data using a
  non-linear least-squares fit and reports parameters, confidence
  intervals, and residual diagnostics. Includes a chemostat steady-state
  check that solves $\mu(S^\ast) = D$ for the substrate setpoint and
  flags the washout dilution rate.
- `kla_scale_up.py`: computes $k_L a$ for stirred-tank bioreactors
  using the Van't Riet correlation
  $k_L a = c (P / V)^a (v_s)^b$
  and walks the scale-up from a 10 L development reactor to 10000 L
  production under three rules (constant geometry, constant $P/V$,
  constant $k_L a$). Outputs the impeller-power, gas-flow, and
  tip-speed requirements at each scale.
- `mass_balance_ferment.py`: closes a household-scale fermentation
  mass balance for the chapter project. Takes initial cabbage and salt
  mass (sauerkraut) or initial sugar and water mass (sugar-yeast
  CO$_2$ fermentation), runs a finite-time Monod model with lactic-acid
  or ethanol product, and reports mass-in, mass-out, CO$_2$ produced,
  salt fraction, and the implied biomass yield.
- `chromatography_resolution.py`: computes the resolution $R_s$ of a
  binary chromatographic separation from peak retention times and peak
  widths, plus the cumulative downstream yield through a configurable
  number of steps. Useful for the polishing-step exercises and for
  the toy insulin process.
- `sterile_log_reduction.py`: computes the time required for an
  $n$-log reduction at a given decimal reduction time $D$, with
  Arrhenius scaling by the $z$ value between sterilisation
  temperatures. Reports cold-spot correction factors and a worked
  twelve-log calculation for heat sterilisation.
- `insulin_yield_calc.py`: closes the toy insulin mass balance from
  the worked example. Inputs are target finished-product mass, culture
  titer, and per-step downstream yields; outputs are required culture
  volume, expected number of successful batches, expected number of
  batches attempted under a stated rejection rate, and a sensitivity
  sweep of total yield versus the weakest-step yield.

Each script writes results to stdout in a fixed format that the
chapter text or a downstream notebook can quote without
re-derivation. None require external data; the working data is at
`data/`.
