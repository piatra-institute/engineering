# Chapter 7 — code assets

Reference implementations supporting Volume VI Chapter 7 (Nervous and
immune systems as control systems). All scripts are standalone, use
only NumPy and Matplotlib, and run with `python3 <script>.py` from this
directory. Outputs are PNG figures; numbers used in the chapter prose
are reproducible.

## Files

- `lif_neuron.py` — leaky integrate-and-fire neuron (the project).
  Reproduces tonic firing, the f-I curve, spike-frequency adaptation,
  and the response to noisy input.

- `hodgkin_huxley.py` — full Hodgkin-Huxley squid-axon model.
  Reproduces a single action potential from a brief current pulse and
  the firing pattern under sustained current. Sweeps the leak
  conductance to find the all-or-nothing transition.

- `cable_equation_solve.py` — finite-difference solver for the passive
  cable equation. Demonstrates exponential attenuation with space
  constant lambda and the transition from passive to active
  propagation.

- `synaptic_dynamics.py` — alpha-function synaptic conductance,
  short-term plasticity (facilitation and depression), and the
  excitatory-postsynaptic-potential summation that produces a spike at
  the postsynaptic neuron.

- `clonal_expansion.py` — deterministic ODE and Gillespie stochastic
  models of antigen-specific lymphocyte expansion. Reproduces the
  $\sim 10^4$-fold expansion in 7 days and the timing of the antibody
  titre peak.

## Reproducibility

Each script seeds NumPy with `np.random.seed(2026)` so that stochastic
runs are deterministic across machines. Outputs are written to the
current directory; remove `*.png` before re-running for a clean rebuild.
