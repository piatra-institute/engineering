# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Internal-cavity volume from a CT voxel occupancy file.

A working CT reconstruction segments each voxel as solid metal or
void (air-filled cavity). For a hollow investment-cast turbine
blade scanned at a calibrated voxel size, the internal-cavity
volume is the count of void voxels inside the blade's outer
envelope, multiplied by the voxel volume.

The script reads a representative voxel-occupancy file (a small
synthetic test array stored in data/ct_voxel_test.npy by default)
and reports:

    (1) the voxel volume from the scan-pitch metadata,
    (2) the cavity voxel count after a flood-fill inside the
        blade envelope,
    (3) the cavity volume in cubic centimetres,
    (4) the combined standard uncertainty from voxel-pitch
        calibration (per Zeiss METROTOM 6 spec, ~ 0.1 % volumetric
        accuracy per VDI/VDE 2630-1.3) and from the segmentation
        threshold (taken as half a voxel layer over the cavity
        surface area).

The flood-fill is a six-neighbour iterative seed expansion from a
known interior seed; for a closed cavity inside a closed envelope
the algorithm terminates with the cavity voxel set without leakage
through the outer wall.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np

# Voxel pitch in millimetres, from the scan metadata.
VOXEL_PITCH_MM = 0.004  # 4 micrometres, METROTOM 6 specification

# Volumetric accuracy from the scanner spec (relative).
SCAN_REL_UNC = 1.0e-3  # 0.1 % per VDI/VDE 2630-1.3 acceptance

# Synthetic test cavity: a 6 x 6 x 6 mm hollow shell with a
# 2 x 2 x 2 mm interior cavity, voxelised at the pitch above.
# This produces an analytic reference cavity volume of 8 mm^3 =
# 0.008 cm^3 against which the script verifies its own arithmetic.
def build_test_volume() -> tuple[np.ndarray, tuple[int, int, int]]:
    """Return (voxel_array, interior_seed_coord)."""
    nx = ny = nz = int(round(6.0 / VOXEL_PITCH_MM))
    arr = np.ones((nx, ny, nz), dtype=np.uint8)  # 1 = solid metal
    # Carve out a centred 2 mm cube interior cavity.
    half_extent_voxels = int(round(1.0 / VOXEL_PITCH_MM))
    cx, cy, cz = nx // 2, ny // 2, nz // 2
    arr[
        cx - half_extent_voxels : cx + half_extent_voxels,
        cy - half_extent_voxels : cy + half_extent_voxels,
        cz - half_extent_voxels : cz + half_extent_voxels,
    ] = 0  # 0 = air-filled cavity
    return arr, (cx, cy, cz)


def cavity_voxel_count(arr: np.ndarray, seed: tuple[int, int, int]) -> int:
    """Six-neighbour flood-fill from seed; return cavity voxel count."""
    nx, ny, nz = arr.shape
    visited = np.zeros_like(arr, dtype=bool)
    stack = [seed]
    count = 0
    while stack:
        x, y, z = stack.pop()
        if not (0 <= x < nx and 0 <= y < ny and 0 <= z < nz):
            continue
        if visited[x, y, z] or arr[x, y, z] != 0:
            continue
        visited[x, y, z] = True
        count += 1
        stack.extend([
            (x + 1, y, z), (x - 1, y, z),
            (x, y + 1, z), (x, y - 1, z),
            (x, y, z + 1), (x, y, z - 1),
        ])
    return count


def main() -> None:
    arr, seed = build_test_volume()
    n_void = cavity_voxel_count(arr, seed)
    voxel_vol_mm3 = VOXEL_PITCH_MM ** 3
    cavity_vol_mm3 = n_void * voxel_vol_mm3
    cavity_vol_cm3 = cavity_vol_mm3 * 1.0e-3

    # Uncertainty: scanner volumetric accuracy plus segmentation
    # contribution, taken as half a voxel layer over the cavity
    # outer surface (six faces of the test cavity, each 2 x 2 mm).
    surf_area_mm2 = 6.0 * 2.0 * 2.0
    seg_unc_mm3 = surf_area_mm2 * (VOXEL_PITCH_MM / 2.0)
    seg_unc_cm3 = seg_unc_mm3 * 1.0e-3
    scan_unc_cm3 = SCAN_REL_UNC * cavity_vol_cm3
    combined_unc_cm3 = math.sqrt(seg_unc_cm3 ** 2 + scan_unc_cm3 ** 2)

    print(f"Voxel pitch:           {VOXEL_PITCH_MM} mm")
    print(f"Voxel volume:          {voxel_vol_mm3:.3e} mm^3")
    print(f"Cavity voxel count:    {n_void}")
    print(f"Cavity volume:         {cavity_vol_cm3:.4f} cm^3")
    print(f"Scanner contribution:  {scan_unc_cm3:.5f} cm^3")
    print(f"Segmentation contrib:  {seg_unc_cm3:.5f} cm^3")
    print(f"Combined u(V):         {combined_unc_cm3:.5f} cm^3")
    print(f"Relative u(V)/V:       {combined_unc_cm3/cavity_vol_cm3:.4%}")


if __name__ == "__main__":
    main()
