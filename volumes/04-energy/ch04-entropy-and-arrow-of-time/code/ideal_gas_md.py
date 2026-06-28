"""Minimal hard-disk molecular-dynamics simulation in two dimensions.

Initialises N disks in the left half of a square box with velocities drawn
from a Maxwell-Boltzmann distribution, integrates the dynamics with
event-driven-free velocity-Verlet plus elastic wall and pair reflection, and
records the number of particles in the left half and the coarse-grained entropy
over time. This is the reference implementation for the chapter project
(simulate a small ideal gas and measure the spontaneous entropy increase).

The pair collision handling here is the simplest correct version: a fixed-step
integrator with overlap resolution. It is adequate for a few hundred disks and
for demonstrating the entropy rise; it is not a production event-driven code.

Run:
    python ideal_gas_md.py
Outputs entropy_relaxation.csv (time, fraction_left, entropy_per_kB).
"""

from __future__ import annotations

import csv
import math
import random

K_B = 1.380649e-23  # J/K


def maxwell_velocity(mass: float, temperature: float) -> tuple[float, float]:
    """Two velocity components from the Maxwell-Boltzmann distribution.

    Each Cartesian component is Gaussian with variance k_B T / m.
    """
    sigma = math.sqrt(K_B * temperature / mass)
    return random.gauss(0.0, sigma), random.gauss(0.0, sigma)


def coarse_entropy(positions: list[tuple[float, float]], box: float, nbins: int) -> float:
    """Coarse-grained entropy per k_B from a spatial histogram.

    S / (N k_B) = - sum_b p_b ln p_b, where p_b is the occupied fraction in
    bin b. Returns the per-particle value so it saturates near ln(nbins-on-x)
    for a uniform spread.
    """
    counts = [0] * (nbins * nbins)
    n = len(positions)
    for x, y in positions:
        ix = min(int(x / box * nbins), nbins - 1)
        iy = min(int(y / box * nbins), nbins - 1)
        counts[iy * nbins + ix] += 1
    entropy = 0.0
    for c in counts:
        if c > 0:
            p = c / n
            entropy -= p * math.log(p)
    return entropy


def simulate(n: int = 400, box: float = 1.0, radius: float = 0.01,
             mass: float = 4.65e-26, temperature: float = 300.0,
             steps: int = 4000, dt: float = 2.0e-5,
             nbins: int = 4) -> list[tuple[float, float, float]]:
    """Run the simulation and return (time, fraction_left, entropy) samples."""
    rng = random.Random(20260624)
    random.seed(20260624)

    # initialise all particles in the left half, on a jittered grid to avoid overlap
    side = int(math.ceil(math.sqrt(n)))
    pos = []
    vel = []
    for i in range(n):
        gx = (i % side + 0.5) / side * (box / 2.0)
        gy = (i // side + 0.5) / side * box
        pos.append((gx + rng.uniform(-0.002, 0.002), gy + rng.uniform(-0.002, 0.002)))
        vel.append(maxwell_velocity(mass, temperature))

    samples = []
    for step in range(steps):
        # drift
        for i in range(n):
            x, y = pos[i]
            vx, vy = vel[i]
            x += vx * dt
            y += vy * dt
            # elastic wall reflection
            if x < radius:
                x = radius; vx = -vx
            elif x > box - radius:
                x = box - radius; vx = -vx
            if y < radius:
                y = radius; vy = -vy
            elif y > box - radius:
                y = box - radius; vy = -vy
            pos[i] = (x, y)
            vel[i] = (vx, vy)

        # naive pairwise elastic collisions (O(N^2); fine for N a few hundred)
        for i in range(n):
            for j in range(i + 1, n):
                dx = pos[j][0] - pos[i][0]
                dy = pos[j][1] - pos[i][1]
                d2 = dx * dx + dy * dy
                if 0.0 < d2 < (2 * radius) ** 2:
                    d = math.sqrt(d2)
                    nx, ny = dx / d, dy / d
                    dvx = vel[i][0] - vel[j][0]
                    dvy = vel[i][1] - vel[j][1]
                    approach = dvx * nx + dvy * ny
                    if approach > 0:
                        vel[i] = (vel[i][0] - approach * nx, vel[i][1] - approach * ny)
                        vel[j] = (vel[j][0] + approach * nx, vel[j][1] + approach * ny)

        if step % 20 == 0:
            t = step * dt
            frac_left = sum(1 for x, _ in pos if x < box / 2.0) / n
            s = coarse_entropy(pos, box, nbins)
            samples.append((t, frac_left, s))
    return samples


def main() -> None:
    samples = simulate()
    with open("entropy_relaxation.csv", "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["time_s", "fraction_left", "entropy_per_kB"])
        for t, f, s in samples:
            writer.writerow([f"{t:.6e}", f"{f:.4f}", f"{s:.4f}"])
    print(f"wrote {len(samples)} samples")


if __name__ == "__main__":
    main()
