# Code assets, Volume VI Chapter 3

Five Python scripts supporting the chapter. All use the standard
library only (no pandas, numpy, or matplotlib dependency) so they run
on a clean Python 3.10+ installation without setup.

## Scripts

| Script                          | Purpose                                                                |
|---------------------------------|------------------------------------------------------------------------|
| `dna_information_content.py`    | Shannon entropy per base, single-base and dinucleotide. Confirms the 2-bit/bp upper bound and quantifies the deviation in real genomes. |
| `central_dogma_kinetics.py`     | Two-variable mRNA + protein ODE with measured E. coli rate constants. Supports a step-induction option to read off the protein time constant. |
| `wright_fisher_drift.py`        | The chapter project's simulation. Sweeps population size, reports fixation probability and mean time. Selection-coefficient option. |
| `mutation_rate_estimator.py`    | Estimates per-base mutation rate from parent-offspring trio counts. Wilson confidence interval. Synthetic-trio mode for validation. |
| `codon_optimization.py`         | CAI computation against an E. coli reference and a greedy re-coder that maximises CAI while preserving the protein sequence. |

## Running the scripts

Each script accepts `--help`. Quick sanity checks:

```
python dna_information_content.py
# expect H1 ~ 2.000 on a 1e6-base random sequence

python central_dogma_kinetics.py
# expect steady-state mRNA ~30 copies, protein ~520,000 copies

python wright_fisher_drift.py --N 10,100,1000 --reps 1000
# expect p_fix ~ 0.5 each row, mean fix time ~ 2.8 N

python mutation_rate_estimator.py --simulate
# expect estimated mu within an order of magnitude of 1.2e-8

python codon_optimization.py
# expect a CAI between 0.4 and 0.8 for the demo ORF
```

## Conventions

- **No matplotlib.** Plots that would normally be the script's output
  are written instead as TikZ figures under `../figures/`. The scripts
  print summary numbers to stdout; the figure files use those numbers
  (or the data tables under `../data/`) directly.
- **No numpy.** The math involved (entropy, Poisson sampling, linear
  ODE) is small enough that the standard `math` and `random` modules
  suffice. Removing the numpy dependency keeps the scripts portable.
- **No biopython.** The chapter does not need a full sequence-analysis
  stack; the small genetic-code table in `codon_optimization.py` and
  the FASTA reader in `dna_information_content.py` cover the work.
- **Deterministic seeds.** Every script that uses randomness exposes a
  `--seed` flag and seeds explicitly so the reader can reproduce a run
  exactly.

## Provenance

The codon-frequency table in `codon_optimization.py` is abridged from
the Codon Usage Database (Nakamura, 2000), accessed via the kazusa.or.jp
mirror in 2024. The mRNA half-life default (5 min) and the protein
half-life default (20 h) are E. coli order-of-magnitude values from
Selinger et al. 2003 and Maier et al. 2011 respectively, cited in the
chapter.
