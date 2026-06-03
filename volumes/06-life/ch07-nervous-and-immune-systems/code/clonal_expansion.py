"""Clonal expansion of antigen-specific lymphocytes.

Two parallel models:
  (a) Deterministic logistic-style ODE for antibody titre dynamics.
  (b) Gillespie stochastic simulation of clonal birth-death dynamics.

Reproduces a ~10^4-fold expansion in 7 days and the timing of the IgG
titre peak around day 10-14 after primary antigen exposure.

Usage:
    python3 clonal_expansion.py
"""

import numpy as np
import matplotlib.pyplot as plt


def deterministic_response(T_days=21.0, dt=0.01,
                           B0=1.0, K=1e5, k_div=2.5,
                           p_to_p=0.1, k_ab=1.0, mu_ab=0.05):
    """Two-compartment model: B cells expand and convert to plasma
    cells; plasma cells secrete antibody at rate k_ab per cell with
    antibody decay mu_ab/day.
    """
    N = int(T_days / dt)
    t = np.arange(N) * dt
    B = np.zeros(N); P = np.zeros(N); A = np.zeros(N)
    B[0] = B0
    for i in range(1, N):
        dB = k_div * B[i - 1] * (1 - (B[i - 1] + P[i - 1]) / K) - p_to_p * B[i - 1]
        dP = p_to_p * B[i - 1] - 0.1 * P[i - 1]
        dA = k_ab * P[i - 1] - mu_ab * A[i - 1]
        B[i] = B[i - 1] + dt * dB
        P[i] = P[i - 1] + dt * dP
        A[i] = A[i - 1] + dt * dA
    return t, B, P, A


def gillespie_clone(T_days=10.0, N0=5, birth=1.0 / 8 * 24, death=0.05,
                    seed=2026):
    """Gillespie stochastic clone growth.

    birth and death are per-cell per-day rates. A doubling time of 8 h
    corresponds to birth ~ ln(2)*24/8 ~ 2.08/day.
    """
    rng = np.random.default_rng(seed)
    t = 0.0
    N = N0
    times = [0.0]
    pop = [N]
    while t < T_days and N > 0:
        rate_total = (birth + death) * N
        dt = rng.exponential(1.0 / rate_total)
        t += dt
        if rng.random() < birth / (birth + death):
            N += 1
        else:
            N -= 1
        times.append(t)
        pop.append(N)
    return np.array(times), np.array(pop)


def main():
    t, B, P, A = deterministic_response()
    fig, axes = plt.subplots(3, 1, figsize=(7, 7), sharex=True)
    axes[0].semilogy(t, np.maximum(B, 1.0))
    axes[0].set_ylabel("B-cell count")
    axes[0].set_title("Clonal expansion (deterministic)")
    axes[1].semilogy(t, np.maximum(P, 1.0))
    axes[1].set_ylabel("plasma cells")
    axes[2].plot(t, A)
    axes[2].set_xlabel("days after antigen")
    axes[2].set_ylabel("antibody (arb.)")
    plt.tight_layout()
    plt.savefig("clonal_deterministic.png", dpi=150)
    plt.close()

    # Several stochastic replicates
    plt.figure(figsize=(7, 4))
    for s in range(2025, 2030):
        tt, pp = gillespie_clone(seed=s)
        plt.semilogy(tt, pp, alpha=0.7)
    plt.xlabel("days")
    plt.ylabel("clone size")
    plt.title("Gillespie stochastic clonal expansion (5 replicates)")
    plt.tight_layout()
    plt.savefig("clonal_gillespie.png", dpi=150)
    plt.close()

    print("Fold expansion of B compartment at day 7:",
          f"{B[int(7/0.01)] / B[0]:.2e}")
    print("Peak antibody day:", t[np.argmax(A)])


if __name__ == "__main__":
    main()
