# Code assets — Volume II, Chapter 10 (Eigenvalues and decompositions)

Executable supporting code for the chapter's worked examples,
simulation exercises, and project. Files are runnable from this
directory with a recent Python 3 interpreter and the dependencies
listed in each file's header.

## Files

| File | Purpose | Used by |
|---|---|---|
| `power_iteration.py` | Power iteration on a random symmetric matrix with Rayleigh-quotient convergence tracking; symmetric deflation for the next eigenpair. | Simulation exercises 1 and 2; section 10.6. |
| `svd_image_compression.py` | Truncated-SVD compression of a grayscale image with Eckart-Young error verification at several ranks. | Simulation exercise 3; section 10.8. |
| `pca_three_routes.py` | PCA computed three ways (covariance eigendecomposition, power iteration with deflation, SVD of the centred data matrix) with conditioning report and library comparison. | Chapter project. |
| `markov_stationary.py` | Stationary distribution of a finite-state Markov chain by both eigendecomposition and direct power iteration; reports the mixing time from the second-largest eigenvalue. | Simulation exercise 4; section 10.5. |
| `pagerank_small.py` | PageRank on the four-page web of section 10.6 by power iteration on the Google matrix, with dangling-node and teleportation corrections and a spectral-gap check. | Section 10.6 worked example; PageRank diagnosis exercise. |
| `inverse_iteration.py` | Fixed-shift inverse iteration (eigenvalue nearest a shift) and Rayleigh-quotient iteration (cubic convergence on a symmetric matrix), reproducing the two worked examples in section 10.6. | Section 10.6 worked examples. |
| `machine_reliability.py` | Five-state machine-reliability Markov chain: stationary distribution three ways (eigenvector, linear solve, power iteration), mixing time, long-run availability, and annual downtime cost. | Case study, section "machine availability as a steady-state problem". |
| `bridge_pca.py` | End-to-end PCA of the eight-gauge bridge-monitoring dataset: conditioning of `X_c` and `C`, SVD route cross-checked against covariance eigendecomposition, explained-variance and loadings, and the Marchenko-Pastur noise-floor test. | Case study, section "structural-health PCA"; `data/bridge_strain_gauges.csv`. |

## Running

Each file's docstring states its dependencies and the command to run.
`power_iteration.py`, `pca_three_routes.py`, and `markov_stationary.py`
require only `numpy`. `svd_image_compression.py` additionally requires
`imageio` (or `Pillow`) to read and write the image file.

Default seeds reproduce the worked example numerics quoted in the
chapter prose; passing `--seed N` changes the random matrix or
synthesised dataset.

## License

Code is provided under the project's overall license (TBD) for
illustrative and pedagogical use. The numerical values produced are
illustrative; production use requires verification against the
intended application.
