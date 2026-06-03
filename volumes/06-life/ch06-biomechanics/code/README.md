# Code assets for Vol VI Ch 6 (Biomechanics)

Six Python scripts, each runnable with `uv run <script>.py` thanks to
PEP 723 inline metadata. They implement the chapter's quantitative
arguments at the working-engineer level: a reader who wants to audit
or extend a number can read the script, change a parameter, and rerun.

- `jump_peak_force.py`: estimates the peak ground-reaction force,
  patello-femoral compression, and quadriceps tension during a vertical
  jump from a synthetic (or measured) accelerometer trace. Closes the
  project's analysis chain end-to-end.
- `hill_muscle_model.py`: implements the Hill three-element muscle
  model (force-length, force-velocity, parallel passive elastic) with
  the Zajac normalisation. Used in the force-length / force-velocity
  figure and in the gastrocnemius push-off estimate.
- `murray_branching.py`: tabulates the radius hierarchy, total
  cross-sectional area, blood velocity, and Reynolds number across the
  twenty-four-generation symmetric arterial tree under Murray's law.
- `pressure_volume_loop.py`: computes the left-ventricular PV-loop
  summary (stroke volume, ejection fraction, stroke work, cardiac
  output, cardiac power) at rest, during heavy exercise, and in heart
  failure with reduced ejection fraction.
- `lung_compliance_fit.py`: fits a Salazar-Knowles sigmoid to the
  static lung P-V curve, computes compliance at FRC and TLC, and
  estimates the work and power of breathing at rest and exercise.
- `mooney_rivlin_fit.py`: fits the Mooney-Rivlin and one-term Ogden
  hyperelastic models to a synthetic soft-tissue uniaxial data set and
  reports parameters, residuals, and a small comparison table. Used in
  the soft-tissue constitutive-model section.

All scripts write to stdout in a fixed format; none require external
data beyond the CSVs in `data/`.
