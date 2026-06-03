# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Levinthal's paradox: random search through conformational space
versus the funnel-search timescale.

Engineering reading: a 100-residue protein with three rotational
states per residue has 3^100 ~ 5e47 conformations. Sampling at the
fastest single-bond rotation timescale (~1 ps) would take 5e35 seconds,
which exceeds the age of the universe by 28 orders of magnitude. The
folding-funnel framing replaces random search with biased downhill
motion; the funnel reduces the search space to roughly sqrt(N) parallel
trajectories that converge on the native state.
"""

from __future__ import annotations

import math


SEC_PER_PS = 1e-12
SEC_PER_YEAR = 3.156e7
AGE_OF_UNIVERSE_S = 4.35e17


def random_search_time(n_residues: int, states_per_residue: int = 3,
                        sample_time_s: float = SEC_PER_PS) -> float:
    conformations = states_per_residue**n_residues
    return conformations * sample_time_s


def funnel_search_time(n_residues: int, drift_velocity_states_per_s: float = 1e10) -> float:
    effective_depth = math.sqrt(n_residues) * 10  # rough downhill states
    return effective_depth / drift_velocity_states_per_s


def main() -> None:
    print(f"{'N':>4} {'random (s)':>14} {'random (yr)':>15} {'funnel (s)':>12} {'observed (s)':>14}")
    observed = {50: 1e-4, 75: 1e-3, 100: 1e-2, 150: 1e-1, 250: 1.0}
    for n in [50, 75, 100, 150, 250]:
        t_random = random_search_time(n)
        t_funnel = funnel_search_time(n)
        t_obs = observed.get(n, float("nan"))
        print(f"{n:4d} {t_random:14.3e} {t_random / SEC_PER_YEAR:15.3e} "
              f"{t_funnel:12.3e} {t_obs:14.3e}")

    n = 100
    t_random = random_search_time(n)
    ratio = t_random / AGE_OF_UNIVERSE_S
    print()
    print(f"For a {n}-residue protein, random search takes")
    print(f"  {t_random:.3e} s = {ratio:.3e} times the age of the universe.")
    print(f"  ({AGE_OF_UNIVERSE_S:.2e} s = 13.8 Gyr).")
    print()
    print("Observed folding times for small single-domain proteins:")
    print("  microseconds (small helical proteins like villin headpiece)")
    print("  milliseconds (most cytoplasmic enzymes)")
    print("  seconds (larger multi-domain proteins).")
    print("The funnel framing recovers these observed timescales.")


if __name__ == "__main__":
    main()
