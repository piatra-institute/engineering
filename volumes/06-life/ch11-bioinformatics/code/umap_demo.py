"""
UMAP demonstration on a small synthetic feature matrix.

Loads the small counts matrix from ../data/counts_matrix.csv (100 features
x 20 cells), normalises (log1p of CPM), runs PCA, and visualises in two
dimensions. The point of the demo is to show that a UMAP plot is a
visualisation aid, not a metric: clusters in the plot are the output of
upstream graph-based clustering, not the cause of it.

Dependencies:
  numpy, matplotlib, scikit-learn, optionally umap-learn. If umap-learn is
  not installed, falls back to PCA for the 2D embedding.

Usage:
  python umap_demo.py

Supports Volume VI, Chapter 11, Section 11.4 (transcriptomics) and the
simulation exercise on dimension reduction.
"""

from __future__ import annotations

import os


def load_counts(path: str):
    """Load a CSV counts matrix; first column is feature names."""
    import csv

    with open(path) as f:
        reader = csv.reader(f)
        header = next(reader)
        cell_ids = header[1:]
        rows = list(reader)
    feature_names = [row[0] for row in rows]
    counts = [[float(x) for x in row[1:]] for row in rows]
    return feature_names, cell_ids, counts


def log_cpm(counts):
    """Normalise to counts-per-million then take log1p."""
    import numpy as np

    arr = np.array(counts, dtype=float).T  # cells x features
    library_size = arr.sum(axis=1, keepdims=True)
    library_size[library_size == 0] = 1.0
    cpm = arr / library_size * 1e6
    return np.log1p(cpm)


def embed_2d(matrix):
    """Return a 2D embedding using UMAP if available, else PCA."""
    try:
        import umap  # type: ignore

        reducer = umap.UMAP(n_neighbors=5, min_dist=0.3, random_state=0)
        return reducer.fit_transform(matrix), "UMAP"
    except ImportError:
        from sklearn.decomposition import PCA

        pca = PCA(n_components=2, random_state=0)
        return pca.fit_transform(matrix), "PCA fallback"


def main() -> None:
    data_path = os.path.join(
        os.path.dirname(__file__), "..", "data", "counts_matrix.csv"
    )
    if not os.path.exists(data_path):
        print(f"Counts matrix not found at {data_path}; nothing to do.")
        return

    feature_names, cell_ids, counts = load_counts(data_path)
    print(f"Loaded {len(feature_names)} features x {len(cell_ids)} cells")

    matrix = log_cpm(counts)
    print(f"Normalised matrix shape: {matrix.shape}")

    embedded, method = embed_2d(matrix)
    print(f"Embedding method: {method}")
    for cid, (x, y) in zip(cell_ids, embedded):
        print(f"  {cid:8s}  ({x:+.3f}, {y:+.3f})")


if __name__ == "__main__":
    main()
