# Code assets — Volume VI, Chapter 2 (Metabolism and bioenergetics)

Self-contained Python scripts that support the chapter's worked
examples, the project, and a subset of the simulation and estimation
exercises. Each script runs to completion on the standard library
(scipy is optional, only `metabolic_flux_lp.py` uses it for an
auxiliary check). No external data files required.

## Files

| File | Section / role |
|---|---|
| `atp_turnover_estimate.py` | Section 2.1; the chapter project. Three independent estimates of an adult human's daily ATP turnover (food energy, cell count, oxygen consumption) and a reconciled mean. |
| `glycolysis_atp_balance.py` | Section 2.2; figure `fig-glycolysis-ledger`. Per-step ATP / NADH ledger and running pathway free-energy sum. |
| `nernst_membrane_potential.py` | Section 2.2 (chemiosmosis); the derivation exercise on proton-motive force. Nernst equation, PMF decomposition, and the minimum proton stoichiometry per ATP at ATP synthase. |
| `metabolic_flux_lp.py` | Section 2.4 (MFA); the simulation exercise on FBA. Toy six-reaction, four-metabolite network solved analytically and (if scipy is installed) verified with `scipy.optimize.linprog`. |
| `photosynthesis_efficiency.py` | Sections 2.3, 2.6; the estimation exercise on algal photobioreactor productivity. Stage-wise photosynthesis efficiency from quantum maximum to field-integrated biomass productivity. |

## Provenance

All scripts are editor-generated for pedagogical use. Numerical inputs
(standard free energies, basal cell counts, oxygen consumption rates)
are drawn from the references cited in the chapter text and the
sibling `data/` directory; the docstrings cite the relevant section.
No experimental data, no clinical data, no PHI.
