"""Finite-difference solver for the passive cable equation.

Demonstrates exponential decay of a steady-state voltage perturbation
along a passive cable with space constant lambda = sqrt(r_m/r_a) and
the spread of a transient pulse.

Usage:
    python3 cable_equation_solve.py
"""

import numpy as np
import matplotlib.pyplot as plt

# Geometry and electrical parameters
LENGTH_CM = 1.0          # cable length (cm)
N = 200                  # spatial nodes
DX = LENGTH_CM / N       # spatial step (cm)
R_M = 5000.0             # specific membrane resistance (Ohm cm^2)
R_A = 100.0              # axial resistivity (Ohm cm)
D_CM = 1e-3              # axon diameter (cm)
C_M = 1.0e-6             # specific membrane capacitance (F/cm^2)

# Derived parameters (per unit length)
r_m_per_cm = R_M / (np.pi * D_CM)         # Ohm cm
r_a_per_cm = R_A / (np.pi * (D_CM / 2) ** 2)  # Ohm/cm
LAMBDA = np.sqrt(r_m_per_cm / r_a_per_cm) # cm
TAU_M = R_M * C_M                          # s


def steady_state(V0=20.0):
    """Steady-state voltage profile with V(x=0)=V0 and dV/dx(L)=0."""
    x = np.linspace(0, LENGTH_CM, N)
    V = V0 * np.exp(-x / LAMBDA)
    return x, V


def simulate_transient(T=0.02, dt=1e-6, pulse_dur=2e-4):
    """Inject a brief current at x=0 and observe propagation."""
    x = np.linspace(0, LENGTH_CM, N)
    V = np.zeros(N)
    steps = int(T / dt)
    snapshots = {}
    snapshot_t = [0.001, 0.005, 0.010, 0.015]
    for s in range(steps):
        t = s * dt
        I_inj = 1.0 if t < pulse_dur else 0.0
        # Cable PDE: tau_m dV/dt = lambda^2 d2V/dx2 - V + r_m * I
        dV = np.zeros(N)
        dV[1:-1] = (LAMBDA ** 2 / DX ** 2) * (V[2:] - 2 * V[1:-1] + V[:-2]) - V[1:-1]
        dV[0] += r_m_per_cm * I_inj
        dV[0] += (LAMBDA ** 2 / DX ** 2) * (V[1] - V[0])
        dV[-1] += (LAMBDA ** 2 / DX ** 2) * (V[-2] - V[-1])
        V = V + (dt / TAU_M) * dV
        for tt in snapshot_t:
            if abs(t - tt) < dt / 2:
                snapshots[tt] = V.copy()
    return x, snapshots


def main():
    print(f"lambda = {LAMBDA * 10:.3f} mm  ({LAMBDA:.4f} cm)")
    print(f"tau_m  = {TAU_M * 1000:.1f} ms")
    # Steady state
    x, V = steady_state(V0=20.0)
    plt.figure(figsize=(7, 4))
    plt.plot(x * 10, V)
    plt.xlabel("distance from injection (mm)")
    plt.ylabel("V (mV)")
    plt.title(f"Passive cable: steady-state decay, lambda = {LAMBDA*10:.2f} mm")
    plt.axvline(LAMBDA * 10, ls="--", color="gray", label="lambda")
    plt.legend()
    plt.tight_layout()
    plt.savefig("cable_steady_state.png", dpi=150)
    plt.close()
    # Transient
    x2, snaps = simulate_transient()
    plt.figure(figsize=(7, 4))
    for tt, Vt in sorted(snaps.items()):
        plt.plot(x2 * 10, Vt, label=f"t = {tt*1000:.0f} ms")
    plt.xlabel("distance (mm)")
    plt.ylabel("V (mV)")
    plt.title("Passive cable: transient propagation")
    plt.legend()
    plt.tight_layout()
    plt.savefig("cable_transient.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    main()
