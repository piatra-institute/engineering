"""
UPGMA tree construction from a small pairwise-distance matrix.

UPGMA (unweighted pair group method with arithmetic mean) is a simple
distance-based hierarchical-clustering algorithm that produces an
ultrametric tree. The implementation iteratively finds the closest pair
of clusters, joins them, and updates the distance matrix with the
weighted mean distance from the new cluster to all remaining clusters.

The output is a Newick string. The example uses a five-taxon 16S/18S
distance matrix that approximately reproduces the topology in figure
fig-phylo-tree.tex.

Dependencies:
  numpy.

Usage:
  python phylo_distance.py

Supports Volume VI, Chapter 11, Section 11.6 (phylogenetics) and the
calculation exercise on UPGMA tree construction.
"""

from __future__ import annotations

import numpy as np


def upgma(distance_matrix: np.ndarray, labels: list[str]) -> str:
    """Construct a UPGMA tree and return its Newick representation.

    Args:
        distance_matrix: symmetric n x n pairwise distance matrix.
        labels: list of n leaf labels.

    Returns:
        Newick string with branch lengths.
    """
    D = distance_matrix.astype(float).copy()
    n = D.shape[0]
    # Cluster sizes and Newick subtrees; heights are last join heights.
    clusters = list(labels)
    sizes = [1] * n
    heights = [0.0] * n

    # Mask distance from a cluster to itself.
    np.fill_diagonal(D, np.inf)

    while len(clusters) > 1:
        # Find the closest pair (i, j) with i < j.
        idx_flat = int(np.argmin(D))
        size_now = D.shape[0]
        i, j = divmod(idx_flat, size_now)
        if i > j:
            i, j = j, i
        d_ij = D[i, j]
        new_height = d_ij / 2.0

        # Branch lengths from each child to the new internal node.
        bl_i = new_height - heights[i]
        bl_j = new_height - heights[j]
        new_label = f"({clusters[i]}:{bl_i:.4f},{clusters[j]}:{bl_j:.4f})"
        new_size = sizes[i] + sizes[j]

        # Distance of new cluster to each remaining k.
        new_row = np.zeros(size_now)
        for k in range(size_now):
            if k == i or k == j:
                continue
            new_row[k] = (sizes[i] * D[i, k] + sizes[j] * D[j, k]) / new_size

        # Build new D and arrays with i replaced by the merged cluster and j dropped.
        keep = [k for k in range(size_now) if k != j]
        D_new = D[np.ix_(keep, keep)].copy()
        new_index = keep.index(i)
        for kk, k in enumerate(keep):
            if k == i:
                continue
            D_new[new_index, kk] = new_row[k]
            D_new[kk, new_index] = new_row[k]
        np.fill_diagonal(D_new, np.inf)
        D = D_new

        clusters = [clusters[k] for k in keep]
        sizes = [sizes[k] for k in keep]
        heights = [heights[k] for k in keep]
        clusters[new_index] = new_label
        sizes[new_index] = new_size
        heights[new_index] = new_height

    return clusters[0] + ";"


def main() -> None:
    labels = ["Aspergillus", "Saccharomyces", "Ecoli", "Bsubtilis", "Halobacterium"]
    # Approximate distances in substitutions per site.
    D = np.array(
        [
            [0.00, 0.13, 0.62, 0.58, 0.72],
            [0.13, 0.00, 0.59, 0.61, 0.74],
            [0.62, 0.59, 0.00, 0.23, 0.68],
            [0.58, 0.61, 0.23, 0.00, 0.66],
            [0.72, 0.74, 0.68, 0.66, 0.00],
        ]
    )
    newick = upgma(D, labels)
    print("UPGMA tree (Newick):")
    print(newick)


if __name__ == "__main__":
    main()
