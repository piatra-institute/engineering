"""
Estimate lifetime stress cycles on a knee implant from gait data.

Vol VI Ch 12, Estimation 12.1.

The model assumes a population-mean gait of 6,000 to 12,000 steps per day
(values cited from epidemiology; the model takes a parameter), a knee
implant lifetime of 15 to 30 years, and a load spectrum in which each
step contributes one major cycle (heel strike to toe-off) plus
approximately three minor cycles (single-leg stance oscillation).
Damage is accumulated using Miner's rule against an assumed S-N curve
for the bearing material (UHMWPE polyethylene insert or cobalt-chromium
femoral component, selectable).

References:
- Charnley, J. "The long-term results of low-friction arthroplasty,"
  paper:v6c12-charnley-low-friction-1972 (gait-cycle conventions).
- Callister & Rethwisch, "Materials Science and Engineering,"
  text:v6c12-callister-materials-2018 (Miner's rule, S-N curves).
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence
import math


# Default parameters; the docstrings give the source.
STEPS_PER_DAY_MEAN = 8000          # population mean, ambulatory adult
STEPS_PER_DAY_HIGH = 12000          # active patient cohort
STEPS_PER_DAY_LOW = 4000            # sedentary or post-surgical cohort

MINOR_CYCLES_PER_STEP = 3.0          # heuristic load-spectrum factor


@dataclass
class LoadCycle:
    """A single load category with stress amplitude and per-step count."""
    name: str
    sigma_amplitude_mpa: float
    cycles_per_step: float


def total_cycles(years: float, steps_per_day: float,
                 cycle_count: float) -> float:
    """Return total cycles over the implant lifetime."""
    days = years * 365.25
    return days * steps_per_day * cycle_count


def miner_damage(load_cycles: Sequence[LoadCycle],
                 years: float,
                 steps_per_day: float,
                 sn_curve: callable) -> float:
    """
    Accumulate Miner's-rule damage for a load spectrum.

    sn_curve(sigma_mpa) returns the allowable cycles N to failure at
    that stress amplitude. Damage D = sum_i n_i / N_i; failure at D = 1.
    """
    total = 0.0
    for lc in load_cycles:
        n_i = total_cycles(years, steps_per_day, lc.cycles_per_step)
        N_i = sn_curve(lc.sigma_amplitude_mpa)
        if N_i <= 0:
            return float("inf")
        total += n_i / N_i
    return total


def basquin_sn(sigma_f_prime_mpa: float, b: float) -> callable:
    """
    Basquin-form S-N curve N = (sigma_a / sigma_f')^(1/b).
    Standard for metallic implant alloys; b typically -0.1 to -0.12 for
    surgical CoCr and Ti6Al4V. See callister-materials-2018.
    """
    def sn(sigma_mpa: float) -> float:
        if sigma_mpa <= 0:
            return float("inf")
        return (sigma_mpa / sigma_f_prime_mpa) ** (1.0 / b)
    return sn


def main() -> None:
    spectrum = [
        LoadCycle("heel-strike major", sigma_amplitude_mpa=80.0,
                  cycles_per_step=1.0),
        LoadCycle("single-leg stance",  sigma_amplitude_mpa=45.0,
                  cycles_per_step=MINOR_CYCLES_PER_STEP),
    ]

    # CoCr S-N parameters, illustrative (see Callister 2018, Ch 9).
    sn = basquin_sn(sigma_f_prime_mpa=1200.0, b=-0.10)

    for steps in (STEPS_PER_DAY_LOW, STEPS_PER_DAY_MEAN,
                  STEPS_PER_DAY_HIGH):
        for years in (10, 15, 20, 30):
            n_total = sum(
                total_cycles(years, steps, lc.cycles_per_step)
                for lc in spectrum
            )
            D = miner_damage(spectrum, years, steps, sn)
            print(f"steps/day={steps:>5}, years={years:>2}  "
                  f"total cycles={n_total:.2e}  Miner D={D:.3f}")


if __name__ == "__main__":
    main()
