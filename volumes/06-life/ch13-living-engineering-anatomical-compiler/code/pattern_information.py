"""
pattern_information.py

Shannon-entropy estimation of morphology specification for an idealised
voxel-grid tissue description.

For a grid of N voxels with K tissue-type labels per voxel, the
maximum specification entropy is N log2(K). The function below also
returns the entropy after applying a simple spatial smoothing
operation, illustrating how spatial correlation reduces effective
specification information.

Used by Vol VI Ch 13 Section 13.3 (estimation: salamander limb
information content).
"""

import numpy as np

def random_voxel_grid(shape, K, rng=None):
    """Random uniform tissue-type assignment over a voxel grid."""
    if rng is None:
        rng = np.random.default_rng(0)
    return rng.integers(0, K, size=shape)

def entropy_uniform(N, K):
    """Maximum entropy in bits: N voxels x log2 K labels."""
    return N * np.log2(K)

def empirical_entropy(grid):
    """Shannon entropy in bits of the marginal label distribution."""
    flat = grid.ravel()
    _, counts = np.unique(flat, return_counts=True)
    p = counts / counts.sum()
    return float(-np.sum(p * np.log2(p)))

def spatial_correlation_entropy(grid, neighbours=6):
    """Crude proxy: entropy after majority-vote smoothing reduces label
    diversity; not a rigorous mutual-information estimate, only used to
    illustrate that smoothing shrinks specification space."""
    # 3x3 mode filter
    from collections import Counter
    smoothed = grid.copy()
    pad = np.pad(grid, 1, mode="edge")
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            window = pad[i:i + 3, j:j + 3].ravel()
            cnt = Counter(window)
            smoothed[i, j] = cnt.most_common(1)[0][0]
    return empirical_entropy(smoothed)

def main():
    # Salamander forelimb at millimetre resolution: ~10^4 voxels, K=8
    N_mm = 10000
    K = 8
    bits_mm = entropy_uniform(N_mm, K)
    print(f"Millimetre-grid specification: ~{bits_mm:.0f} bits "
          f"({bits_mm / 8:.0f} bytes)")
    # Cell-resolution: 10^8 cells x 20 bits/cell
    N_cell = 10 ** 8
    bits_cell = N_cell * 20
    print(f"Cell-resolution specification: ~{bits_cell:.2e} bits "
          f"({bits_cell / 8 / 1e6:.0f} MB)")
    # Small empirical check
    rng = np.random.default_rng(0)
    grid = random_voxel_grid((40, 40), K, rng)
    print(f"Empirical marginal entropy of random 40x40 grid: "
          f"{empirical_entropy(grid):.3f} bits/voxel "
          f"(max {np.log2(K):.3f})")
    print(f"After spatial smoothing: "
          f"{spatial_correlation_entropy(grid):.3f} bits/voxel")

if __name__ == "__main__":
    main()
