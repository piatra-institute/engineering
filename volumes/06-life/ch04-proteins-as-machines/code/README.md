# Vol VI Ch 4 code assets

Each script carries inline PEP 723 metadata. Run with `uv run <script>`
from any working directory; paths are resolved relative to the script.

- `michaelis_menten_fit.py`: nonlinear least-squares fit of v versus [S]
  with the Michaelis-Menten model, plus the Lineweaver-Burk
  linearisation as a teaching diagnostic. Reads
  `../data/mm_kinetics_example.csv`.

- `hill_cooperativity.py`: fits the Hill equation to oxygen-saturation
  curves for haemoglobin and myoglobin, returning Hill coefficient n
  and P50. Reads `../data/hemoglobin_oxygen_binding.csv`.

- `pdb_distance_calc.py`: parses a small PDB excerpt and computes the
  CA-CA distance matrix plus the C(i,O)-N(i+4,H) hydrogen-bond
  distances that diagnose an alpha-helix. Reads
  `../data/pdb_excerpt_1aki.pdb`.

- `motor_protein_stall_force.py`: implements the linear and Bell-model
  force-velocity relations for kinesin, myosin V, and dynein. Standalone
  (no data file).

- `levinthal_paradox.py`: computes the random-search and funnel-search
  folding timescales for a range of protein sizes. Standalone.

- `mwc_allostery.py`: two-state MWC model for an allosteric tetramer;
  computes Hill coefficient as a function of the allosteric parameters
  L and c. Standalone.

Run order for the chapter exercises: `michaelis_menten_fit.py` and
`hill_cooperativity.py` are the canonical fits; `pdb_distance_calc.py`
supports the structural-analysis project; `motor_protein_stall_force.py`
and `levinthal_paradox.py` support the estimation and design exercises.
