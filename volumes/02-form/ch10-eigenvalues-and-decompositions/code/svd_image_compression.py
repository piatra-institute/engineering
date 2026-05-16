"""
Truncated-SVD image compression with Eckart-Young error verification.

Reads a grayscale image, computes its SVD, reconstructs at several
ranks, and reports the spectral-norm and Frobenius-norm errors at each
rank against the Eckart-Young predictions sigma_{k+1} and
sqrt(sum_{i>k} sigma_i^2).

Supports:
  - Volume II, Chapter 10, Simulation exercise 3 (truncated-SVD image
    compression and error verification).

Dependencies:
  numpy, imageio (or Pillow)

Usage:
  python svd_image_compression.py path/to/image.png
                                  [--ranks 10 50 100 200]
                                  [--out-prefix recon]

If the image is colour, it is averaged to grayscale.
"""

from __future__ import annotations

import argparse
import os
import sys
import numpy as np


def load_grayscale(path: str) -> np.ndarray:
    """Load an image and return a float64 grayscale array (H, W)."""
    try:
        import imageio.v3 as iio  # type: ignore
        arr = iio.imread(path)
    except ImportError:
        try:
            from PIL import Image  # type: ignore
            arr = np.asarray(Image.open(path))
        except ImportError:
            sys.exit("Neither imageio nor Pillow is installed. "
                     "pip install imageio")
    if arr.ndim == 3:
        # Average the colour channels to a grayscale matrix.
        arr = arr[..., :3].mean(axis=-1)
    return arr.astype(np.float64)


def save_grayscale(path: str, arr: np.ndarray) -> None:
    """Save a float array as 8-bit PNG (clipped to [0, 255])."""
    try:
        import imageio.v3 as iio  # type: ignore
        clipped = np.clip(arr, 0, 255).astype(np.uint8)
        iio.imwrite(path, clipped)
    except ImportError:
        from PIL import Image  # type: ignore
        Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).save(path)


def truncated_svd(A: np.ndarray, k: int
                  ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Compute the rank-k truncation of A and return (U_k, s_k, V_k^T,
    full-singular-spectrum)."""
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    return U[:, :k], s[:k], Vt[:k, :], s


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=str)
    parser.add_argument("--ranks", type=int, nargs="+",
                        default=[10, 50, 100, 200])
    parser.add_argument("--out-prefix", type=str, default=None)
    args = parser.parse_args()

    A = load_grayscale(args.image)
    print(f"# Image shape: {A.shape}, dtype: {A.dtype}")
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    print(f"# Singular values: max={s[0]:.3e}, min={s[-1]:.3e}, "
          f"count={len(s)}")

    print()
    print(f"{'k':>5} {'storage_ratio':>14} {'spec_err':>12} "
          f"{'sigma_{k+1}':>12} {'frob_err':>12} {'tail_energy':>14}")
    H, W = A.shape
    for k in args.ranks:
        Ak = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]
        spec_err = np.linalg.norm(A - Ak, ord=2)
        frob_err = np.linalg.norm(A - Ak, ord="fro")
        # Eckart-Young predictions
        sigma_kp1 = s[k] if k < len(s) else 0.0
        tail = float(np.sqrt(np.sum(s[k:] ** 2)))
        # Storage ratio: (H + 1 + W) * k vs H * W
        storage = (H + 1 + W) * k / (H * W)
        print(f"{k:5d} {storage:14.4f} {spec_err:12.4e} {sigma_kp1:12.4e} "
              f"{frob_err:12.4e} {tail:14.4e}")
        if args.out_prefix is not None:
            base, _ = os.path.splitext(args.out_prefix)
            out = f"{base}_k{k}.png"
            save_grayscale(out, Ak)


if __name__ == "__main__":
    main()
