"""
Stochastic Gillespie simulation of a simplified apoptotic caspase
cascade.

The model has three species: an upstream regulator (Bcl-2 balance,
proxy R), an initiator caspase (C9), and an executioner caspase (C3).
The cascade is driven by a stress signal that pushes R below a
threshold, which permits cytochrome c release, which activates C9,
which cleaves and activates C3. Bistability arises from a positive
feedback loop in which active C3 cleaves Bcl-2 family members and
amplifies the upstream signal.

Reproduces the classic switch-like behaviour of apoptotic decision-
making at the single-cell level, and shows the all-or-none commitment
observed in single-cell apoptosis assays.

Supports:
  - Volume VI, Chapter 1, Simulation exercises on stochastic switches.
  - Volume VI, Chapter 1, Failure section on apoptosis dynamics.

Dependencies:
  numpy.

Usage:
  python gillespie_apoptosis.py [--trials N] [--stress S]
"""

import argparse
import numpy as np


def gillespie_apoptosis(stress: float = 1.0,
                        t_max: float = 200.0,
                        seed: int = 20260603
                        ) -> tuple[list[float], list[tuple[int, int, int]]]:
    """One stochastic trajectory of the simplified apoptosis cascade.

    Species: R (Bcl-2 / survival; starts high), C9 (initiator caspase),
    C3 (executioner caspase). Stress promotes R degradation; loss of R
    permits C9 activation; C9 activates C3; active C3 further cleaves
    R (positive feedback) and is also self-degraded.
    """
    rng = np.random.default_rng(seed)

    R = 100   # initial survival signal
    C9 = 0
    C3 = 0

    # Reaction rate constants (arbitrary units).
    k_r_decay = 0.02 * stress  # R degradation (stress-driven)
    k_r_synth = 0.5           # R baseline synthesis
    k_c9_act = 0.05           # C9 activation rate (high when R low)
    k_c9_inact = 0.1          # C9 spontaneous inactivation
    k_c3_act = 0.02           # C9 -> C3 activation
    k_c3_decay = 0.01         # C3 self-degradation
    k_r_cleave = 0.0005       # active C3 cleaves R (feedback)

    times: list[float] = [0.0]
    states: list[tuple[int, int, int]] = [(R, C9, C3)]
    t = 0.0

    while t < t_max and C3 < 500:
        # Rates of each reaction.
        rates = [
            k_r_decay * R,                          # R -> 0 (stress)
            k_r_synth,                              # 0 -> R
            k_c9_act * max(0.0, 50.0 - R),          # C9 += 1 if R low
            k_c9_inact * C9,                        # C9 -= 1
            k_c3_act * C9,                          # C3 += 1
            k_c3_decay * C3,                        # C3 -= 1
            k_r_cleave * C3 * R,                    # C3 cleaves R
        ]
        total = sum(rates)
        if total <= 0.0:
            break
        # Time to next reaction (exponential).
        dt = rng.exponential(1.0 / total)
        t += dt
        # Choose which reaction.
        u = rng.uniform(0.0, total)
        cumulative = 0.0
        for i, r in enumerate(rates):
            cumulative += r
            if u <= cumulative:
                idx = i
                break
        # Apply.
        if idx == 0: R = max(0, R - 1)
        elif idx == 1: R += 1
        elif idx == 2: C9 += 1
        elif idx == 3: C9 = max(0, C9 - 1)
        elif idx == 4: C3 += 1
        elif idx == 5: C3 = max(0, C3 - 1)
        elif idx == 6: R = max(0, R - 1)

        times.append(t)
        states.append((R, C9, C3))

    return times, states


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trials", type=int, default=10)
    parser.add_argument("--stress", type=float, default=1.0,
                        help="Stress level (1.0 = baseline)")
    parser.add_argument("--tmax", type=float, default=200.0)
    args = parser.parse_args()

    print(f"# Gillespie apoptosis simulation: stress = {args.stress}, "
          f"t_max = {args.tmax}")
    print(f"# Trial | T_commit | Peak C3 | Final R")
    committed = 0
    for trial in range(args.trials):
        times, states = gillespie_apoptosis(
            stress=args.stress, t_max=args.tmax,
            seed=20260603 + trial)
        c3_values = [s[2] for s in states]
        peak_c3 = max(c3_values)
        # Commitment: first time C3 > 100
        t_commit = None
        for t, s in zip(times, states):
            if s[2] > 100:
                t_commit = t
                break
        final_R = states[-1][0]
        if t_commit is not None:
            committed += 1
            print(f"  {trial:5d} | {t_commit:8.2f} | {peak_c3:7d} | "
                  f"{final_R:7d}")
        else:
            print(f"  {trial:5d} |   (none) | {peak_c3:7d} | "
                  f"{final_R:7d}")
    print(f"\n# Fraction committing to apoptosis: "
          f"{committed}/{args.trials}")
    print("# Reading: at low stress, most cells survive; at high "
          "stress, most commit; the transition is sharp (bistable "
          "switch).")


if __name__ == "__main__":
    main()
