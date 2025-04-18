"""
Disjoint Set (DSU), or Union Find.

A data structure representing partitions of elements (like equivalence classes)
with efficient set union (merge) and find (membership test).


More: https://cp-algorithms.com/data_structures/disjoint_set_union.html

Use cases:
- Minimum Spanning Tree (Kruskal)
- Counting connected components

Operations:
- Find: Return the representative of an element (its class)
    - O(a(n))
- Union: Merge two classes
    - O(a(n))

Time Complexity with path compression and union by rank:
- Creation: O(n)
- Union, Find: O(a(n))


Tips:
- Rank is lower or equal to the height of the tree of a given class.
- In union, put the lowest in the largest to have the minimum height.
"""


class DisjointSet:
    """Disjoint Set implementation with path compression and rank union."""

    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [1] * n

    def find(self, x: int) -> int:
        """Return the class index of x."""
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # Path compression
            x = self.parent[x]

        return x

    def union(self, x: int, y: int) -> None:
        """Merge x's and y's classes ."""
        x_par, y_par = self.find(x), self.find(y)
        if x_par == y_par:
            return

        # Rank union: merge in the largest rank
        if self.rank[x_par] > self.rank[y_par]:
            self.parent[y_par] = x_par
        elif self.rank[y_par] > self.rank[x_par]:
            self.parent[x_par] = y_par
        else:
            self.parent[y_par] = x_par
            self.rank[x_par] += 1
