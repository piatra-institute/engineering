# Code assets — Volume I, Chapter 3 (Calibration and traceability)

## Files

| File | Purpose | Used by |
|---|---|---|
| `drift_recalibration.py` | Monte Carlo simulation of drift + random variation; computes out-of-tolerance probability vs recalibration interval. | Simulation exercise 1; figure 1.3 reference. |
| `chain_uncertainty.py` | Combined-uncertainty calculation for an N-link traceability chain; compares equal-link vs dominant-link configurations. | Simulation exercise 2. |
| `recalibration_cost.py` | Cost model for recalibration interval choice; identifies the cost-minimising interval. | Simulation exercise 3. |
| `control_chart.py` | Western-Electric SPC control-chart rules applied to daily verification readings; flags drift early. | Design exercise (verification routine). |

## Running

All files require only `numpy` and (for plotting, optional) `matplotlib`.
Run with `python <file>`. Each file's docstring lists details.
