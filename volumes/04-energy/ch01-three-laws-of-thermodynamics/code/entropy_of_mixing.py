"""Entropy of mixing for ideal gases, by formula and by particle simulation.

The closed-form mixing entropy per total mole is

    dS_mix = -R * sum_i x_i ln(x_i),

with x_i the mole fractions. The simulation distributes N labelled particles
across two halves of a box, lets them random-walk between halves, and tracks
the Gibbs-style mixing entropy estimated from the bin populations, which
approaches the formula value as the system equilibrates.

Run:
    python entropy_of_mixing.py
"""

import math
import random

R = 8.314  # J / (mol K)


def mixing_entropy_formula(n_a, n_b):
    n = n_a + n_b
    x_a, x_b = n_a / n, n_b / n
    return -R * (n_a * math.log(x_a) + n_b * math.log(x_b))


def simulate(n_particles=10000, steps=400, seed=0):
    """Two species A and B start segregated; track left/right composition."""
    rng = random.Random(seed)
    # species[i] in {0=A, 1=B}; side[i] in {0=left, 1=right}
    species = [0] * (n_particles // 2) + [1] * (n_particles // 2)
    side = [0] * (n_particles // 2) + [1] * (n_particles // 2)
    history = []
    for _ in range(steps):
        for _ in range(n_particles // 10):       # a fraction hop each step
            i = rng.randrange(n_particles)
            side[i] = rng.randint(0, 1)           # diffusive equilibration
        # mixing entropy estimate from species fractions on each side
        s = 0.0
        for sd in (0, 1):
            members = [species[i] for i in range(n_particles) if side[i] == sd]
            if not members:
                continue
            m = len(members)
            xa = members.count(0) / m
            xb = 1.0 - xa
            for x in (xa, xb):
                if x > 0:
                    s -= (m / n_particles) * x * math.log(x)
        history.append(R * s)
    return history


if __name__ == "__main__":
    s_formula = mixing_entropy_formula(0.5, 0.5)
    print(f"formula dS_mix (equimolar) = {s_formula:6.3f} J/K per mole")
    print(f"                          = {R * math.log(2):6.3f} J/K  (= R ln 2)")
    hist = simulate()
    print(f"simulated final estimate  = {hist[-1]:6.3f} J/K per mole "
          f"(approaches R ln 2 as mixing completes)")
