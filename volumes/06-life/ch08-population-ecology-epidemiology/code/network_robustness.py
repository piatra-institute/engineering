# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numpy",
#     "matplotlib",
# ]
# ///
"""Network robustness: random vs scale-free, with random-failure
versus targeted-attack curves.

Vol VI Ch 8 §8.4. Reproduces the Albert-Jeong-Barabasi 2000 result
on connectivity-collapse under attack on heavy-degree hubs.

Usage:
  uv run network_robustness.py
"""

import numpy as np
import matplotlib.pyplot as plt


def er_graph(n, p, rng):
    """Adjacency matrix for an Erdos-Renyi graph G(n, p)."""
    A = (rng.random((n, n)) < p).astype(int)
    A = np.triu(A, 1)
    A = A + A.T
    return A


def barabasi_albert(n, m, rng):
    """Adjacency matrix for a preferential-attachment graph BA(n, m)."""
    A = np.zeros((n, n), dtype=int)
    # Initial clique of m+1 nodes
    for i in range(m + 1):
        for j in range(i + 1, m + 1):
            A[i, j] = A[j, i] = 1
    degrees = A.sum(axis=1).astype(float)
    for new_node in range(m + 1, n):
        prob = degrees[:new_node] / degrees[:new_node].sum()
        chosen = rng.choice(new_node, size=m, replace=False, p=prob)
        for c in chosen:
            A[new_node, c] = A[c, new_node] = 1
        degrees[chosen] += 1
        degrees[new_node] = m
    return A


def largest_component_size(A):
    """Connected-component analysis by BFS."""
    n = A.shape[0]
    if n == 0:
        return 0
    seen = np.zeros(n, dtype=bool)
    sizes = []
    for start in range(n):
        if seen[start]:
            continue
        frontier = [start]
        size = 0
        while frontier:
            cur = frontier.pop()
            if seen[cur]:
                continue
            seen[cur] = True
            size += 1
            neighbours = np.where(A[cur] == 1)[0]
            frontier.extend(int(x) for x in neighbours if not seen[x])
        sizes.append(size)
    return max(sizes) if sizes else 0


def remove_nodes(A, order):
    """Return A with rows/cols zeroed in the given order, as a sequence."""
    A_cur = A.copy()
    sizes = []
    for k in range(len(order)):
        node = order[k]
        A_cur[node, :] = 0
        A_cur[:, node] = 0
        sizes.append(largest_component_size(A_cur))
    return np.array(sizes)


def main():
    rng = np.random.default_rng(0)
    n = 200
    # ER with same mean degree as BA(m=3): mean degree = 2 m = 6 -> p = 6/(n-1)
    A_er = er_graph(n, 6 / (n - 1), rng)
    A_ba = barabasi_albert(n, 3, rng)
    rand_order_er = rng.permutation(n)
    rand_order_ba = rng.permutation(n)
    attack_order_er = np.argsort(-A_er.sum(axis=1))
    attack_order_ba = np.argsort(-A_ba.sum(axis=1))
    rand_er = remove_nodes(A_er, rand_order_er)
    rand_ba = remove_nodes(A_ba, rand_order_ba)
    atk_er = remove_nodes(A_er, attack_order_er)
    atk_ba = remove_nodes(A_ba, attack_order_ba)
    frac = np.arange(1, n + 1) / n
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(frac, rand_er / n, "-", label="ER random failure")
    ax.plot(frac, atk_er / n, "--", label="ER targeted attack")
    ax.plot(frac, rand_ba / n, "-", label="BA random failure", color="C2")
    ax.plot(frac, atk_ba / n, "--", label="BA targeted attack", color="C3")
    ax.set_xlabel("fraction of nodes removed")
    ax.set_ylabel("largest-component size / n")
    ax.set_title("Network robustness: Erdos-Renyi vs Barabasi-Albert (n=200)")
    ax.legend()
    fig.tight_layout()
    fig.savefig("network_robustness.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
