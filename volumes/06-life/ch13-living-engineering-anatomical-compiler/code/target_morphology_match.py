"""
target_morphology_match.py

Image-similarity metrics for comparing a regenerated morphology to a
target morphology. Provides three metrics commonly used in
high-throughput phenotype scoring:

  * Intersection over union (IoU): area-based agreement.
  * Hausdorff distance: worst-case point-to-point boundary distance.
  * Centroid offset: simple translation error.

Used by Vol VI Ch 13 Section 13.4 (verification assays) to illustrate
that 'success' in a morphogenetic intervention needs a quantitative
shape metric, not a qualitative judgement.
"""

import numpy as np

def iou(mask_a, mask_b):
    """Intersection over union of two binary masks."""
    a, b = mask_a.astype(bool), mask_b.astype(bool)
    inter = np.logical_and(a, b).sum()
    union = np.logical_or(a, b).sum()
    if union == 0:
        return 1.0
    return float(inter) / float(union)

def centroid_offset(mask_a, mask_b):
    """Euclidean distance between centroids of two masks."""
    a, b = mask_a.astype(bool), mask_b.astype(bool)
    if not a.any() or not b.any():
        return np.inf
    ya, xa = np.nonzero(a)
    yb, xb = np.nonzero(b)
    ca = np.array([ya.mean(), xa.mean()])
    cb = np.array([yb.mean(), xb.mean()])
    return float(np.linalg.norm(ca - cb))

def hausdorff(mask_a, mask_b):
    """Symmetric Hausdorff distance between boundary points."""
    a, b = mask_a.astype(bool), mask_b.astype(bool)
    if not a.any() or not b.any():
        return np.inf
    pts_a = np.argwhere(a)
    pts_b = np.argwhere(b)
    # Distance from each point in A to nearest in B and vice versa
    def one_way(P, Q):
        # Brute force; OK for small masks
        dmax = 0.0
        for p in P:
            d = np.min(np.linalg.norm(Q - p, axis=1))
            if d > dmax:
                dmax = d
        return float(dmax)
    return max(one_way(pts_a, pts_b), one_way(pts_b, pts_a))

def main():
    # Two example masks: small target and a slightly displaced regenerated
    N = 40
    target = np.zeros((N, N), dtype=bool)
    regen = np.zeros((N, N), dtype=bool)
    # Target: disk centred at (20, 20), radius 8
    yy, xx = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
    target[(yy - 20) ** 2 + (xx - 20) ** 2 < 64] = True
    # Regen: disk shifted by 3 px
    regen[(yy - 22) ** 2 + (xx - 23) ** 2 < 64] = True
    print(f"IoU = {iou(target, regen):.3f}")
    print(f"Centroid offset = {centroid_offset(target, regen):.2f} px")
    print(f"Hausdorff distance = {hausdorff(target, regen):.2f} px")

if __name__ == "__main__":
    main()
