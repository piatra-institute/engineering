"""Two-stage ODE model for the central dogma.

We model the steady-state and dynamic abundance of a single mRNA and
its protein product as a coupled linear system:

    dm/dt = k_tx           - gamma_m * m
    dp/dt = k_tl * m       - gamma_p * p

Parameters are bacterial defaults (E. coli, current as of 2024):

  k_tx     transcription initiation rate          0.1 mRNA/s
  k_tl     translation rate per mRNA              0.05 protein/s
  gamma_m  mRNA decay rate (half-life ~5 min)     ln 2 / 300 s
  gamma_p  protein decay rate (half-life ~20 h)   ln 2 / 72000 s

The steady-state values follow:

    m_ss = k_tx / gamma_m
    p_ss = (k_tl / gamma_p) * m_ss

We integrate from zero initial concentrations and plot mRNA and
protein trajectories. The script can be invoked with
--induction-time T to introduce a step change in k_tx at time T,
illustrating the time constant of the response.
"""
from __future__ import annotations

import argparse
import math


def step(state: tuple[float, float], k_tx: float, k_tl: float,
         gamma_m: float, gamma_p: float, dt: float) -> tuple[float, float]:
    m, p = state
    dm = k_tx - gamma_m * m
    dp = k_tl * m - gamma_p * p
    return (m + dm * dt, p + dp * dt)


def integrate(k_tx: float, k_tl: float, gamma_m: float, gamma_p: float,
              t_end: float, dt: float,
              induction_time: float | None = None,
              k_tx_after: float | None = None
              ) -> list[tuple[float, float, float]]:
    """Return list of (t, m, p) tuples sampled every 100 steps."""
    m = 0.0
    p = 0.0
    out: list[tuple[float, float, float]] = []
    n_steps = int(t_end / dt)
    for i in range(n_steps):
        t = i * dt
        current_k_tx = k_tx
        if induction_time is not None and t >= induction_time:
            current_k_tx = k_tx_after if k_tx_after is not None else k_tx
        m, p = step((m, p), current_k_tx, k_tl, gamma_m, gamma_p, dt)
        if i % 100 == 0:
            out.append((t, m, p))
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k-tx", type=float, default=0.1,
                        help="transcription rate (mRNA / s)")
    parser.add_argument("--k-tl", type=float, default=0.05,
                        help="translation rate (protein / mRNA / s)")
    parser.add_argument("--mrna-half-life", type=float, default=300.0,
                        help="mRNA half-life in seconds (default 5 min)")
    parser.add_argument("--protein-half-life", type=float, default=72000.0,
                        help="protein half-life in seconds (default 20 h)")
    parser.add_argument("--t-end", type=float, default=86400.0,
                        help="integration end time in seconds (default 24 h)")
    parser.add_argument("--dt", type=float, default=1.0,
                        help="time step in seconds")
    parser.add_argument("--induction-time", type=float, default=None)
    parser.add_argument("--k-tx-after", type=float, default=None)
    args = parser.parse_args()

    gamma_m = math.log(2.0) / args.mrna_half_life
    gamma_p = math.log(2.0) / args.protein_half_life

    m_ss = args.k_tx / gamma_m
    p_ss = (args.k_tl / gamma_p) * m_ss
    print(f"steady-state mRNA copies     : {m_ss:.1f}")
    print(f"steady-state protein copies  : {p_ss:.1f}")
    print(f"mRNA  time constant tau_m    : {1.0 / gamma_m:.1f} s")
    print(f"prot. time constant tau_p    : {1.0 / gamma_p:.1f} s "
          f"= {1.0 / gamma_p / 3600:.2f} h")

    trace = integrate(args.k_tx, args.k_tl, gamma_m, gamma_p,
                      args.t_end, args.dt,
                      args.induction_time, args.k_tx_after)
    print("t (s),    m,        p")
    # print a few sample points
    for t, m, p in trace[::max(1, len(trace) // 20)]:
        print(f"{t:8.0f}, {m:8.2f}, {p:10.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
