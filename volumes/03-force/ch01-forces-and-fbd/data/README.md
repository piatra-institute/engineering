# Data for Volume III, Chapter 1 (Forces and free-body diagrams)

Reference tables backing the chapter's worked examples, figures, and
exercises. Values marked "working figure" are representative engineering
estimates, not standards; in any real design the coefficient or load is
measured for the actual contact under the actual conditions.

| File | Contents |
|------|----------|
| `friction_coefficients.csv` | Representative dry-sliding static and kinetic friction coefficients by material pair, with condition and a source note. |
| `ladder_slip_angles.csv` | Minimum floor coefficient `1/(2 tan theta)` for a uniform ladder against a smooth wall, tabulated against the floor angle. |
| `two_rope_tensions.csv` | Tension ratios `T1/mg` and `T2/mg` for a mass on two ropes at angles `(alpha, beta)` to the vertical, showing the divergence as the ropes flatten. |

The `two_rope_tensions.csv` and `ladder_slip_angles.csv` rows are
reproduced by the closed-form results in the chapter; `resolve_forces.py`
and `block_on_incline.py` in the `code/` folder regenerate the spot
checks.
