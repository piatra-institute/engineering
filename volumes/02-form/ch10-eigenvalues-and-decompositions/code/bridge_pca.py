"""
Principal Component Analysis of the eight-gauge bridge-monitoring
dataset (data/bridge_strain_gauges.csv), worked end to end:

  1. Centre the data; report the conditioning of X_c and of the
     covariance C = X_c^T X_c / (m - 1).
  2. Compute the PCA by SVD of the centred matrix (the reportable
     route) and, for contrast, by eigendecomposition of C.
  3. Report singular values, explained-variance ratios, cumulative
     retention, and the PC1/PC2 loadings (rows of V).
  4. Apply the Marchenko-Pastur noise-floor test on the standardised
     data: eigenvalues of the correlation matrix above lambda_+ are
     genuine components; those inside [lambda_-, lambda_+] are noise.

The numbers printed here are the ones quoted in section 10 (the
bridge-monitoring case study) of Volume II, Chapter 10.

Supports:
  - Chapter case study: structural-health PCA on a real-shaped
    multivariate engineering dataset.

Dependencies:
  numpy

Run:
  python bridge_pca.py
"""

import csv
import numpy as np


def load(path="../data/bridge_strain_gauges.csv"):
    with open(path) as fh:
        reader = csv.reader(fh)
        header = next(reader)
        rows = [[float(v) for v in r] for r in reader]
    return header, np.asarray(rows)


def main():
    gauges, X = load()
    m, n = X.shape
    Xc = X - X.mean(axis=0)

    # SVD route (the reportable one: no squaring of the conditioning).
    U, S, Vt = np.linalg.svd(Xc, full_matrices=False)
    var = S**2 / (m - 1)               # eigenvalues of the covariance C
    evr = var / var.sum()              # explained-variance ratios
    cum = np.cumsum(evr)

    kappa_Xc = S[0] / S[-1]
    kappa_C = kappa_Xc**2

    print(f"samples m = {m}, features n = {n}")
    print(f"cond(X_c)  = {kappa_Xc:8.1f}")
    print(f"cond(C)    = {kappa_C:8.1f}   (= cond(X_c)^2)")
    print("singular values:", np.round(S, 2))
    print("variances      :", np.round(var, 2))
    print("explained ratio:", np.round(evr, 4))
    print("cumulative     :", np.round(cum, 4))
    print("PC1 loadings   :", dict(zip(gauges, np.round(Vt[0], 3))))
    print("PC2 loadings   :", dict(zip(gauges, np.round(Vt[1], 3))))

    # Cross-check: eigendecomposition of C must agree with the SVD.
    C = Xc.T @ Xc / (m - 1)
    eigvals, _ = np.linalg.eigh(C)
    eigvals = np.sort(eigvals)[::-1]
    print("eig(C) vs sigma^2/(m-1) agree:",
          np.allclose(eigvals, var, atol=1e-6))

    # Marchenko-Pastur noise floor on the standardised data.
    Xs = Xc / Xc.std(axis=0, ddof=1)
    corr_eigs = np.sort(np.linalg.eigvalsh(Xs.T @ Xs / (m - 1)))[::-1]
    gamma = n / m
    lam_plus = (1 + np.sqrt(gamma))**2
    lam_minus = (1 - np.sqrt(gamma))**2
    print(f"gamma = n/m = {gamma:.4f}; MP bulk = "
          f"[{lam_minus:.3f}, {lam_plus:.3f}]")
    print("correlation eigenvalues:", np.round(corr_eigs, 3))
    n_signal = int(np.sum(corr_eigs > lam_plus))
    print(f"components above the noise floor: {n_signal}")


if __name__ == "__main__":
    main()
