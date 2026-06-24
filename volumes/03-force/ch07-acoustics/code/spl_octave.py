# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Combine octave-band sound levels and apply A-weighting.

Given a set of octave-band sound-pressure levels in dB, this script
computes the overall unweighted level (energy sum), applies the standard
octave-band A-weighting offsets, and reports the overall A-weighted
level in dB(A). Levels combine on an energy basis:

    L_total = 10 * log10( sum_i 10^(L_i / 10) ).

Run:  uv run spl_octave.py
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

# standard octave-band centre frequencies (Hz)
BANDS = [31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000]

# octave-band A-weighting offsets (dB), IEC 61672 nominal values
A_OFFSET = [-39.4, -26.2, -16.1, -8.6, -3.2, 0.0, 1.2, 1.0, -1.1]

# example machine spectrum, unweighted band levels (dB SPL)
SPECTRUM = [82, 86, 84, 80, 78, 76, 74, 70, 62]


def energy_sum(levels: list[float]) -> float:
    return 10.0 * math.log10(sum(10.0 ** (L / 10.0) for L in levels))


def main() -> None:
    a_levels = [L + off for L, off in zip(SPECTRUM, A_OFFSET)]
    overall = energy_sum(SPECTRUM)
    overall_a = energy_sum(a_levels)
    print(f"overall unweighted level: {overall:5.1f} dB")
    print(f"overall A-weighted level: {overall_a:5.1f} dB(A)")
    print(f"A-weighting reduces the single number by "
          f"{overall - overall_a:4.1f} dB")
    print("band    dB     dB(A)")
    for f, L, La in zip(BANDS, SPECTRUM, a_levels):
        print(f"{f:6.1f} {L:6.1f} {La:7.1f}")

    out = Path(__file__).resolve().parent.parent / "data" / "octave_spectrum.csv"
    with out.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["band_hz", "level_db", "a_offset_db", "level_dba"])
        for f, L, off, La in zip(BANDS, SPECTRUM, A_OFFSET, a_levels):
            w.writerow([f, L, off, f"{La:.1f}"])
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
