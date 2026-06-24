# Code for Chapter 10: Fluid statics

All scripts carry no third-party dependencies and run under `uv`.

- `standard_atmosphere.py` integrates the International Standard Atmosphere
  from sea level to 32 km and compares it with the single-scale-height
  isothermal model. Produces the values in `data/isa_profile.csv` and the
  curves in `figures/fig-atmosphere.tex`.
- `submerged_surface.py` computes the resultant force and centre of pressure
  on flat vertical or inclined rectangles (Section 10.4 worked examples).
- `metacentre.py` finds the floating draft and metacentric height of a
  homogeneous rectangular box and classifies it stable or unstable
  (Section 10.5).
- `manometer.py` traces the hydrostatic path for open-end, differential, and
  inclined manometers (Section 10.3).

Run any script with, for example:

    uv run volumes/03-force/ch10-fluid-statics/code/standard_atmosphere.py
