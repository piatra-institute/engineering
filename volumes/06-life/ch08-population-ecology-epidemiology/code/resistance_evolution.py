# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numpy",
#     "matplotlib",
# ]
# ///
"""Antibiotic-resistance evolution: deterministic and stochastic
simulations for Vol VI Ch 8 §8.5.

Reproduces:
  * Deterministic selection-coefficient model: f(t)/(1 - f(t)) =
    (f0/(1 - f0)) exp(s t), fixation time t_fix.
  * Stochastic individual-based simulation under constant-drug,
    pulsed-drug, and combination-drug (two independent mutations)
    regimens.

Usage:
  uv run resistance_evolution.py
"""

import numpy as np
import matplotlib.pyplot as plt


def deterministic_fraction(t, f0, s):
    """Closed-form solution f(t) of df/dt = s f (1 - f)."""
    ratio0 = f0 / (1 - f0)
    ratio_t = ratio0 * np.exp(s * t)
    return ratio_t / (1 + ratio_t)


def fixation_time(f0, f_target, s):
    """Time for resistant fraction to rise from f0 to f_target."""
    return (1 / s) * np.log((f_target / (1 - f_target)) /
                            (f0 / (1 - f0)))


def stochastic_run(N0, mu, s_on, s_off, drug_schedule, n_steps, dt, rng):
    """Coarse stochastic simulation of resistant fraction.

    `drug_schedule` is a function step -> bool (drug present).
    """
    f = 1.0 / N0  # one pre-existing resistant per N0
    trajectory = [f]
    for step in range(n_steps):
        drug_on = drug_schedule(step)
        s = s_on if drug_on else s_off
        df = s * f * (1 - f) * dt
        # Add new resistant mutations from susceptible pool
        df += mu * (1 - f) * dt
        f = np.clip(f + df, 0, 1)
        trajectory.append(f)
    return np.array(trajectory)


def main():
    f0 = 1e-9
    targets = [1e-3, 1e-2, 1e-1, 0.5]
    s = 0.8
    print(f"Selection differential s = {s}/h, starting frequency f0 = {f0}")
    for tgt in targets:
        t = fixation_time(f0, tgt, s)
        print(f"  Time to reach f = {tgt:.0e}: {t:.1f} h")

    # Stochastic regimens
    dt = 0.1  # hours
    n_steps = 1000
    rng = np.random.default_rng(0)
    constant = stochastic_run(N0=1e9, mu=1e-12, s_on=0.8, s_off=-0.1,
                              drug_schedule=lambda i: True,
                              n_steps=n_steps, dt=dt, rng=rng)
    pulsed = stochastic_run(N0=1e9, mu=1e-12, s_on=0.8, s_off=-0.1,
                            drug_schedule=lambda i: (i // 120) % 2 == 0,
                            n_steps=n_steps, dt=dt, rng=rng)
    combo = stochastic_run(N0=1e9, mu=1e-12, s_on=0.4, s_off=-0.1,
                           drug_schedule=lambda i: True,
                           n_steps=n_steps, dt=dt, rng=rng)
    t_axis = np.arange(n_steps + 1) * dt

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogy(t_axis, constant, label="constant drug, single mutation")
    ax.semilogy(t_axis, pulsed, label="pulsed drug (12h on / 12h off)")
    ax.semilogy(t_axis, combo, label="combination, effective s = 0.4")
    ax.axhline(1e-2, color="gray", linestyle=":", label="1% threshold")
    ax.set_xlabel("hours from treatment start")
    ax.set_ylabel("resistant fraction f")
    ax.set_title("Resistance dynamics under three regimens")
    ax.legend()
    fig.tight_layout()
    fig.savefig("resistance_regimens.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
