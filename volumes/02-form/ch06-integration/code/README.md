# Code assets — Volume II, Chapter 6 (Integration)

## Files

| File | Purpose | Used by |
|---|---|---|
| `quadrature_convergence.py` | Trapezoidal, Simpson, and three-point Gauss-Legendre quadrature applied to $\int_0^1 e^{-x^2} dx$; prints the absolute error vs $n$ and verifies the $h^2$, $h^4$, and exponential convergence orders. | Simulation exercise 1; figure `fig-quadrature-convergence`. |
| `rc_convolution.py` | Discrete convolution of a rectangular input pulse with an RC impulse response; compares to the closed-form charge-discharge solution. | Simulation exercise 3; figure `fig-rc-convolution`. |
| `moment_of_inertia_profile.py` | Numerical integration of $I = \int x^2 \sigma(x) dx$ from a measured cross-section profile in `data/hammer_profile.csv`; demonstrates the convergence-by-halving check. | Chapter project (method ii); diagnosis exercise on hammer discrepancy. |
| `monte_carlo_2d.py` | Monte Carlo integration of $\int_0^1 \int_0^1 e^{-(x^2 + y^2)} dx dy$ with reported mean and standard error; comparison to a trapezoidal-rule double integral. | Simulation exercise 4. |
| `coulomb_counting.py` | Coulomb counting: integrates a measured 1800 s cell-current trace (nominal 1.5 A discharge with a load transient and 20 mA noise) by the trapezoidal rule to get charge removed and state-of-charge drop; reports the three-term error budget (gain, offset, noise) and writes `data/coulomb_trace.csv`. | Case study (section 6.10); figure `fig-coulomb-counting`. |
| `drag_energy.py` | Aerodynamic drag energy over a 180 s drive cycle: integrates the cubic-in-speed drag power $P = \tfrac12 \rho C_d A v^3$ by the trapezoidal rule, cross-checks by Simpson and by halving, contrasts a $v$-dependent and constant $C_d$, and reports a four-term error budget (drag coefficient, cubed speed-sensor scale, air density, frontal area); writes `data/drag_trace.csv`. | Case study (drag energy); figure `fig-drag-energy`. |
| `fourier_coefficients.py` | Fourier-coefficient pipeline: computes the sine coefficients of a unit square wave by trapezoidal quadrature of the projection integral, confirms agreement with the closed form $b_n = 4/(n\pi)$, and reconstructs partial sums showing the Gibbs overshoot. | Fourier-coefficient subsection; figure `fig-fourier-coefficients`. |

## Running

All files use only the Python standard library plus `numpy` (and,
where indicated, `matplotlib` for plotting). Each file carries
PEP 723 inline metadata so it can be run directly with `uv run`:

```
uv run volumes/02-form/ch06-integration/code/quadrature_convergence.py
```

Or, in a Python environment with `numpy` installed:

```
python quadrature_convergence.py
```

Each file's docstring lists its specific dependencies and the
exercise or figure it supports.
