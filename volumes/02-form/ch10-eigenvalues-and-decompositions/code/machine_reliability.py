# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Machine-reliability Markov chain: stationary distribution three ways.

Companion to Vol II, Ch 10, the case study "Machine availability as a
Markov-chain steady-state problem". Reads the five-state transition
matrix from data/machine_reliability_chain.csv and computes the
stationary distribution by

  1. left-eigenvector at eigenvalue 1 (eig route),
  2. solving the singular linear system (pi (P - I) = 0 with the
     normalisation row appended),
  3. direct power iteration on the row vector.

It then turns the stationary occupancy into a long-run availability
and an annual downtime-cost figure, the engineering payoff of the
spectral calculation.

Run:
    uv run machine_reliability.py
"""

from __future__ import annotations

import csv
import pathlib

import numpy as np

STATES = ["running", "degraded", "down", "maintenance", "spare"]
# A state counts as "available" (producing) if running or degraded.
AVAILABLE = {"running", "degraded"}


def load_matrix(path: pathlib.Path) -> np.ndarray:
    """Read the transition matrix, skipping comment lines starting '#'."""
    rows: list[list[float]] = []
    with path.open() as handle:
        reader = csv.reader(line for line in handle if not line.startswith("#"))
        header = next(reader)  # from_state,running,degraded,...
        cols = header[1:]
        assert cols == STATES, f"unexpected column order: {cols}"
        for record in reader:
            rows.append([float(x) for x in record[1:]])
    matrix = np.array(rows)
    assert matrix.shape == (5, 5)
    np.testing.assert_allclose(matrix.sum(axis=1), 1.0, atol=1e-12)
    return matrix


def stationary_via_eig(transition: np.ndarray) -> np.ndarray:
    """Left eigenvector at eigenvalue 1, normalised to sum to one."""
    values, vectors = np.linalg.eig(transition.T)
    one = np.argmin(np.abs(values - 1.0))
    pi = np.real(vectors[:, one])
    return pi / pi.sum()


def stationary_via_solve(transition: np.ndarray) -> np.ndarray:
    """Solve pi (P - I) = 0 with the sum-to-one normalisation row."""
    n = transition.shape[0]
    a = (transition.T - np.eye(n))
    a[-1, :] = 1.0  # replace last equation by the normalisation
    b = np.zeros(n)
    b[-1] = 1.0
    return np.linalg.solve(a, b)


def stationary_via_power(
    transition: np.ndarray, steps: int = 500
) -> tuple[np.ndarray, np.ndarray]:
    """Power iteration on the row vector; return final pi and the trace."""
    n = transition.shape[0]
    pi = np.full(n, 1.0 / n)
    trace = [pi.copy()]
    for _ in range(steps):
        pi = pi @ transition
        trace.append(pi.copy())
    return pi, np.array(trace)


def second_eigenvalue_magnitude(transition: np.ndarray) -> float:
    values = np.linalg.eigvals(transition)
    mags = np.sort(np.abs(values))[::-1]
    return float(mags[1])


def main() -> None:
    here = pathlib.Path(__file__).resolve().parent
    path = here.parent / "data" / "machine_reliability_chain.csv"
    transition = load_matrix(path)

    pi_eig = stationary_via_eig(transition)
    pi_solve = stationary_via_solve(transition)
    pi_power, _ = stationary_via_power(transition)

    print("stationary distribution (eig / solve / power):")
    for i, name in enumerate(STATES):
        print(
            f"  {name:>12}: {pi_eig[i]:.5f}  {pi_solve[i]:.5f}  {pi_power[i]:.5f}"
        )

    # Agreement check across the three routes.
    np.testing.assert_allclose(pi_eig, pi_solve, atol=1e-9)
    np.testing.assert_allclose(pi_eig, pi_power, atol=1e-6)

    lam2 = second_eigenvalue_magnitude(transition)
    mixing = 1.0 / (1.0 - lam2)
    print(f"\n|lambda_2| = {lam2:.4f}  ->  mixing time ~ {mixing:.1f} shifts")

    availability = sum(
        pi_eig[i] for i, name in enumerate(STATES) if name in AVAILABLE
    )
    print(f"long-run availability (running + degraded) = {availability:.4f}")
    print(f"long-run unavailability                    = {1 - availability:.4f}")

    # Annual downtime-cost: 3 shifts/day, 365 days, lost-margin per
    # shift of unavailability. Numbers are illustrative inputs.
    shifts_per_year = 3 * 365
    lost_margin_per_shift = 4_000.0  # currency units of lost contribution
    annual_cost = (1 - availability) * shifts_per_year * lost_margin_per_shift
    print(
        f"annual downtime cost at {lost_margin_per_shift:,.0f}/shift "
        f"over {shifts_per_year} shifts = {annual_cost:,.0f}"
    )


if __name__ == "__main__":
    main()
