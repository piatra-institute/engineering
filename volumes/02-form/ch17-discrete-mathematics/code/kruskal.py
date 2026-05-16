# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Kruskal minimum-spanning-tree algorithm with union-find.

Reference: CLRS chapter 23. The union-find uses union by rank and
path compression, giving the inverse-Ackermann-time amortised
operation cited in section 17.3.

Run: uv run code/kruskal.py
"""

from __future__ import annotations

from typing import Hashable

Vertex = Hashable
Edge = tuple[Vertex, Vertex, float]


class UnionFind:
    def __init__(self, vertices: list[Vertex]) -> None:
        self.parent: dict[Vertex, Vertex] = {v: v for v in vertices}
        self.rank: dict[Vertex, int] = {v: 0 for v in vertices}

    def find(self, x: Vertex) -> Vertex:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, x: Vertex, y: Vertex) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def kruskal(vertices: list[Vertex], edges: list[Edge]) -> tuple[list[Edge], float]:
    uf = UnionFind(vertices)
    tree: list[Edge] = []
    total = 0.0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if uf.union(u, v):
            tree.append((u, v, w))
            total += w
        if len(tree) == len(vertices) - 1:
            break
    return tree, total


def example_exercise_5() -> tuple[list[Edge], float]:
    """Reproduce exercise 17.5 from section 17.9."""
    vertices = [1, 2, 3, 4, 5]
    edges: list[Edge] = [
        (1, 2, 1),
        (2, 3, 4),
        (1, 3, 3),
        (3, 4, 2),
        (4, 5, 5),
        (2, 4, 6),
    ]
    return kruskal(vertices, edges)


if __name__ == "__main__":
    tree, total = example_exercise_5()
    for u, v, w in tree:
        print(f"{u} -- {v}  (w = {w})")
    print(f"total weight = {total}")
    assert total == 11, f"expected MST weight 11, got {total}"
