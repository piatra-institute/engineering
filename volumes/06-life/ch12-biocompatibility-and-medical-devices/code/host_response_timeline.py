"""
Simulate the foreign-body response timeline at an implant surface.

Vol VI Ch 12, sec 12.2; simulation exercise 1.

The model is a coupled ODE system for four populations near the
implant surface:
- N(t): neutrophils (acute responders)
- M(t): macrophages
- F(t): foreign-body giant cells (fused macrophages)
- C(t): fibrous-capsule collagen density

The system has a fast-transient (neutrophil influx and clearance over
hours), a slow recruitment of macrophages (days), macrophage fusion to
giant cells (days to weeks), and a long-tail collagen deposition
(weeks to months) that asymptotes to a mature fibrous capsule density.

The model is illustrative; the canonical timeline is from
paper:v6c12-anderson-foreign-body-2008. Parameter values are
order-of-magnitude defaults; the rates carry one significant figure.
"""

from __future__ import annotations
import math


def step(y: list[float], dt: float, params: dict) -> list[float]:
    """
    Single Euler step of the four-population ODE system.
    State y = [N, M, F, C]; time t is encoded by the caller.
    """
    N, M, F, C = y

    # Neutrophil dynamics: rapid recruitment driven by adsorbed protein
    # cue (treated as constant during the acute phase, then decays);
    # rapid clearance through apoptosis.
    cue = params["acute_cue"] * math.exp(-params["cue_decay"]
                                          * params["t"])
    dN = cue * params["k_neutrophil_in"] \
        - params["k_neutrophil_out"] * N

    # Macrophage dynamics: recruited by chemotactic signals secreted
    # by activated neutrophils and by direct adsorbed-protein cues;
    # slow clearance.
    dM = params["k_macrophage_in"] * (N + 0.2 * cue) \
        - params["k_macrophage_out"] * M

    # Giant-cell formation: macrophage fusion proportional to the
    # square of macrophage density (cooperative fusion).
    dF = params["k_fusion"] * M * M - params["k_giant_out"] * F

    # Collagen deposition: stimulated by macrophages and giant cells;
    # asymptotes to a mature value via logistic-style growth.
    capsule_capacity = params["C_max"]
    dC = (params["k_collagen"] * (M + 2.0 * F)
          * (1.0 - C / capsule_capacity))

    return [N + dt * dN,
            M + dt * dM,
            F + dt * dF,
            C + dt * dC]


def simulate(days: float = 90.0, dt: float = 0.05) -> list[tuple]:
    """Return the trajectory over (days) at step (dt) days."""
    params = {
        "acute_cue": 10.0,
        "cue_decay": 0.5,         # per day
        "k_neutrophil_in": 5.0,
        "k_neutrophil_out": 8.0,  # neutrophils clear in hours
        "k_macrophage_in": 0.4,
        "k_macrophage_out": 0.05,
        "k_fusion": 0.001,
        "k_giant_out": 0.01,
        "k_collagen": 0.05,
        "C_max": 100.0,
        "t": 0.0,
    }

    y = [0.0, 0.0, 0.0, 0.0]    # initial populations
    traj: list[tuple] = []

    t = 0.0
    while t <= days:
        params["t"] = t
        traj.append((t, y[0], y[1], y[2], y[3]))
        y = step(y, dt, params)
        t += dt

    return traj


def main() -> None:
    traj = simulate(days=90.0, dt=0.05)

    # Report at characteristic checkpoints.
    checkpoints = [0.5, 1.0, 3.0, 7.0, 14.0, 30.0, 60.0, 90.0]
    print(f"{'t(d)':>8} {'N':>10} {'M':>10} {'F':>10} {'C':>10}")
    j = 0
    for cp in checkpoints:
        while j < len(traj) - 1 and traj[j][0] < cp:
            j += 1
        t, N, M, F, C = traj[j]
        print(f"{t:>8.2f} {N:>10.2f} {M:>10.2f} {F:>10.2f} {C:>10.2f}")


if __name__ == "__main__":
    main()
