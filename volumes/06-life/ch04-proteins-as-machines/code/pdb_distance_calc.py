# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Parse a PDB excerpt and compute residue-residue alpha-carbon distance
matrix, plus the C(i,O)--N(i+4,H) hydrogen-bond distances that
diagnose an alpha-helix.

Reads ../data/pdb_excerpt_1aki.pdb (lysozyme backbone, residues 1-12).

Engineering reading: the alpha-helix is identified by the C=O of
residue i hydrogen-bonding to the N-H of residue i+4 at a distance of
approximately 2.9 angstroms (O to N) or 1.9 angstroms (O to H). The
3.6 residues per turn and 1.5 angstroms rise per residue give the
helix geometry. A right-handed helix is identified by the sign of the
cross product of successive backbone vectors.
"""

from __future__ import annotations

import pathlib

import numpy as np


HERE = pathlib.Path(__file__).resolve().parent
PDB = HERE.parent / "data" / "pdb_excerpt_1aki.pdb"


def parse_pdb(path: pathlib.Path) -> dict[tuple[int, str], np.ndarray]:
    """Return {(resnum, atom_name): xyz} for ATOM records."""
    coords: dict[tuple[int, str], np.ndarray] = {}
    with path.open() as fp:
        for line in fp:
            if not line.startswith("ATOM"):
                continue
            atom = line[12:16].strip()
            res = int(line[22:26])
            x = float(line[30:38])
            y = float(line[38:46])
            z = float(line[46:54])
            coords[(res, atom)] = np.array([x, y, z])
    return coords


def ca_distance_matrix(coords: dict[tuple[int, str], np.ndarray]) -> np.ndarray:
    residues = sorted({res for (res, atom) in coords if atom == "CA"})
    n = len(residues)
    matrix = np.zeros((n, n))
    for i, ri in enumerate(residues):
        for j, rj in enumerate(residues):
            matrix[i, j] = float(
                np.linalg.norm(coords[(ri, "CA")] - coords[(rj, "CA")])
            )
    return matrix


def helix_hbond_distances(coords: dict[tuple[int, str], np.ndarray]) -> list[tuple[int, float]]:
    residues = sorted({res for (res, atom) in coords if atom == "CA"})
    out: list[tuple[int, float]] = []
    for r in residues:
        if (r, "O") in coords and (r + 4, "N") in coords:
            d = float(np.linalg.norm(coords[(r, "O")] - coords[(r + 4, "N")]))
            out.append((r, d))
    return out


def main() -> None:
    coords = parse_pdb(PDB)
    n_ca = sum(1 for k in coords if k[1] == "CA")
    print(f"Loaded {n_ca} CA atoms from {PDB.name}")

    matrix = ca_distance_matrix(coords)
    print("\nCA-CA distance matrix (angstroms), residues 1-12:")
    header = "     " + " ".join(f"{i + 1:5d}" for i in range(n_ca))
    print(header)
    for i in range(n_ca):
        row = " ".join(f"{matrix[i, j]:5.1f}" for j in range(n_ca))
        print(f"{i + 1:3d} | {row}")

    print("\nCandidate alpha-helix hydrogen bonds (C=O of i to N-H of i+4):")
    hbonds = helix_hbond_distances(coords)
    for r, d in hbonds:
        marker = "  (helical)" if 2.5 < d < 3.5 else ""
        print(f"  O({r:2d}) to N({r + 4:2d}): {d:.2f} A{marker}")


if __name__ == "__main__":
    main()
