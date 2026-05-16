# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Combined uncertainty of a gauge-block stack.

A length standard built by wringing several gauge blocks together has
two uncertainty contributions per block: the calibration uncertainty
of the block (typically reported on its certificate) and the wringing
contribution (the residual thickness of the wrung film between
blocks, treated as zero-mean with a small standard uncertainty per
joint).

This script computes the combined standard uncertainty of the stack
under both contributions and reports the contribution breakdown.
The values used are illustrative; replace them with the certificates
of the actual blocks in use.
"""

from __future__ import annotations

import math

# Per-block calibration standard uncertainty, in micrometres.
# Typical Grade 0 ceramic gauge blocks: roughly +- 0.10 micrometre
# expanded at k = 2 for 1 to 25 mm blocks (illustrative figure).
CAL_U_K1_PER_BLOCK_UM = 0.05  # u (standard uncertainty), micrometres

# Wringing film standard uncertainty per joint, micrometres.
# An ideal wring leaves a film of order nanometres; the practical
# uncertainty is conservatively a few tens of nanometres per joint.
WRING_U_PER_JOINT_UM = 0.02  # u, micrometres


def stack_uncertainty(block_lengths_mm: list[float]) -> dict:
    """Compute the combined standard uncertainty of a stack.

    Args:
        block_lengths_mm: nominal lengths of each block, in mm.

    Returns:
        dict with stack length (mm), per-block calibration term,
        wringing term, combined u, expanded U at k = 2.
    """
    n_blocks = len(block_lengths_mm)
    n_joints = max(0, n_blocks - 1)

    stack_mm = sum(block_lengths_mm)

    # Calibration uncertainties add in quadrature when blocks are
    # independently calibrated (the standard assumption when blocks
    # come from a single set with independent certificates).
    u_cal_um = math.sqrt(n_blocks) * CAL_U_K1_PER_BLOCK_UM
    u_wring_um = math.sqrt(n_joints) * WRING_U_PER_JOINT_UM

    u_combined_um = math.sqrt(u_cal_um**2 + u_wring_um**2)
    U_k2_um = 2.0 * u_combined_um

    return {
        "stack_length_mm": stack_mm,
        "n_blocks": n_blocks,
        "n_joints": n_joints,
        "u_calibration_um": u_cal_um,
        "u_wringing_um": u_wring_um,
        "u_combined_um": u_combined_um,
        "U_k2_um": U_k2_um,
        "U_k2_relative": U_k2_um / (stack_mm * 1000.0),
    }


def main() -> None:
    # Example: build a 67.825 mm reference by stacking 50 + 12 + 5 + 0.8 + 0.025
    blocks_mm = [50.0, 12.0, 5.0, 0.8, 0.025]
    r = stack_uncertainty(blocks_mm)

    print(f"stack length        : {r['stack_length_mm']:.4f}  mm")
    print(f"number of blocks    : {r['n_blocks']}")
    print(f"number of joints    : {r['n_joints']}")
    print(f"u (calibration)     : {r['u_calibration_um']:.4f}  um")
    print(f"u (wringing)        : {r['u_wringing_um']:.4f}  um")
    print(f"u (combined, k=1)   : {r['u_combined_um']:.4f}  um")
    print(f"U (expanded, k=2)   : {r['U_k2_um']:.4f}  um")
    print(f"relative U (k=2)    : {r['U_k2_relative']:.2e}")


if __name__ == "__main__":
    main()
