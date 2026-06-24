# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Enumerate the acoustic eigenmodes of a rigid rectangular room.

For a rigid-walled box L_x x L_y x L_z the natural frequencies are

    f(nx, ny, nz) = (c / 2) * sqrt((nx/Lx)^2 + (ny/Ly)^2 + (nz/Lz)^2),

with non-negative integers (nx, ny, nz), not all zero. Modes split into
axial (one nonzero index), tangential (two), and oblique (three). This
script lists the modes below a cutoff, classifies them, and writes the
cumulative mode count to a CSV consumed by fig-room-modes.tex.

Run:  uv run room_modes.py
"""

from __future__ import annotations

import csv
import itertools
import math
from pathlib import Path

C = 343.0          # speed of sound in air, m/s
LX, LY, LZ = 5.0, 4.0, 2.5   # room dimensions, m
F_MAX = 200.0      # cutoff frequency, Hz


def mode_frequency(nx: int, ny: int, nz: int) -> float:
    return 0.5 * C * math.sqrt((nx / LX) ** 2 + (ny / LY) ** 2 + (nz / LZ) ** 2)


def classify(nx: int, ny: int, nz: int) -> str:
    nonzero = sum(1 for n in (nx, ny, nz) if n > 0)
    return {1: "axial", 2: "tangential", 3: "oblique"}[nonzero]


def enumerate_modes(f_max: float) -> list[tuple[float, int, int, int, str]]:
    # an index cannot exceed 2 L f_max / c along its own axis
    n_max = [int(math.ceil(2 * L * f_max / C)) + 1 for L in (LX, LY, LZ)]
    modes = []
    for nx, ny, nz in itertools.product(
        range(n_max[0] + 1), range(n_max[1] + 1), range(n_max[2] + 1)
    ):
        if nx == ny == nz == 0:
            continue
        f = mode_frequency(nx, ny, nz)
        if f <= f_max:
            modes.append((f, nx, ny, nz, classify(nx, ny, nz)))
    modes.sort(key=lambda row: row[0])
    return modes


def main() -> None:
    modes = enumerate_modes(F_MAX)
    counts = {"axial": 0, "tangential": 0, "oblique": 0}
    for _, _, _, _, kind in modes:
        counts[kind] += 1
    print(f"room {LX} x {LY} x {LZ} m, c = {C} m/s")
    print(f"modes below {F_MAX} Hz: {len(modes)}")
    print(f"  axial {counts['axial']}, tangential {counts['tangential']}, "
          f"oblique {counts['oblique']}")
    print("lowest ten modes:")
    for f, nx, ny, nz, kind in modes[:10]:
        print(f"  {f:6.1f} Hz  ({nx},{ny},{nz})  {kind}")

    out = Path(__file__).resolve().parent.parent / "data" / "room_mode_count.csv"
    with out.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["frequency_hz", "cumulative_count", "nx", "ny", "nz", "type"])
        for i, (f, nx, ny, nz, kind) in enumerate(modes, start=1):
            w.writerow([f"{f:.2f}", i, nx, ny, nz, kind])
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
