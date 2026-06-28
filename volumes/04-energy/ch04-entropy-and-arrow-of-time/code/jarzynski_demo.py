"""Verify the Jarzynski equality for a dragged overdamped particle.

A particle in a harmonic trap whose centre is moved at finite speed performs
non-equilibrium work W that varies from realisation to realisation. The
Jarzynski equality states that the exponential average of the work recovers the
equilibrium free-energy difference exactly:

    < exp(-W / k_B T) > = exp(-Delta F / k_B T),

even though the process is irreversible and < W > >= Delta F. Here the trap
stiffness is constant, so Delta F = 0, and the test is that the exponential
average of the work returns one despite a positive mean work.

The dynamics are overdamped Langevin (Brownian) in a reduced unit system where
k_B T = 1 and the trap stiffness k = 1; lengths and times are dimensionless.
"""

from __future__ import annotations

import math
import random


def run_trajectory(rng: random.Random, v_pull: float, n_steps: int,
                   dt: float, gamma: float = 1.0, kT: float = 1.0,
                   k_trap: float = 1.0) -> float:
    """One overdamped-Langevin pull; returns the accumulated work.

    The trap centre moves at constant speed v_pull. Work is integrated as the
    force from the moving trap acting through the centre displacement,
    dW = -k_trap (x - x_center) dx_center.
    """
    x = rng.gauss(0.0, math.sqrt(kT / k_trap))  # start in equilibrium
    x_center = 0.0
    work = 0.0
    noise_amp = math.sqrt(2.0 * gamma * kT * dt)
    for _ in range(n_steps):
        # work increment: dW = (dH/d lambda) d lambda with lambda the trap
        # centre and H = 0.5 k (x - lambda)^2, so dH/d lambda = -k (x - lambda).
        dxc = v_pull * dt
        work += -k_trap * (x - x_center) * dxc
        x_center += dxc
        # overdamped Langevin update of the particle at the new trap centre
        force = -k_trap * (x - x_center)
        x += force / gamma * dt + noise_amp / gamma * rng.gauss(0.0, 1.0)
    return work


def main() -> None:
    rng = random.Random(20260624)
    realisations = 20000
    v_pull = 0.5
    n_steps = 200
    dt = 0.01

    works = [run_trajectory(rng, v_pull, n_steps, dt) for _ in range(realisations)]
    mean_work = sum(works) / realisations
    exp_avg = sum(math.exp(-w) for w in works) / realisations
    delta_F_estimate = -math.log(exp_avg)

    print(f"realisations          {realisations}")
    print(f"< W >                 {mean_work:.4f}  (>= Delta F, dissipation)")
    print(f"< exp(-W) >           {exp_avg:.4f}  (Jarzynski; target 1.0)")
    print(f"Delta F estimate      {delta_F_estimate:.4f}  (target 0.0)")


if __name__ == "__main__":
    main()
