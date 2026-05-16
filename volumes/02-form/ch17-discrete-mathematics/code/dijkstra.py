# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Dijkstra single-source shortest path with a binary heap.

Reference: CLRS chapter 24. The implementation is the standard
textbook form; it serves the simulation exercise in section 17.9
and the trace shown in figure fig:vol02:ch17:dijkstra-trace.

The graph is given as an adjacency dict mapping a vertex to a list
of (neighbour, weight) pairs. Weights must be non-negative;
negative weights silently violate the algorithm's correctness
invariant. Use bellman_ford.py for graphs with negative edges.

Run: uv run code/dijkstra.py
"""

from __future__ import annotations

import heapq
import math
from typing import Hashable

Vertex = Hashable
Graph = dict[Vertex, list[tuple[Vertex, float]]]


def dijkstra(graph: Graph, source: Vertex) -> dict[Vertex, float]:
    distance: dict[Vertex, float] = {v: math.inf for v in graph}
    distance[source] = 0.0
    heap: list[tuple[float, Vertex]] = [(0.0, source)]

    while heap:
        d_u, u = heapq.heappop(heap)
        if d_u > distance[u]:
            continue
        for v, w in graph.get(u, []):
            if w < 0:
                raise ValueError(
                    f"negative edge weight {w} on ({u}, {v}); use bellman_ford"
                )
            tentative = d_u + w
            if tentative < distance[v]:
                distance[v] = tentative
                heapq.heappush(heap, (tentative, v))
    return distance


def example_exercise_4() -> dict[Vertex, float]:
    """Reproduce the trace of exercise 17.4 in section 17.9."""
    graph: Graph = {
        "s": [("a", 4), ("b", 2)],
        "a": [("c", 3), ("b", 1)],
        "b": [("c", 4), ("a", 1), ("t", 5)],
        "c": [("t", 2)],
        "t": [],
    }
    return dijkstra(graph, "s")


if __name__ == "__main__":
    result = example_exercise_4()
    expected = {"s": 0, "b": 2, "a": 3, "c": 6, "t": 8}
    for v, d in sorted(result.items(), key=lambda kv: (kv[1], str(kv[0]))):
        flag = "OK" if d == expected[v] else "MISMATCH"
        print(f"d(s, {v}) = {d}  [{flag}, expected {expected[v]}]")
