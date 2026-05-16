# Data assets — Volume II, Chapter 6 (Integration)

## Files

| File | Source | Used by |
|---|---|---|
| `hammer_profile.csv` | Editor's measured cross-section profile of a 680 g framing hammer, calliper-measured at 5 mm axial intervals; columns `x_mm` (axial position from the head face) and `area_mm2` (cross-section area perpendicular to the long axis). | `code/moment_of_inertia_profile.py`; chapter project (method ii); diagnosis exercise on hammer discrepancy. |
| `quadrature_speedometer.csv` | Editor's transcription of the worked estimation block (section 6.1) of a car speedometer read every 5 minutes for a 30-minute trip; columns `t_min` (minute from start) and `v_kmh` (speed in km/h). | Estimation exercise on the speedometer; chapter project cross-check on numerical integration of measured data. |

## Provenance

`hammer_profile.csv`: editor's own measurement, taken with a digital
calliper of $\pm 0.05\,\text{mm}$ resolution. Areas are computed
assuming the cross-section is well-approximated by an ellipse with
the two calliper-measured semi-axes; areas of the head, neck, and
handle were measured separately and summed.

`quadrature_speedometer.csv`: transcribed verbatim from the
estimation block in chapter 6.1.

These are reference data for in-text computations and exercises, not
results of a scientific measurement programme.
