# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Estimate peak knee force during a vertical jump from accelerometer.

Workflow:
  1. Read or synthesise a time series a(t) of vertical acceleration
     measured at the body's centre of mass (lower back).
  2. Detect the take-off push phase (positive vertical acceleration
     before take-off) and the landing impact (positive spike after
     descent).
  3. Compute the impulse delivered during the push phase by integrating
     m * a over the push duration.
  4. Compute average and peak ground-reaction force, and the resulting
     peak patello-femoral joint force from a simplified knee model.

Geometric knee model (sagittal-plane static approximation):
  - At deep knee flexion (~90 deg) the quadriceps moment arm about the
    knee centre is ~5 cm and the ground-reaction-force moment arm
    from the ankle joint centre to the knee axis is ~15 cm.
  - F_quad = F_grf * (15 / 5) = 3 F_grf (at the simplified geometry).
  - Patello-femoral compression ~ 1.5 F_quad at 90 deg flexion.

Reference: Winter (2009), Biomechanics and motor control of human
movement, 4th ed., chapter on knee mechanics.

Run: uv run jump_peak_force.py
"""
from __future__ import annotations
import numpy as np


def synthesize_jump_signal(
    dt: float = 0.001,
    duration: float = 2.5,
    body_mass: float = 70.0,
    crouch_depth_m: float = 0.40,
    jump_height_m: float = 0.40,
    push_duration: float = 0.30,
    flight_duration: float = 0.57,
    landing_duration: float = 0.10,
) -> tuple[np.ndarray, np.ndarray]:
    """Generate a synthetic a(t) for a vertical jump."""
    n = int(duration / dt)
    t = np.arange(n) * dt
    a = np.zeros(n)  # vertical acceleration excluding gravity, m/s^2
    # Push phase: piecewise-cosine ramp peaking near mid-push
    push_start = 0.10
    push_end = push_start + push_duration
    push_idx = (t >= push_start) & (t < push_end)
    tau = (t[push_idx] - push_start) / push_duration  # 0..1
    # Required mean GRF-to-mg ratio derived below; shape is a half-sine
    target_impulse = body_mass * np.sqrt(2 * 9.81 * jump_height_m)
    mean_a = target_impulse / (body_mass * push_duration)
    a[push_idx] = mean_a * (np.pi / 2) * np.sin(np.pi * tau)
    # Flight phase: free fall (signal is gravity, no vertical accel beyond -g)
    flight_idx = (t >= push_end) & (t < push_end + flight_duration)
    a[flight_idx] = 0.0
    # Landing impact: sharp positive spike for ~landing_duration
    land_start = push_end + flight_duration
    land_end = land_start + landing_duration
    land_idx = (t >= land_start) & (t < land_end)
    peak_landing_a = 3.5 * 9.81  # ~3.5g peak deceleration on landing
    a[land_idx] = peak_landing_a * np.sin(np.pi * (t[land_idx] - land_start) / landing_duration)
    return t, a


def push_phase_impulse(
    t: np.ndarray, a: np.ndarray, body_mass: float, push_window: tuple[float, float]
) -> dict:
    """Integrate vertical acceleration during the push phase."""
    t0, t1 = push_window
    idx = (t >= t0) & (t <= t1)
    dt = t[1] - t[0]
    a_push = a[idx]
    # GRF = m*(a + g)
    grf = body_mass * (a_push + 9.81)
    impulse_total = np.sum(grf) * dt
    impulse_above_bw = impulse_total - body_mass * 9.81 * (t1 - t0)
    return {
        "impulse_total_Ns": impulse_total,
        "impulse_above_bw_Ns": impulse_above_bw,
        "peak_grf_N": float(np.max(grf)),
        "mean_grf_N": float(np.mean(grf)),
        "push_duration_s": t1 - t0,
        "takeoff_velocity_mps": impulse_above_bw / body_mass,
        "jump_height_m": (impulse_above_bw / body_mass) ** 2 / (2 * 9.81),
    }


def knee_force_from_grf(
    grf_N: float, body_mass: float, knee_flex_deg: float = 90.0
) -> dict:
    """Static-sagittal-plane knee model: quadriceps and patello-femoral force."""
    # Effective moment arms (m). Linearly interpolate between 30 deg and 90 deg.
    grf_arm = 0.05 + 0.10 * (knee_flex_deg - 30) / (90 - 30)  # 5 cm at 30 deg, 15 cm at 90 deg
    quad_arm = 0.05  # quadriceps tendon at the patella
    quad_tension = grf_N * grf_arm / quad_arm
    # Patello-femoral compression factor from knee flexion angle.
    # Approximate empirical fit: 0.5 at full extension, 1.5 at 90 deg flexion.
    pf_factor = 0.5 + 1.0 * (knee_flex_deg / 90.0)
    pf_force = pf_factor * quad_tension
    return {
        "grf_arm_m": grf_arm,
        "quad_arm_m": quad_arm,
        "quad_tension_N": quad_tension,
        "pf_factor": pf_factor,
        "pf_force_N": pf_force,
        "pf_force_BW": pf_force / (body_mass * 9.81),
    }


def main() -> None:
    body_mass = 70.0
    t, a = synthesize_jump_signal(body_mass=body_mass)
    push = push_phase_impulse(t, a, body_mass, (0.10, 0.40))
    knee = knee_force_from_grf(push["peak_grf_N"], body_mass, knee_flex_deg=90.0)
    print("=== Push-phase summary ===")
    for k, v in push.items():
        print(f"  {k:>25s} = {v:10.2f}")
    print("\n=== Knee-force summary (90 deg flexion) ===")
    for k, v in knee.items():
        print(f"  {k:>25s} = {v:10.2f}")


if __name__ == "__main__":
    main()
