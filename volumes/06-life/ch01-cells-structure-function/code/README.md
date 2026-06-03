# Code assets — Volume VI, Chapter 1 (Cells: structure and function)

Executable supporting code for the chapter's worked examples and
exercises. Files are runnable from this directory with a recent Python
3 interpreter and the dependencies listed in each file's header.

## Files

| File | Purpose | Used by |
|---|---|---|
| `membrane_voltage_nernst.py` | Nernst and Goldman-Hodgkin-Katz equilibrium-potential calculation; reduction check that GHK collapses to Nernst when only one ion is permeable. | Derivation exercises on the Nernst and GHK equations. |
| `cell_size_scaling.py` | Surface-to-volume ratio for spheres at canonical cell sizes; biconcave-disc comparison; diffusion-limited radius for O2. | Calculation exercises on SA/V; estimation exercise on cell-size bounds. |
| `diffusion_timescale.py` | Tabulates Fickian diffusion timescale `tau = L^2 / (6 D)` across lengthscales (bacterial radius, animal cell radius, axon) and species (small molecules, proteins, vesicles). Includes crowding-corrected cytoplasmic diffusion coefficients. | Estimation exercise on diffusion time; design exercise on cellular logistics. |
| `na_k_pump_atp_cost.py` | ATP cost per action potential as a function of axon dimensions and membrane capacitance; cell-level resting ATP budget; cardiomyocyte mitochondrial accounting. | Calculation exercises on Na+/K+ pump flux and ATP throughput. |
| `gillespie_apoptosis.py` | Stochastic (Gillespie) simulation of a simplified apoptotic caspase cascade with positive feedback. Demonstrates bistable, switch-like commitment to apoptosis under stress. | Simulation exercises; failure section's discussion of apoptotic decision-making. |

## Running

Each file's docstring states its dependencies and the command to run.
All files require only `numpy`. The Gillespie simulator runs in
seconds for default trial counts.

## License

Code is provided under the project's overall license (TBD) for
illustrative and pedagogical use. The values produced are
illustrative; production use requires verification against the
intended application.
