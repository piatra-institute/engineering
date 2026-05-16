#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# ///
"""
Union bound vs independence vs perfect-positive-dependence: numerical
tabulation of the joint failure probability of n events under three
assumed dependence structures.

For n events each with marginal probability p,
    independence:           P(at least one) = 1 - (1 - p)^n
    union bound (upper):    sum of marginals = n * p, clipped at 1
    perfect positive dep.:  P(at least one) = p (events occur together)

Supports the estimation block on the union bound and the judgement
exercise on independence-vs-union-bound.

Dependencies:
    standard library only.

Usage:
    uv run union_bound_check.py
"""

from __future__ import annotations


def main() -> None:
    print("Union bound (independent vs perfect-positive-dependence)\n")
    print(f"{'n':>4} {'p':>8} {'independent':>14}"
          f" {'union bound':>14} {'perfect+dep.':>14} {'gap factor':>12}")

    for n in (5, 10, 100):
        for p in (0.001, 0.01, 0.05, 0.1):
            indep = 1.0 - (1.0 - p) ** n
            union = min(n * p, 1.0)
            perfect = p
            gap = (union / indep) if indep > 0 else float("inf")
            print(
                f"{n:>4d} {p:>8.4f}"
                f" {indep:>14.6f} {union:>14.6f}"
                f" {perfect:>14.6f} {gap:>12.4f}"
            )
        print()

    print(
        "Reading: independence and union bound agree to two significant"
        " figures when np is small (np << 1). They diverge when np ~ 1."
        " Perfect positive dependence reduces the union-event probability"
        " to a single marginal, several orders of magnitude below the"
        " independence value when n is large. The engineer choosing"
        " between models needs the correlation structure that the data"
        " (rarely) provide; section 13.8 names this as the dominant"
        " source of underestimated tail risk in safety analysis and"
        " finance."
    )


if __name__ == "__main__":
    main()
