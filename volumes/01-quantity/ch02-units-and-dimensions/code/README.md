# Code assets — Volume I, Chapter 2 (Units and dimensions)

Executable supporting code for the chapter's worked examples and
exercises.

## Files

| File | Purpose | Used by |
|---|---|---|
| `drag_curve.py` | Morsi-Alexander piecewise correlation for sphere drag coefficient; plots $C_D(\mathrm{Re})$ over $10^{-1}$-$5\times10^4$. | Simulation exercise (drag curve); figure 1.3. |
| `pendulum_pi.py` | Numerical verification of the Buckingham-pi result for a simple pendulum across 10 $(L, g)$ combinations. | Simulation exercise (pendulum pi). |
| `wave_speed.py` | Finite-difference wave-equation solver verifying $v = \sqrt{T/\mu}$. | Simulation exercise (wave speed). |
| `dim_check.py` | Symbolic dimensional-consistency checker; given an equation as a SymPy expression in dimensional units, returns whether the equation balances dimensionally. | Diagnosis exercises (incorrect-equation detection); general debugging aid. |

## Running

Each file's docstring lists dependencies and the command to run.
`drag_curve.py` and `pendulum_pi.py` require `numpy` and `matplotlib`.
`wave_speed.py` requires `numpy`. `dim_check.py` requires `sympy`.
