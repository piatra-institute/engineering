# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Erdos-Renyi random graph generator and giant-component sweep.

Reference: Erdos and Renyi, 'On the evolution of random graphs,'
Publ. Math. Inst. Hungar. Acad. Sci. 5, 1960. The classical result
is the emergence of a unique giant connected component as the edge
probability crosses p = 1/n, exactly the threshold the simulation
exercise asks the reader to reproduce.

Run: uv run code/erdos_renyi.py
"""

from __future__ import annotations

import random
from collections import deque


def generate_gnp(n: int, p: float, seed: int = 0) -> list[list[int]]:
    """G(n, p) Erdos-Renyi graph as adjacency lists."""
    rng = random.Random(seed)
    adj: list[list[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if rng.random() < p:
                adj[u].append(v)
                adj[v].append(u)
    return adj


def largest_component_size(adj: list[list[int]]) -> int:
    n = len(adj)
    seen = [False] * n
    best = 0
    for root in range(n):
        if seen[root]:
            continue
        size = 0
        queue: deque[int] = deque([root])
        seen[root] = True
        while queue:
            u = queue.popleft()
            size += 1
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    queue.append(v)
        best = max(best, size)
    return best


def sweep(n: int = 1000) -> list[tuple[float, int, float]]:
    """Return [(p, lcc_size, lcc_fraction)] for c in {0.5, 1, 2, 4, 8}."""
    rows: list[tuple[float, int, float]] = []
    for c in (0.5, 1.0, 2.0, 4.0, 8.0):
        p = c / n
        adj = generate_gnp(n, p, seed=42)
        lcc = largest_component_size(adj)
        rows.append((p, lcc, lcc / n))
    return rows


if __name__ == "__main__":
    print(f"{'c=np':>6}  {'p':>9}  {'|LCC|':>7}  {'|LCC|/n':>8}")
    for p, lcc, frac in sweep(1000):
        print(f"{p*1000:>6.2f}  {p:>9.5f}  {lcc:>7d}  {frac:>8.3f}")
