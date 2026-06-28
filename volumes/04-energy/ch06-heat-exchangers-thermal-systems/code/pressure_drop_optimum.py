"""Heat-transfer versus pressure-drop velocity optimum for a tube-side stream.

Build the annualised cost as the sum of a capital term that falls with velocity
(higher film coefficient, less area) and a pumping term that rises with the cube
of velocity, then locate the minimum by a scan. The model reproduces the
trade-off figure of section 6.4 and gives the optimal tube velocity.

Scaling: capital cost proportional to area ~ 1/h ~ u^-0.8; pumping cost ~ u^3.
The coefficients fold in the duty, fluid properties, pump efficiency, and the
capital-recovery factor, and are taken as given constants here.
"""

from __future__ import annotations


def total_cost(u, k_cap, k_pump, alpha=0.8, beta=3.0):
    return k_cap * u ** (-alpha) + k_pump * u ** beta


def optimum_velocity(k_cap, k_pump, alpha=0.8, beta=3.0,
                     u_lo=0.3, u_hi=4.0, n=2000):
    best_u, best_c = u_lo, total_cost(u_lo, k_cap, k_pump, alpha, beta)
    for i in range(n + 1):
        u = u_lo + (u_hi - u_lo) * i / n
        c = total_cost(u, k_cap, k_pump, alpha, beta)
        if c < best_c:
            best_u, best_c = u, c
    return best_u, best_c


def analytic_optimum(k_cap, k_pump, alpha=0.8, beta=3.0):
    # d/du [k_cap u^-alpha + k_pump u^beta] = 0
    # => u^(alpha+beta) = alpha*k_cap / (beta*k_pump)
    return (alpha * k_cap / (beta * k_pump)) ** (1.0 / (alpha + beta))


if __name__ == "__main__":
    k_cap, k_pump = 2.2, 0.18
    u_scan, c_scan = optimum_velocity(k_cap, k_pump)
    u_anal = analytic_optimum(k_cap, k_pump)
    print(f"scan optimum:     u = {u_scan:.2f} m/s, cost = {c_scan:.3f}")
    print(f"analytic optimum: u = {u_anal:.2f} m/s")
