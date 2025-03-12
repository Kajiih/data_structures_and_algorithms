"""
Kruskal's algorithm.

Return the edges forming a minimum spanning tree of a graph.
It works for negative weights.

Algorithm:
- Sort the edges.
- Try them one by one, keep it if it links 2 disjoint sets of nodes (using Union-Find).
    - Stop when all nodes belong to the same connected component or no more
        edges (if there is more than 1 single connected component).

Complexity:
- O(E log E) ~ O(E log V) for sorting
- O(E a(n)) for the main loop

Tips:
- Use a disjoint set for the main loop.
"""

import operator


def kruskal[T: int | float](n: int, edges: list[tuple[int, int, T]]) -> list[tuple[int, int, T]]:
    """
    Return the edges of a minimum spanning tree.

    Edges are given as:  (u, v, w), where w is the weight.
    """
    # 1. Sort the edges
    edges.sort(key=operator.itemgetter(2))

    # 2. Implement a disjoint set
    rank = [1] * n
    parent = list(range(n))

    def find(x: int) -> int:
        par = x
        while parent[par] != par:
            parent[par] = parent[parent[par]]  # Path compression
            par = parent[par]
        return par

    def union(a: int, b: int) -> bool:
        """Merge and return if a merge was performed."""
        a_p = find(a)
        b_p = find(b)

        if a_p == b_p:
            return False

        # Rank based union
        if rank[a_p] > rank[b_p]:
            parent[b_p] = a_p
        elif rank[b_p] > rank[a_p]:
            parent[a_p] = b_p
        else:
            parent[b_p] = a_p
            rank[a_p] += 1

        return True

    # 3. Select edges
    res = []

    for edge in edges:
        u, v, _ = edge

        if union(u, v):
            res.append(edge)
            if len(res) == n - 1:
                return res

    return res
