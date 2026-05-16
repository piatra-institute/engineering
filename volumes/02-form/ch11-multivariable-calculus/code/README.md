# Code assets - Volume II, Chapter 11 (Multivariable calculus)

Executable supporting code for the chapter's worked examples and
exercises. Files are runnable from this directory with a recent
Python 3 interpreter; each script carries PEP 723 inline metadata
declaring its dependencies and can be executed with `uv run
<file.py>`.

## Files

| File | Purpose | Used by |
|---|---|---|
| `gradient_descent_rosenbrock.py` | Fixed-step gradient descent on the Rosenbrock function with $b = 10$, configured to reproduce the chapter's Simulation exercise. Reports the final iterate, the final loss, and whether the iterate reached the global minimum within tolerance. | Simulation exercise on gradient descent; the saddle-point and curved-valley discussion in section 11.3. |
| `volume_concentration.py` | Analytical and Monte Carlo computation of the outer-shell volume fraction $1 - (1 - \varepsilon)^{n}$ and the inscribed-ball-to-cube ratio $V_{n}(1) / 2^{n}$, across a range of dimensions. Emits a CSV table to `../data/volume_concentration.csv`. | Failure-section figure and the Simulation exercise on the inscribed-ball ratio. |
| `critical_points.py` | Numerical critical-point location and classification for $f(x, y) = \sin(x)\cos(y)$ on $[0, 2\pi]^{2}$, by Newton refinement and Hessian-eigenvalue analysis. | Simulation exercise on numerical critical-point location. |
| `monte_carlo_ball_integral.py` | Monte Carlo integration of $f(x, y, z) = x^{2} + y^{2} + z^{2}$ over the unit ball in $\mathbb{R}^{3}$, with $95\%$ confidence intervals at three sample sizes. | Simulation exercise on Monte Carlo multiple integration. |

## Running

Each file's docstring states its dependencies and the command. All
files depend on `numpy`. Execute as:

```
uv run gradient_descent_rosenbrock.py
uv run volume_concentration.py
uv run critical_points.py
uv run monte_carlo_ball_integral.py
```

`volume_concentration.py` writes its result table to
`../data/volume_concentration.csv` if the data directory exists; the
data directory contains a frozen reference run from the chapter's
half-life-tagged date.

## License

Code is provided under the project's overall license (TBD) for
illustrative and pedagogical use. The values produced are
illustrative; production use requires verification against the
intended application.
