# Code assets — Volume II, Chapter 7 (Differential equations: ODEs)

Executable supporting code for the chapter's worked examples and
exercises. Files are runnable from this directory with a recent
Python 3 interpreter and the dependencies listed in each file's
header.

## Files

| File | Purpose | Used by |
|---|---|---|
| `euler_vs_rk4.py` | Forward Euler and classical RK4 on the scalar test problem $\dot{y}=-y$. Verifies the $O(h)$ and $O(h^{4})$ convergence rates. | Simulation exercise 1; the step-size error analysis worked example. |
| `stiff_demo.py` | Two-variable stiff system; compares explicit Euler at three step sizes against implicit Euler at $100\times$ larger steps. Prints the stiffness ratio of the Jacobian. | Simulation exercise 5; the chapter's stiffness section. |
| `phase_plane.py` | Phase-plane plotter for three 2D autonomous systems (damped oscillator, predator-prey, van der Pol). RK4 integration with optional Matplotlib output. | Simulation exercise 4; the phase-plane analysis section. |
| `pendulum_period.py` | Pendulum period extraction across an amplitude grid, by zero-crossing detection on $\dot{\theta}$. Compares numerical period against the small-angle and first-correction predictions. | The chapter project (the pendulum at large amplitudes); Simulation exercise 6. |
| `forced_oscillator.py` | Analytical frequency-response amplitude and phase of the forced second-order oscillator across a frequency sweep, with optional RK4 verification at resonance. | Section 7.5 (forced response, resonance); the driven-oscillator worked example. |
| `first_order_models.py` | First-order linear step responses across domains (mixing tank, Newton cooling, RC/RL), plus the forensic time-of-death inversion. | Section 7.2 (first-order linear ODEs); the mixing-tank, Newton-cooling, and forensic worked examples. |

## Running

Each file's docstring states its dependencies and the command to
run. The Euler/RK4 demonstration and the stiff demonstration
require only `numpy`. The phase-plane plotter optionally uses
`matplotlib` for the figure; pass `--no-plot` to print trajectory
endpoints only. The pendulum-period extractor is `numpy`-only.

A reasonable working environment is Python 3.11+ with `numpy` and
`matplotlib` installed via the reader's preferred package manager
(`pip`, `conda`, `uv`).

## License

Code is provided under the project's overall license (TBD) for
illustrative and pedagogical use. Numerical values produced by
these scripts are illustrative; production use requires
independent verification.
