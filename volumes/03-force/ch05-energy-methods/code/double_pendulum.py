"""Double-pendulum integrator built from the Lagrangian equations of motion.

The equations of motion derived in section 5.6.2 are solved as a
first-order system in the state vector (theta1, theta2, omega1, omega2)
with a fixed-step fourth-order Runge-Kutta integrator. Total mechanical
energy is logged at every step so that energy drift can be used as the
integrator-accuracy diagnostic the chapter's project requires.

Run:
    python double_pendulum.py
writes a trajectory and energy log to data/double_pendulum_trajectory.csv.
"""

from __future__ import annotations
import csv
import math
from pathlib import Path

G = 9.81  # m s^-2


def accelerations(state, m1, m2, l1, l2):
    """Angular accelerations from the two Euler-Lagrange equations.

    The coupled pair is solved for (alpha1, alpha2) by inverting the
    2x2 mass matrix that multiplies the angular accelerations.
    """
    th1, th2, w1, w2 = state
    d = th1 - th2
    cd, sd = math.cos(d), math.sin(d)

    # Mass-matrix entries M [[a, b], [c, e]] times [alpha1, alpha2] = rhs.
    a = (m1 + m2) * l1
    b = m2 * l2 * cd
    c = l1 * cd
    e = l2

    r1 = -m2 * l2 * w2 * w2 * sd - (m1 + m2) * G * math.sin(th1)
    r2 = l1 * w1 * w1 * sd - G * math.sin(th2)

    det = a * e - b * c
    alpha1 = (r1 * e - b * r2) / det
    alpha2 = (a * r2 - c * r1) / det
    return alpha1, alpha2


def deriv(state, m1, m2, l1, l2):
    _, _, w1, w2 = state
    a1, a2 = accelerations(state, m1, m2, l1, l2)
    return (w1, w2, a1, a2)


def total_energy(state, m1, m2, l1, l2):
    th1, th2, w1, w2 = state
    t = (0.5 * (m1 + m2) * l1 * l1 * w1 * w1
         + 0.5 * m2 * l2 * l2 * w2 * w2
         + m2 * l1 * l2 * w1 * w2 * math.cos(th1 - th2))
    u = (-(m1 + m2) * G * l1 * math.cos(th1)
         - m2 * G * l2 * math.cos(th2))
    return t + u


def rk4_step(state, h, m1, m2, l1, l2):
    def add(s, k, f):
        return tuple(si + f * ki for si, ki in zip(s, k))

    k1 = deriv(state, m1, m2, l1, l2)
    k2 = deriv(add(state, k1, h / 2), m1, m2, l1, l2)
    k3 = deriv(add(state, k2, h / 2), m1, m2, l1, l2)
    k4 = deriv(add(state, k3, h), m1, m2, l1, l2)
    return tuple(si + (h / 6) * (a + 2 * b + 2 * c + d)
                 for si, a, b, c, d in zip(state, k1, k2, k3, k4))


def simulate(state, m1, m2, l1, l2, t_end, h):
    rows = []
    e0 = total_energy(state, m1, m2, l1, l2)
    n = int(round(t_end / h))
    for i in range(n + 1):
        e = total_energy(state, m1, m2, l1, l2)
        rows.append((i * h, state[0], state[1], state[2], state[3],
                     e, (e - e0) / abs(e0)))
        state = rk4_step(state, h, m1, m2, l1, l2)
    return rows


def main():
    m1 = m2 = 1.0
    l1 = l2 = 1.0
    state0 = (math.radians(120.0), math.radians(-10.0), 0.0, 0.0)
    rows = simulate(state0, m1, m2, l1, l2, t_end=30.0, h=1.0e-3)

    out = Path(__file__).resolve().parent.parent / "data"
    out.mkdir(exist_ok=True)
    path = out / "double_pendulum_trajectory.csv"
    # thin to every 10th row to keep the dataset legible
    with path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["t_s", "theta1_rad", "theta2_rad",
                    "omega1_rad_s", "omega2_rad_s",
                    "energy_J", "energy_drift_rel"])
        for row in rows[::10]:
            w.writerow([f"{v:.6e}" for v in row])
    drift = max(abs(r[6]) for r in rows)
    print(f"wrote {path}, peak relative energy drift = {drift:.2e}")


if __name__ == "__main__":
    main()
