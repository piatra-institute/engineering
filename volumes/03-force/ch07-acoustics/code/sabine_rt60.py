# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Predict reverberation time from room geometry and surface absorption.

Computes the total absorption A = sum_i S_i * alpha_i over the room's
surfaces and returns the Sabine reverberation time T60 = 0.161 V / A,
plus the Eyring estimate that is preferred when the mean absorption
coefficient is large.

Run:  uv run sabine_rt60.py
"""

from __future__ import annotations

import math

# room: 5 x 4 x 2.5 m
LX, LY, LZ = 5.0, 4.0, 2.5
VOLUME = LX * LY * LZ

# surfaces as (name, area_m2, absorption_coefficient at 500 Hz)
SURFACES = [
    ("floor (carpet)", LX * LY, 0.30),
    ("ceiling (plaster)", LX * LY, 0.05),
    ("walls (painted)", 2 * (LX + LY) * LZ, 0.06),
    ("furniture + drapery", 8.0, 0.50),
    ("window glass", 3.0, 0.18),
]


def sabine_t60(volume: float, absorption: float) -> float:
    return 0.161 * volume / absorption


def eyring_t60(volume: float, total_area: float, mean_alpha: float) -> float:
    # Eyring: replaces alpha with -ln(1 - alpha_bar)
    return 0.161 * volume / (-total_area * math.log(1.0 - mean_alpha))


def main() -> None:
    total_area = sum(area for _, area, _ in SURFACES)
    absorption = sum(area * alpha for _, area, alpha in SURFACES)
    mean_alpha = absorption / total_area

    t_sab = sabine_t60(VOLUME, absorption)
    t_eyr = eyring_t60(VOLUME, total_area, mean_alpha)

    print(f"room volume     {VOLUME:6.1f} m^3")
    print(f"total surface   {total_area:6.1f} m^2")
    print(f"absorption A    {absorption:6.2f} m^2-sabin")
    print(f"mean alpha      {mean_alpha:6.3f}")
    print(f"Sabine  T60     {t_sab:6.2f} s")
    print(f"Eyring  T60     {t_eyr:6.2f} s")
    print("breakdown of absorption by surface:")
    for name, area, alpha in SURFACES:
        print(f"  {name:24s} {area * alpha:6.2f} m^2-sabin")


if __name__ == "__main__":
    main()
