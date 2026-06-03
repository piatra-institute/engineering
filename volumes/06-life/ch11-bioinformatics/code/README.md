# Code assets — Volume VI, Chapter 11 (Bioinformatics)

## Files

| File | Purpose | Used by |
|---|---|---|
| `needleman_wunsch.py` | Dynamic-programming global pairwise alignment with linear gap penalty; produces score matrix and traceback. | Section 11.1; calculation exercise 1; project phase 1. |
| `blast_evalue.py` | Karlin-Altschul E-value calculator and sweep over database size. | Section 11.1; derivation exercise 1; simulation exercise 1. |
| `variant_filter.py` | Filter pipeline applied to a small synthetic VCF: quality, depth, strand bias, mapping quality; emits a PASS-only VCF. | Section 11.3; design exercise 1; project phase 3. |
| `umap_demo.py` | UMAP demonstration on a small synthetic counts matrix (digits substitute), showing the difference between clustering and embedding. | Section 11.4; simulation exercise 2. |
| `batch_correct.py` | ComBat-style empirical-Bayes batch correction on a simulated two-batch expression dataset; PCA before and after. | Section 11.8; diagnosis exercise 1; failure-analysis exercise 1. |
| `phylo_distance.py` | UPGMA tree construction from a 16S distance matrix; outputs Newick string. | Section 11.6; calculation exercise 5. |

## Running

All files require only the Python standard library plus `numpy` and `matplotlib`
(optional, for plotting). `umap_demo.py` requires `umap-learn` and
`scikit-learn`. Each file is runnable as `python <file>`. Each file's docstring
lists details.

The data files referenced from these scripts live in `../data/`; paths are
relative to the script directory.
