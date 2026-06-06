# Code assets, Volume II, Chapter 15 (Optimisation)

Each script is self-contained and runnable with `uv run`:

```
uv run code/<script>.py
```

## Files

| File | Purpose | Used by |
|---|---|---|
| `gradient_descent.py` | Gradient descent on the elongated quadratic $f(x_1, x_2) = \tfrac{1}{2}(x_1^2 + 100 x_2^2)$; sweeps step sizes and reports convergence vs divergence at the predicted stability threshold $\eta L < 2$. | Section 15.5; Simulation exercise 1. |
| `rosenbrock_methods.py` | Vanilla gradient descent, momentum (decay 0.9), and Adam on the Rosenbrock function from $(-1, 1)$; reports iteration counts to reach $f < 10^{-4}$. | Section 15.6; Simulation exercises 2 and 5. |
| `lp_diet.py` | A five-food, three-nutrient toy diet LP solved via `scipy.optimize.linprog` with HiGHS; prints the optimal diet, binding constraints, and shadow prices. Reads `data/diet_problem.csv`. | Section 15.3; Simulation exercise 4 (template). |
| `lp_production_simplex.py` | The two-variable production LP of Section 15.3 (max $3x_1 + 5x_2$ under three machine-hour limits) solved primal-and-dual via `scipy.optimize.linprog` with HiGHS; prints $x^* = (2, 6)$, profit 36, and the shadow prices $(0, 1.5, 1.0)$. | Section 15.3 worked LP. |
| `knapsack_branch_and_bound.py` | The four-item 0/1 knapsack of Section 15.7 solved by branch-and-bound with a fractional-knapsack LP-relaxation bound; pure stdlib. Prints the optimum (220), an optimal item set, and the visited-node count against the full decision tree. | Section 15.7 worked branch-and-bound. |
| `markowitz_portfolio.py` | The mean-variance portfolio QP of Section 15.3 solved over a grid of risk-aversion values; traces the efficient frontier and reports the active-set table under the no-short constraint. | Section 15.3 worked QP. |
| `truss_sizing_lp.py` | The six-member cantilever-truss sizing LP of the structural case study, solved via `scipy.optimize.linprog`; prints optimal areas, the binding constraint per member (stress vs floor), total mass, and shadow prices. | Truss case-study section. |
| `gauss_newton_calibration.py` | Gauss-Newton, Levenberg-Marquardt, and gradient descent (all from scratch) on the three-parameter exponential-decay calibration $\hat{y}(t) = A e^{-kt} + C$; prints the fitted parameters, residual histories, the condition number of $J^\top J$, and the small-residual diagnostic. Seeded. | Nonlinear-least-squares case study. |

## Conventions

- Where randomness is used, the generator is seeded for reproducibility (per script).
- Output is human-readable text on stdout, not files.
- The numerical values are illustrative and reproducible from the code; they are not curated empirical datasets.

## Provenance

Editor's reference implementations. Verify against your own solver or modelling layer (CVXPY, JuMP, AMPL) when the answers matter for an engineering decision.
