"""Single-bus swing-equation model of grid frequency after a trip.

The aggregate frequency of a synchronous grid obeys, to first order,
the swing equation in per-unit form:

    2H df/dt = P_mech - P_load - D (f - f0)

where H is the inertia constant (seconds of rated MW-s per MW), D is
the load-damping coefficient, and the governor adds primary response
proportional to the frequency error through the droop R.

We integrate the linearised model after a step loss of generation and
locate the frequency nadir, the metric that decides whether
under-frequency load shedding fires.

Usage:
    python frequency_response.py
"""

from __future__ import annotations


def simulate(
    H=4.0,            # inertia constant, seconds
    D=1.0,            # load damping, pu power per pu freq
    R=0.05,           # governor droop (5%)
    Tg=8.0,           # governor + turbine time constant, seconds
    dP=0.10,          # lost generation, fraction of system load
    f0=50.0,          # nominal frequency, Hz
    dt=0.01,          # step, seconds
    t_end=60.0,
):
    """Integrate the linearised swing + governor model.

    Returns (times, freqs) lists in Hz.
    """
    df = 0.0          # frequency deviation in pu (1.0 = f0)
    pg = 0.0          # governor mechanical response in pu
    times, freqs = [], []
    n = int(t_end / dt)
    for i in range(n + 1):
        t = i * dt
        times.append(t)
        freqs.append(f0 * (1.0 + df))
        # governor first-order lag toward -df/R
        pg += dt * ((-df / R) - pg) / Tg
        # swing equation: 2H d(df)/dt = pg - dP - D df
        ddf = (pg - dP - D * df) / (2.0 * H)
        df += dt * ddf
    return times, freqs


if __name__ == "__main__":
    for H in (2.0, 4.0, 8.0):
        t, f = simulate(H=H)
        nadir = min(f)
        print(f"H={H:4.1f} s   nadir = {nadir:6.3f} Hz   dip = {50.0 - nadir:5.3f} Hz")
