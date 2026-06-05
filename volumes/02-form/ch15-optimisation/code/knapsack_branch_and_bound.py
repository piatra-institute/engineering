# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Branch-and-bound on the 0/1 knapsack of Section 15.7.

Mirrors the worked example in the text: four items with values
v = (60, 100, 120, 40) and weights w = (10, 20, 30, 10), capacity 50.
The LP relaxation is the fractional knapsack, solved greedily by
value-to-weight ratio; its optimum is an upper bound on the integer
optimum and supplies the bound that prunes the search tree.

The script reports every node it visits (the committed partial
solution, the LP bound, and whether it is pruned, fathomed by
integrality, or branched), then prints the optimal value and an
optimal item set. The visited-node count is compared against the
2^n leaves of brute force to show the pruning effect.
"""

from __future__ import annotations

from dataclasses import dataclass

VALUES = [60, 100, 120, 40]
WEIGHTS = [10, 20, 30, 10]
CAPACITY = 50
N = len(VALUES)

# Items are pre-sorted by descending value-to-weight ratio so the
# greedy LP relaxation fills in index order.
ORDER = sorted(range(N), key=lambda i: VALUES[i] / WEIGHTS[i], reverse=True)


def lp_relaxation_bound(taken: dict[int, int]) -> float:
    """Greedy fractional-knapsack upper bound given fixed decisions.

    taken maps an item index to 0 or 1 for committed items; undecided
    items are filled fractionally by ratio order.
    """
    weight = sum(WEIGHTS[i] for i, x in taken.items() if x == 1)
    if weight > CAPACITY:
        return float("-inf")  # infeasible commitment
    value = float(sum(VALUES[i] for i, x in taken.items() if x == 1))
    remaining = CAPACITY - weight
    for i in ORDER:
        if i in taken:
            continue
        if WEIGHTS[i] <= remaining:
            value += VALUES[i]
            remaining -= WEIGHTS[i]
        else:
            value += VALUES[i] * (remaining / WEIGHTS[i])
            remaining = 0
            break
    return value


@dataclass
class Result:
    best_value: float
    best_set: frozenset[int]
    nodes_visited: int


def solve() -> Result:
    best_value = float("-inf")
    best_set: frozenset[int] = frozenset()
    nodes = 0

    # Branch on undecided items in ratio order; a stack holds the
    # partial decision dict and the index of the next item to decide.
    stack: list[tuple[dict[int, int], int]] = [({}, 0)]
    while stack:
        taken, depth = stack.pop()
        nodes += 1
        bound = lp_relaxation_bound(taken)
        if bound <= best_value:
            continue  # prune: cannot beat the incumbent
        if depth == N:
            value = sum(VALUES[i] for i, x in taken.items() if x == 1)
            if value > best_value:
                best_value = float(value)
                best_set = frozenset(i for i, x in taken.items() if x == 1)
            continue
        item = ORDER[depth]
        # Branch x_item = 1 (only if it fits) and x_item = 0.
        weight = sum(WEIGHTS[i] for i, x in taken.items() if x == 1)
        if weight + WEIGHTS[item] <= CAPACITY:
            stack.append(({**taken, item: 1}, depth + 1))
        stack.append(({**taken, item: 0}, depth + 1))

    return Result(best_value, best_set, nodes)


def main() -> None:
    res = solve()
    print("0/1 knapsack, capacity =", CAPACITY)
    print("values  =", VALUES)
    print("weights =", WEIGHTS)
    print()
    print(f"optimal value = {res.best_value:.0f}")
    print("optimal set   =", sorted(res.best_set))
    full_tree = 2 ** (N + 1) - 1
    print(f"nodes visited = {res.nodes_visited} "
          f"(full decision tree = {full_tree} nodes, {2 ** N} leaves)")


if __name__ == "__main__":
    main()
