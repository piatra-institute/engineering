# Code assets for Vol VI Ch 5 (Tissue and organ engineering)

Five Python scripts, each runnable with `uv run <script>.py` thanks to
PEP 723 inline metadata. The scripts implement the quantitative
arguments of the chapter at a level a working engineer can audit and
extend.

- `krogh_oxygen_diffusion.py`: analytic and finite-difference solutions
  of the steady-state oxygen-diffusion equation through a slab of
  metabolically active tissue, with the working
  $100$-$200\,\mu\text{m}$ diffusion-limit reproduction and a
  sensitivity sweep over the consumption rate and the diffusion
  coefficient.
- `tissue_stress_strain_fit.py`: fits the Mooney-Rivlin and Fung
  exponential constitutive models to synthetic uniaxial stress-strain
  data; reports parameters, residual norm, and goodness-of-fit
  diagnostics. Used in the simulation exercise.
- `murrays_law_branching.py`: computes the daughter-vessel radius
  ratio and optimal bifurcation angles for a symmetric or asymmetric
  bifurcation under Murray's law, and tabulates the radius hierarchy
  for a three-generation tree.
- `scaffold_porosity_calc.py`: computes scaffold porosity, specific
  surface area, and connectivity for a model unit cell (sphere
  packing) under varying pore size and wall thickness, against the
  pore-size design windows for dermal, bone, vascular, and nerve
  applications.
- `cell_seeding_density.py`: estimates the total cell count required
  to populate an engineered construct at native tissue density, the
  scale-up factor required from a starting cell sample (skin punch
  biopsy, peripheral blood draw), and the expected time-to-target
  cell number given typical expansion-rate assumptions.

Each script writes results to stdout in a fixed format that the
chapter text or a downstream notebook can quote without
re-derivation. None require external data; the working data is at
`data/`.
