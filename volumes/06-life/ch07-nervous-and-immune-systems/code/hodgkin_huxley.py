"""Hodgkin-Huxley squid giant axon model.

Reproduces the classical 1952 model. Parameters are at 6.3 deg C as in
the original Hodgkin-Huxley paper, with potentials shifted so the
resting state is near -65 mV.

Usage:
    python3 hodgkin_huxley.py
"""

import numpy as np
import matplotlib.pyplot as plt

# Maximum conductances (mS/cm^2)
G_NA = 120.0
G_K = 36.0
G_L = 0.3

# Reversal potentials (mV)
E_NA = 50.0
E_K = -77.0
E_L = -54.4

# Membrane capacitance (uF/cm^2)
C_M = 1.0


def alpha_m(V):
    return 0.1 * (V + 40.0) / (1.0 - np.exp(-(V + 40.0) / 10.0))


def beta_m(V):
    return 4.0 * np.exp(-(V + 65.0) / 18.0)


def alpha_h(V):
    return 0.07 * np.exp(-(V + 65.0) / 20.0)


def beta_h(V):
    return 1.0 / (1.0 + np.exp(-(V + 35.0) / 10.0))


def alpha_n(V):
    return 0.01 * (V + 55.0) / (1.0 - np.exp(-(V + 55.0) / 10.0))


def beta_n(V):
    return 0.125 * np.exp(-(V + 65.0) / 80.0)


def simulate_hh(I_func, T=50.0, dt=0.01, g_L=G_L):
    """Integrate the HH equations.

    Parameters
    ----------
    I_func : callable
        Stimulus current (uA/cm^2) as a function of time (ms).
    T : float
        Duration (ms).
    dt : float
        Step (ms).
    g_L : float
        Leak conductance (mS/cm^2).
    """
    N = int(T / dt)
    t = np.arange(N) * dt
    V = np.zeros(N)
    m = np.zeros(N)
    h = np.zeros(N)
    n = np.zeros(N)
    V[0] = -65.0
    m[0] = alpha_m(V[0]) / (alpha_m(V[0]) + beta_m(V[0]))
    h[0] = alpha_h(V[0]) / (alpha_h(V[0]) + beta_h(V[0]))
    n[0] = alpha_n(V[0]) / (alpha_n(V[0]) + beta_n(V[0]))
    for i in range(1, N):
        I_Na = G_NA * (m[i - 1] ** 3) * h[i - 1] * (V[i - 1] - E_NA)
        I_K = G_K * (n[i - 1] ** 4) * (V[i - 1] - E_K)
        I_L = g_L * (V[i - 1] - E_L)
        dV = (I_func(t[i - 1]) - I_Na - I_K - I_L) / C_M
        V[i] = V[i - 1] + dt * dV
        m[i] = m[i - 1] + dt * (alpha_m(V[i - 1]) * (1 - m[i - 1])
                                - beta_m(V[i - 1]) * m[i - 1])
        h[i] = h[i - 1] + dt * (alpha_h(V[i - 1]) * (1 - h[i - 1])
                                - beta_h(V[i - 1]) * h[i - 1])
        n[i] = n[i - 1] + dt * (alpha_n(V[i - 1]) * (1 - n[i - 1])
                                - beta_n(V[i - 1]) * n[i - 1])
    return t, V, m, h, n


def main():
    # Single AP from a brief pulse.
    def pulse(t):
        return 10.0 if 5.0 <= t <= 5.5 else 0.0

    t, V, m, h, n = simulate_hh(pulse, T=40.0)
    fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    axes[0].plot(t, V)
    axes[0].set_ylabel("V (mV)")
    axes[0].set_title("Hodgkin-Huxley single action potential")
    axes[1].plot(t, m ** 3 * h, label=r"$m^3 h$ (Na gate)")
    axes[1].plot(t, n ** 4, label=r"$n^4$ (K gate)")
    axes[1].set_xlabel("time (ms)")
    axes[1].set_ylabel("gating")
    axes[1].legend()
    plt.tight_layout()
    plt.savefig("hh_single_ap.png", dpi=150)
    plt.close()

    # Sustained current: repetitive firing
    def step(t):
        return 7.0 if t > 5.0 else 0.0

    t2, V2, *_ = simulate_hh(step, T=100.0)
    plt.figure(figsize=(8, 3))
    plt.plot(t2, V2)
    plt.xlabel("time (ms)")
    plt.ylabel("V (mV)")
    plt.title("HH repetitive firing at sustained current")
    plt.tight_layout()
    plt.savefig("hh_repetitive.png", dpi=150)
    plt.close()

    # Sweep over leak conductance to find AP threshold
    g_L_values = np.linspace(0.05, 0.8, 16)
    spike_counts = []
    for gL in g_L_values:
        _, Vt, *_ = simulate_hh(pulse, T=40.0, g_L=gL)
        spike_counts.append(int(np.any(Vt > 0.0)))
    print("g_L sweep (mS/cm^2 : AP fired?)")
    for gL, s in zip(g_L_values, spike_counts):
        print(f"  {gL:.3f}  {bool(s)}")


if __name__ == "__main__":
    main()
