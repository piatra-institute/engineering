# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy", "scipy"]
# ///
"""Two-variable production LP of Section 15.3, primal and dual.

maximise   3 x1 + 5 x2
subject to x1       <= 4     (machine A)
                2 x2 <= 12    (machine B)
           3 x1 + 2 x2 <= 18  (machine C)
           x1, x2 >= 0

The text solves this graphically (vertex enumeration) and by the
simplex method by hand, reaching x* = (2, 6) with profit 36. This
script confirms the optimum with a library LP solver, prints the
binding constraints, and reports the dual variables (shadow prices)
y* = (0, 1.5, 1.0) on machines A, B, C.

scipy.optimize.linprog minimises, so the objective is negated; the
reported optimal value is negated back to the maximisation value.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import linprog

# Negated objective for minimisation form.
c = np.array([-3.0, -5.0])

# A_ub x <= b_ub
A_ub = np.array(
    [
        [1.0, 0.0],   # machine A
        [0.0, 2.0],   # machine B
        [3.0, 2.0],   # machine C
    ]
)
b_ub = np.array([4.0, 12.0, 18.0])

RESOURCES = ["machine A", "machine B", "machine C"]


def main() -> None:
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0, None), (0, None)],
                  method="highs")
    x = res.x
    profit = -res.fun
    slack = b_ub - A_ub @ x
    # HiGHS returns dual values (marginals) for the inequality rows.
    duals = -res.ineqlin.marginals  # sign convention -> shadow prices

    print("Production LP, two variables")
    print(f"optimal x*    = ({x[0]:.3f}, {x[1]:.3f})")
    print(f"optimal profit = {profit:.3f}")
    print()
    print(f"{'resource':>12}  {'slack':>8}  {'shadow price':>13}  binding")
    for name, s, y in zip(RESOURCES, slack, duals):
        binding = "yes" if abs(s) < 1e-9 else "no"
        print(f"{name:>12}  {s:>8.3f}  {y:>13.3f}  {binding:>7}")


if __name__ == "__main__":
    main()
