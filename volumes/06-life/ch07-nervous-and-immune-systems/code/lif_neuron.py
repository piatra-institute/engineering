"""Leaky integrate-and-fire neuron model.

Reproduces the project deliverables for Vol VI Chapter 7: tonic firing,
f-I curve, spike-frequency adaptation, and the response to noisy input.

Usage:
    python3 lif_neuron.py
"""

import numpy as np
import matplotlib.pyplot as plt

# ----- Parameters (chapter project) -----------------------------------
TAU_M = 20e-3            # membrane time constant (s)
V_REST = -65e-3          # resting potential (V)
V_TH = -50e-3            # threshold (V)
V_RESET = -75e-3         # reset potential (V)
R_M = 10e6               # membrane resistance (Ohm)
TAU_REF = 2e-3           # absolute refractory period (s)
DT = 0.1e-3              # simulation step (s)


def simulate_lif(I_func, T=1.0, adapt=False, tau_a=100e-3, a_inc=2e-9, seed=2026):
    """Integrate the LIF equation with optional spike-frequency adaptation.

    Parameters
    ----------
    I_func : callable
        Current as a function of time (A).
    T : float
        Simulation duration (s).
    adapt : bool
        Enable an after-spike adaptation current.
    tau_a : float
        Adaptation time constant (s).
    a_inc : float
        Per-spike increment of the adaptation current (A).

    Returns
    -------
    t, V, spikes : ndarray, ndarray, list
    """
    np.random.seed(seed)
    N = int(T / DT)
    t = np.arange(N) * DT
    V = np.full(N, V_REST)
    spike_times = []
    last_spike = -1e9
    a = 0.0   # adaptation current (A)
    for i in range(1, N):
        if t[i] - last_spike < TAU_REF:
            V[i] = V_RESET
            if adapt:
                a *= np.exp(-DT / tau_a)
            continue
        I_eff = I_func(t[i]) - a
        dV = (-(V[i - 1] - V_REST) + R_M * I_eff) / TAU_M
        V[i] = V[i - 1] + DT * dV
        if adapt:
            a *= np.exp(-DT / tau_a)
        if V[i] >= V_TH:
            V[i] = 0.04          # plot a spike marker
            spike_times.append(t[i])
            last_spike = t[i]
            if adapt:
                a += a_inc
    return t, V, np.array(spike_times)


def fi_curve(currents, T=1.0, adapt=False):
    """Compute the f-I curve."""
    rates = []
    for I0 in currents:
        _, _, sp = simulate_lif(lambda t: I0, T=T, adapt=adapt)
        rates.append(len(sp) / T)
    return np.array(rates)


def main():
    # Panel 1: voltage trace at suprathreshold current
    t, V, sp = simulate_lif(lambda t: 2.0e-9, T=0.3)
    plt.figure(figsize=(8, 3))
    plt.plot(t * 1000, V * 1000)
    plt.xlabel("time (ms)")
    plt.ylabel("V (mV)")
    plt.title(f"LIF tonic firing, {len(sp)} spikes in 300 ms")
    plt.tight_layout()
    plt.savefig("lif_voltage_trace.png", dpi=150)
    plt.close()

    # Panel 2: f-I curves with and without adaptation
    Is = np.linspace(1.0e-9, 5.0e-9, 25)
    f_plain = fi_curve(Is, adapt=False)
    f_adapt = fi_curve(Is, adapt=True)
    plt.figure(figsize=(6, 4))
    plt.plot(Is * 1e9, f_plain, "o-", label="no adaptation")
    plt.plot(Is * 1e9, f_adapt, "s-", label="adaptation")
    plt.xlabel("input current (nA)")
    plt.ylabel("firing rate (Hz)")
    plt.title("f-I curve")
    plt.axhline(1 / TAU_REF, ls="--", color="gray", label="refractory limit")
    plt.legend()
    plt.tight_layout()
    plt.savefig("lif_fi_curve.png", dpi=150)
    plt.close()

    # Panel 3: noisy input
    rng = np.random.default_rng(2026)
    noise = rng.normal(0.0, 1.0, int(1.0 / DT))
    sigma = 1.5e-9
    I_mean = 1.8e-9
    noise_current = I_mean + sigma * noise

    def I_noise(tt):
        idx = int(tt / DT)
        if 0 <= idx < len(noise_current):
            return noise_current[idx]
        return I_mean

    t3, V3, sp3 = simulate_lif(I_noise, T=1.0)
    plt.figure(figsize=(8, 3))
    plt.plot(t3 * 1000, V3 * 1000)
    plt.xlabel("time (ms)")
    plt.ylabel("V (mV)")
    plt.title(f"LIF, noisy input, {len(sp3)} spikes in 1 s")
    plt.tight_layout()
    plt.savefig("lif_noisy_input.png", dpi=150)
    plt.close()

    # Threshold current report
    I_th = (V_TH - V_REST) / R_M
    print(f"threshold current = {I_th*1e9:.3f} nA")
    print(f"max rate (1/tau_ref) = {1/TAU_REF:.0f} Hz")


if __name__ == "__main__":
    main()
