#!/usr/bin/env python3
"""Generalised eigenvalue problem for a multi-degree-of-freedom system.

Solves  (K - omega^2 M) phi = 0  for natural frequencies and mode shapes,
normalises the modes to unit modal mass, and verifies the
mass-orthogonality of the mode shapes. Demonstrated on the two-degree-of-
freedom system of the chapter's Calculation exercise 8.

Run:  python3 modal_2dof.py
"""

import numpy as np
from scipy.linalg import eigh


def modal_analysis(M, K):
    """Return (frequencies_rad, mode_shapes) for the system (M, K).

    Mode shapes are columns, mass-normalised so phi_i^T M phi_i = 1.
    """
    # eigh solves K phi = lambda M phi for symmetric M, K with M > 0.
    eigvals, eigvecs = eigh(K, M)
    omegas = np.sqrt(np.clip(eigvals, 0.0, None))
    return omegas, eigvecs


def check_orthogonality(M, phi):
    """Return phi^T M phi; should be the identity for mass-normalised modes."""
    return phi.T @ M @ phi


if __name__ == "__main__":
    # Calculation exercise 8: M = diag(2, 1), K = [[3, -1], [-1, 1]].
    M = np.array([[2.0, 0.0], [0.0, 1.0]])
    K = np.array([[3.0, -1.0], [-1.0, 1.0]])

    omegas, phi = modal_analysis(M, K)
    for i, w in enumerate(omegas):
        shape = phi[:, i] / phi[0, i]  # normalise to first component
        print(f"mode {i+1}: omega = {w:.4f} rad/s   "
              f"f = {w/(2*np.pi):.4f} Hz   shape = [{shape[0]:.3f}, {shape[1]:.3f}]")

    print("\nphi^T M phi (mass-orthogonality check):")
    print(np.round(check_orthogonality(M, phi), 6))

    # Larger demo: a 5-mass shear-building chain, equal masses and stiffness.
    n = 5
    m_floor, k_floor = 1.0e4, 1.5e7  # kg, N/m per storey
    Mb = m_floor * np.eye(n)
    Kb = np.zeros((n, n))
    for i in range(n):
        Kb[i, i] += k_floor
        if i + 1 < n:
            Kb[i, i] += k_floor
            Kb[i, i + 1] -= k_floor
            Kb[i + 1, i] -= k_floor
    wb, _ = modal_analysis(Mb, Kb)
    print("\n5-storey shear frame, natural frequencies (Hz):")
    print(np.round(wb / (2 * np.pi), 3))
