"""Boris-pusher single-particle integrator in uniform E and B fields.

The Boris algorithm is the standard time-centred leapfrog scheme for the
Lorentz-force equation of motion. It separates the magnetic rotation from
the electric acceleration and conserves the gyro-orbit energy exactly in a
pure magnetic field, which is why it is the workhorse of particle-in-cell
plasma codes. This module integrates one particle and compares the
measured guiding-centre drift against the analytic E x B value.

Pure standard library; no numpy. Supports Exercise (Boris pusher) directly.
"""

import math

Q = 1.602176634e-19       # elementary charge, C
M = 9.1093837015e-31      # electron mass, kg


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def boris_step(x, v, e_field, b_field, dt, q=Q, m=M):
    """One Boris update. Returns (x_new, v_new)."""
    qmdt = q * dt / (2.0 * m)
    # half electric acceleration
    v_minus = tuple(v[i] + qmdt * e_field[i] for i in range(3))
    # magnetic rotation
    t = tuple(qmdt * b_field[i] for i in range(3))
    t_mag2 = sum(ti * ti for ti in t)
    s = tuple(2.0 * ti / (1.0 + t_mag2) for ti in t)
    v_prime = tuple(v_minus[i] + cross(v_minus, t)[i] for i in range(3))
    v_plus = tuple(v_minus[i] + cross(v_prime, s)[i] for i in range(3))
    # second half electric acceleration
    v_new = tuple(v_plus[i] + qmdt * e_field[i] for i in range(3))
    x_new = tuple(x[i] + dt * v_new[i] for i in range(3))
    return x_new, v_new


def run(steps=10000, dt=None):
    b_field = (0.0, 0.0, 1.0)            # 1 T along z
    e_field = (1.0e4, 0.0, 0.0)          # 10 kV/m along x
    omega_c = Q * b_field[2] / M
    if dt is None:
        dt = 0.02 / omega_c             # ~50 steps per gyro-period
    x = (0.0, 0.0, 0.0)
    v = (3.0e5, 0.0, 0.0)               # 1 eV-scale perpendicular speed
    ys = []
    for _ in range(steps):
        x, v = boris_step(x, v, e_field, b_field, dt)
        ys.append(x[1])
    # The guiding centre drifts; the gyration adds a bounded oscillation in
    # y. Averaging the y-position over an integer number of gyro-periods
    # removes the oscillation, so the drift is the slope of the mean
    # position between two windows one gyro-period apart.
    period = 2.0 * math.pi / omega_c
    n_per = max(1, int(round(period / dt)))      # steps per gyro-period
    early = sum(ys[:n_per]) / n_per              # mean y over first period
    late = sum(ys[-n_per:]) / n_per             # mean y over last period
    span = (steps - n_per) * dt
    measured_drift = (late - early) / span
    analytic_drift = -e_field[0] / b_field[2]   # (E x B)/B^2, y-component
    return measured_drift, analytic_drift


def main():
    measured, analytic = run()
    print(f"E x B drift  analytic = {analytic:.3e} m/s")
    print(f"             measured = {measured:.3e} m/s")
    print(f"      relative error  = {abs(measured - analytic) / abs(analytic):.2%}")


if __name__ == "__main__":
    main()
