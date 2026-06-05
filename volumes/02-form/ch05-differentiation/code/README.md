# Code assets - Volume II, Chapter 5 (Differentiation)

Each script is self-contained, depends only on the Python standard
library, and runs with `uv run`:

```
uv run code/<script>.py
```

## Files

| File | Purpose | Used by |
|---|---|---|
| `finite_diff_accuracy.py` | Step-size sweep for forward and central differences of $f(x) = e^{x}$ at $x = 1$. Shows the V-shaped bias-variance tradeoff between round-off and truncation error. | Section 5.7 (Numerical differentiation); Simulation exercise on the step-size sweep for $f(x) = e^{x}$. |
| `noisy_derivative.py` | Central-difference derivative of $\sin(2\pi t)$ contaminated with Gaussian noise; compares root-mean-square error to the analytical $2\pi \cos(2\pi t)$ across sub-sampling strides. | Section 5.7 (Differentiating noisy data); Simulation exercise on smoothing-then-differentiation. |
| `newton_root.py` | Newton's iteration for the root of $g(x) = x^{3} - 2x - 5$; reports quadratic convergence. | Section 5.4 (linearisation as the engine of Newton's method); Simulation exercise on Newton iteration. |
| `gradient_descent.py` | Gradient descent applied to the closed-can surface-area minimisation $A(r) = 2\pi r^{2} + 2V/r$; sweeps the step size to show stable and divergent regimes. | Section 5.6 (optimisation of one variable); Simulation exercise on gradient descent for the can. |
| `related_rates.py` | Sliding-ladder related-rates calculation; tabulates the top's descent speed as the foot nears the wall base, showing the kinematic singularity. | Section 5.2 (related rates); related-rates figure. |
| `newton_basins.py` | Convergence-versus-divergence sweep of Newton's iteration over starting points for $x^{3}-2x-5$ and $\arctan x$; reports the basin of attraction. | Section 5.4 (Newton's-method divergence); Newton-divergence figure. |
| `complex_step.py` | Complex-step derivative of $e^{x}$ versus the central difference; shows the complex-step error falling as $h^{2}$ with no round-off floor. | Section 5.7 mastery box (complex-step differentiation). |

## Conventions

- Random-number generator seeded for reproducibility (per script).
- All output is human-readable text on stdout; no plots are written.
- The scripts use only `math`, `random`, and `statistics` from the standard library.
- Floating-point precision is the platform default (double precision on common hardware).

## Provenance

Editor's reference implementations. Verify with your own tools.
