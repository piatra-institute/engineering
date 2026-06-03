"""Synaptic conductance models.

Implements an alpha-function synaptic conductance and short-term
plasticity (Tsodyks-Markram facilitation/depression), then shows how
multiple synaptic inputs sum at a passive postsynaptic neuron.

Usage:
    python3 synaptic_dynamics.py
"""

import numpy as np
import matplotlib.pyplot as plt

DT = 0.0001              # 0.1 ms
T = 0.20                 # 200 ms simulation

# Synapse parameters
G_PEAK = 1e-9            # 1 nS peak conductance
TAU_SYN = 5e-3           # 5 ms decay
E_SYN = 0.0              # 0 mV reversal (excitatory)
TAU_M = 20e-3
V_REST = -65e-3
C_M = 200e-12            # 200 pF


def alpha_synapse(t, t_spike, tau=TAU_SYN, g_peak=G_PEAK):
    """Alpha function g(t) = g_peak * (t/tau) * exp(1 - t/tau)."""
    dt = np.where(t >= t_spike, t - t_spike, 0.0)
    g = g_peak * (dt / tau) * np.exp(1 - dt / tau)
    g = np.where(t >= t_spike, g, 0.0)
    return g


def tsodyks_markram(spike_times, T, dt, U=0.5, tau_rec=200e-3, tau_fac=50e-3):
    """Compute the per-spike effective synaptic strength."""
    N = int(T / dt)
    t = np.arange(N) * dt
    R = 1.0    # available resources
    u = U
    strengths = []
    spike_idx = 0
    R_trace = np.zeros(N)
    u_trace = np.zeros(N)
    for i in range(N):
        R += dt * (1 - R) / tau_rec
        u += dt * (U - u) / tau_fac
        R_trace[i] = R
        u_trace[i] = u
        if spike_idx < len(spike_times) and t[i] >= spike_times[spike_idx]:
            u += U * (1 - u)
            strength = u * R
            strengths.append(strength)
            R -= strength
            spike_idx += 1
    return t, R_trace, u_trace, strengths


def main():
    t = np.arange(int(T / DT)) * DT
    # Single EPSC
    g = alpha_synapse(t, 0.020)
    plt.figure(figsize=(7, 3))
    plt.plot(t * 1000, g * 1e9)
    plt.xlabel("time (ms)")
    plt.ylabel("g_syn (nS)")
    plt.title("Alpha-function synaptic conductance")
    plt.tight_layout()
    plt.savefig("synapse_alpha.png", dpi=150)
    plt.close()
    # EPSP summation: 5 EPSCs at 50 Hz drive a passive cell
    V = np.full_like(t, V_REST)
    spike_times = np.arange(5) * 0.020 + 0.010
    g_sum = np.zeros_like(t)
    for ts in spike_times:
        g_sum += alpha_synapse(t, ts)
    for i in range(1, len(t)):
        I_syn = g_sum[i] * (V[i - 1] - E_SYN)
        dV = (-(V[i - 1] - V_REST) - I_syn / 1.0 * 1e6) / TAU_M
        V[i] = V[i - 1] + DT * dV
    plt.figure(figsize=(7, 3))
    plt.plot(t * 1000, V * 1000)
    plt.xlabel("time (ms)")
    plt.ylabel("V (mV)")
    plt.title("EPSP summation, 5 inputs at 50 Hz")
    plt.tight_layout()
    plt.savefig("synapse_epsp_sum.png", dpi=150)
    plt.close()
    # Short-term plasticity
    sp = np.arange(8) * 0.020 + 0.010
    t2, R, u, w = tsodyks_markram(sp, T=0.20, dt=DT)
    plt.figure(figsize=(7, 4))
    plt.subplot(2, 1, 1)
    plt.plot(t2 * 1000, R, label="R (avail. resources)")
    plt.plot(t2 * 1000, u, label="u (release prob.)")
    plt.legend(); plt.ylabel("state")
    plt.subplot(2, 1, 2)
    plt.bar(sp * 1000, w, width=2)
    plt.xlabel("time (ms)")
    plt.ylabel("effective release")
    plt.title("Tsodyks-Markram dynamics")
    plt.tight_layout()
    plt.savefig("synapse_tm_plasticity.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    main()
