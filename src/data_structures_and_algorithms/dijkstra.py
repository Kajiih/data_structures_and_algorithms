"""
Dijkstra's algorithm.

Breadth first search with priority queue, for graph weighted with non-negative edges.

Use cases:
- Shortest path (single source, single target) in weighted graph with no negative edges.

Algorithm:
- Replace the double-ended queue by a priority queue, and store the distance to
    the node in the priority queue.

Complexity: V nodes and E edges
- O(E log E) ~ O(E log V)
    - Each edge can be taken at most once
    - Push and pop cost of the priority queue for each (at most E edges in the priority queue)

Tips:
- check visited when iterating on neighbors to save the push an pop cost
"""

from collections.abc import Iterable
from heapq import heappop, heappush


def dijkstra(n: int, edges: Iterable[tuple[int, int, float]], src: int, dest: int) -> float | None:
    """Return the shortest path from src to dest in the graph or None if no path exists."""
    # Adjacency list
    neighbors = [[] for _ in range(n)]
    for i, j, w in edges:
        neighbors[i].append((w, j))  # (weight, node)

    # BFS with priority queue
    pq = [(0, src)]
    visited = [False] * n
    while pq:
        # Base case
        dist, node = heappop(pq)
        if node == dest:
            return dist

        # Iteration
        for w, neib in neighbors[node]:
            if visited[neib]:
                continue
            heappush(pq, (dist + w, neib))

    return None
