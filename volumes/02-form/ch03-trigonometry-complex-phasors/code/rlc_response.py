"""Series RLC steady-state response via phasor algebra and via ODE.

Computes the impedance, current phasor, and element voltages for the
worked series RLC example of section 3.8 over a swept frequency
range. Then integrates the underlying second-order ODE
    L d^2 q / dt^2 + R dq/dt + q / C = V_m cos(omega t)
and compares the steady-state current with the phasor result at the
drive frequency.

Usage:
    uv run --with numpy --with matplotlib --with scipy rlc_response.py

Dependencies: numpy, matplotlib, scipy.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Worked-example parameters from section 3.8.
R = 100.0          # ohm
L = 0.100          # henry
C = 10e-6          # farad
V_M = 10.0         # volt (peak)
F_DRIVE = 50.0     # hertz
OMEGA = 2 * np.pi * F_DRIVE


def impedance(omega: float | np.ndarray) -> complex | np.ndarray:
    """Series RLC impedance Z(omega) = R + i (omega L - 1/(omega C))."""
    return R + 1j * (omega * L - 1.0 / (omega * C))


def phasor_solution() -> dict[str, complex]:
    """Phasor solution at the drive frequency."""
    z = impedance(OMEGA)
    vs = V_M + 0j
    i_phasor = vs / z
    vr = R * i_phasor
    vl = 1j * OMEGA * L * i_phasor
    vc = -1j / (OMEGA * C) * i_phasor
    return {"Z": z, "I": i_phasor, "VR": vr, "VL": vl, "VC": vc}


def ode_rhs(t: float, state: np.ndarray) -> np.ndarray:
    """State = (q, i). Returns (dq/dt, di/dt)."""
    q, i = state
    di_dt = (V_M * np.cos(OMEGA * t) - R * i - q / C) / L
    return np.array([i, di_dt])


def main() -> None:
    sol = phasor_solution()
    print("Phasor-domain results at f = 50 Hz:")
    for name, val in sol.items():
        print(f"  {name}: |.| = {abs(val):.4f}, "
              f"angle = {np.degrees(np.angle(val)):+.2f} deg")

    # Integrate the ODE long enough to settle the transient.
    n_periods = 30
    t_end = n_periods * 2 * np.pi / OMEGA
    t_eval = np.linspace(0, t_end, 5000)
    solver = solve_ivp(ode_rhs, (0.0, t_end), [0.0, 0.0],
                       t_eval=t_eval, rtol=1e-8, atol=1e-10)
    i_numeric = solver.y[1]

    # Steady-state from phasor: i(t) = |I| cos(omega t + angle(I))
    i_amp = abs(sol["I"])
    i_phase = np.angle(sol["I"])
    i_steady = i_amp * np.cos(OMEGA * t_eval + i_phase)

    # Plot last few periods to show agreement after transient.
    plot_mask = t_eval > t_eval[-1] - 4 * 2 * np.pi / OMEGA
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(t_eval[plot_mask], 1000 * i_numeric[plot_mask],
            label="numeric (ODE)", linewidth=1.6)
    ax.plot(t_eval[plot_mask], 1000 * i_steady[plot_mask],
            label="phasor steady-state",
            linewidth=1.2, linestyle="--", color="red")
    ax.set_xlabel("t (s)")
    ax.set_ylabel("i(t) (mA)")
    ax.legend(loc="best")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("rlc_response.png", dpi=120)
    print("Wrote rlc_response.png")

    # Sweep the impedance magnitude over a frequency range and write csv.
    f_sweep = np.logspace(1, 4, 200)
    z_sweep = impedance(2 * np.pi * f_sweep)
    np.savetxt("rlc_impedance.csv",
               np.column_stack([f_sweep, np.abs(z_sweep),
                                np.degrees(np.angle(z_sweep))]),
               delimiter=",",
               header="frequency_hz,impedance_magnitude_ohm,phase_deg",
               comments="")
    print("Wrote rlc_impedance.csv")


if __name__ == "__main__":
    main()
