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

## Conventions

- Where randomness is used, the generator is seeded for reproducibility (per script).
- Output is human-readable text on stdout, not files.
- The numerical values are illustrative and reproducible from the code; they are not curated empirical datasets.

## Provenance

Editor's reference implementations. Verify against your own solver or modelling layer (CVXPY, JuMP, AMPL) when the answers matter for an engineering decision.
