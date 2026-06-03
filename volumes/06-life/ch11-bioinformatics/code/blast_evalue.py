"""
Karlin-Altschul E-value calculator for BLAST-style local alignment.

The E-value of a raw score S against a database of size n with a query
of length m is

    E = K * m * n * exp(-lambda * S)

where K and lambda are Karlin-Altschul parameters that depend only on the
scoring system and the residue composition.

Dependencies:
  numpy (only for the sweep table)

Usage:
  python blast_evalue.py

Supports Volume VI, Chapter 11, Section 11.1 (sequence search), the
derivation exercise on the E-value extreme-value distribution, and the
simulation exercise on database-size scaling.
"""

from __future__ import annotations

import math


def evalue(
    raw_score: float,
    query_len: int,
    db_size: int,
    K: float = 0.1,
    lambd: float = 0.3,
) -> float:
    """Karlin-Altschul E-value for a BLAST hit.

    Args:
        raw_score: raw alignment score in score-system units.
        query_len: number of residues in the query (m).
        db_size: total number of residues in the database (n).
        K: Karlin-Altschul scoring-system constant.
        lambd: scoring-system scale (per bit when raw_score is in bits).

    Returns:
        E-value (expected number of hits at this score by chance).
    """
    return K * query_len * db_size * math.exp(-lambd * raw_score)


def bit_score(raw_score: float, K: float, lambd: float) -> float:
    """Normalised bit score: S' = (lambda * S - ln K) / ln 2."""
    return (lambd * raw_score - math.log(K)) / math.log(2.0)


def evalue_from_bits(bits: float, query_len: int, db_size: int) -> float:
    """E-value from a bit score: E = m * n / 2^bits."""
    return query_len * db_size / (2.0 ** bits)


def sweep_database_size() -> None:
    """Print a table of E-values vs database size at fixed raw scores."""
    m = 300
    K = 0.1
    lambd = 0.3
    print(f"Query length m = {m} aa, K = {K}, lambda = {lambd} per bit")
    print(f"{'n (Gbp)':>10}  {'S=60':>10}  {'S=80':>10}  {'S=100':>10}  {'S=120':>10}")
    for n_gb in [0.01, 0.05, 0.2, 1.0, 5.0, 10.0, 50.0]:
        n = int(n_gb * 1e9)
        row = [evalue(s, m, n, K, lambd) for s in (60, 80, 100, 120)]
        print(f"{n_gb:>10.2f}  " + "  ".join(f"{e:>10.2e}" for e in row))


def main() -> None:
    print("Example 1: single hit")
    S, m, n = 95.0, 300, int(2e9)
    e = evalue(S, m, n)
    b = bit_score(S, K=0.1, lambd=0.3)
    print(f"  raw S = {S} bits, m = {m}, n = {n}")
    print(f"  bit score = {b:.2f}")
    print(f"  E-value   = {e:.2e}")
    print()

    print("Example 2: sweep over database size")
    sweep_database_size()


if __name__ == "__main__":
    main()
