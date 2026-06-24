"""Tresca and von Mises yield checks for a general 3D stress state.

Given the six independent components of the symmetric Cauchy stress tensor and a
uniaxial yield stress, report the principal stresses and whether the state has
yielded by each criterion. Used in section 3.6 and the simulation exercises.
"""

from __future__ import annotations

import numpy as np


def principal_stresses(sxx, syy, szz, sxy, syz, szx):
    """Eigenvalues of the stress tensor, sorted s1 >= s2 >= s3."""
    sigma = np.array([
        [sxx, sxy, szx],
        [sxy, syy, syz],
        [szx, syz, szz],
    ], dtype=float)
    eigs = np.linalg.eigvalsh(sigma)   # ascending, symmetric matrix
    return tuple(sorted(eigs, reverse=True))


def tresca_equivalent(s1, s2, s3):
    """Tresca equivalent stress = sigma_1 - sigma_3."""
    return s1 - s3


def von_mises_equivalent(s1, s2, s3):
    return np.sqrt(0.5 * ((s1 - s2) ** 2 + (s2 - s3) ** 2 + (s3 - s1) ** 2))


def check(sxx, syy, szz, sxy, syz, szx, sigma_y):
    s1, s2, s3 = principal_stresses(sxx, syy, szz, sxy, syz, szx)
    tr = tresca_equivalent(s1, s2, s3)
    vm = von_mises_equivalent(s1, s2, s3)
    return {
        "principals": (s1, s2, s3),
        "tresca": tr,
        "von_mises": vm,
        "yields_tresca": tr >= sigma_y,
        "yields_vonmises": vm >= sigma_y,
    }


if __name__ == "__main__":
    sigma_y = 250.0
    # Five states chosen to highlight the difference between the criteria.
    states = {
        "uniaxial 240":   (240, 0, 0, 0, 0, 0),     # both below, agree
        "pure shear 130": (0, 0, 0, 130, 0, 0),     # Tresca yields, vM borderline
        "biaxial 200/200":(200, 200, 0, 0, 0, 0),   # both criteria: sigma_eq=200
        "biaxial 200/-200":(200, -200, 0, 0, 0, 0), # large divergence
        "hydrostatic 500":(500, 500, 500, 0, 0, 0), # neither yields (no shear)
    }
    for name, st in states.items():
        r = check(*st, sigma_y)
        print(f"{name:18s} vM={r['von_mises']:6.1f} Tr={r['tresca']:6.1f} "
              f"| vM_yield={r['yields_vonmises']} Tr_yield={r['yields_tresca']}")
