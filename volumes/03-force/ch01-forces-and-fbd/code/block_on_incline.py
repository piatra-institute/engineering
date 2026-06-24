"""
Friction force on a block resting on a plane whose inclination angle is
slowly increased from zero, demonstrating the static plateau and the
kink at the slipping threshold.

Supports:
  - Volume III, Chapter 1, simulation exercise "simulate the motion of a
    block on a rough inclined plane as the angle increases slowly"
  - The Coulomb-friction figure (static plateau, kinetic drop).

Physics:
  While not sliding, static friction balances the down-slope weight
  component: F_f = m g sin(theta), up to the limit mu_s m g cos(theta).
  The block breaks free at the threshold angle theta* = atan(mu_s).
  Once sliding, kinetic friction is mu_k m g cos(theta).

Dependencies:
  numpy  (matplotlib optional, only for the plot)

Usage:
  python block_on_incline.py            # prints the threshold angle
  python block_on_incline.py --plot     # also writes friction_vs_angle.png
"""

import argparse
import math

import numpy as np


def friction_force(theta, m, g, mu_s, mu_k):
    """Return (F_f, sliding) for a block on an incline at angle theta (rad)."""
    drive = m * g * math.sin(theta)
    normal = m * g * math.cos(theta)
    f_max = mu_s * normal
    if drive <= f_max:
        return drive, False           # static: friction matches the drive
    return mu_k * normal, True        # kinetic: saturates at mu_k N


def sweep(m=2.0, g=9.81, mu_s=0.5, mu_k=0.35, n=400):
    thetas = np.linspace(0.0, math.radians(60.0), n)
    ff = np.array([friction_force(t, m, g, mu_s, mu_k)[0] for t in thetas])
    theta_star = math.atan(mu_s)
    return thetas, ff, theta_star


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plot", action="store_true")
    args = ap.parse_args()

    thetas, ff, theta_star = sweep()
    print(f"slip threshold theta* = atan(mu_s) = "
          f"{math.degrees(theta_star):.2f} deg")
    print(f"friction at threshold = {ff[np.argmax(thetas > theta_star) - 1]:.3f} N")

    if args.plot:
        import matplotlib.pyplot as plt
        plt.plot(np.degrees(thetas), ff)
        plt.axvline(math.degrees(theta_star), ls="--")
        plt.xlabel("incline angle (deg)")
        plt.ylabel("friction force (N)")
        plt.title("Friction force vs incline angle")
        plt.savefig("friction_vs_angle.png", dpi=120)
        print("wrote friction_vs_angle.png")


if __name__ == "__main__":
    main()
