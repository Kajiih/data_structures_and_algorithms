"""
Bellman-Ford's algorithm.

Compute the shortest path in a weighted graph from a source to all other nodes.

In contrary to Dijkstra, it supports graph with negative edges and detects
negative cycles (that would lead to arbitrarily low paths).

Also in contrary to Dijkstra that uses a greedy method, all edges are relaxed at
each iterations, and there are |V| - 1 iterations (morally, the shortest path passes
by at most |V| nodes).

Optimization are possible, where one can stop before the algorithm when there
was no changes during an iteration.
A second optimization is to relax only vertices whose distance value changed
since the last time  their edges have been relaxed, by keeping a collection of
vertices whose edges should be relaxed, removing a vertex when its edges are
relaxed, and adding it when its distance value changes.

Use cases:
- Shortest path in graph with negative edges, and therefore potentially negative cycles.

Algorithm:
-

Complexity: V nodes and E edges
    - O(V * E): E edges relaxed V - 1 times
    - with optimization: O(E * l) where l is the length of the maximum length of a shortest path

Tips:
- We don't need adjacency list or matrix, the list of edges is enough
- To detect negative cycles, check for an edge where dist[u] + w < dist[v]: it can only exist if there is a negative cycle and the edge is reachable from the cycle
    - Go backward predecessors keeping track of visited nodes until you visit a node twice. This node is on the cycle.
    - Then you can reconstruct the cycle.
"""

from collections.abc import Iterable

INF = float("inf")


def bellman_ford(
    n: int, edges: Iterable[tuple[int, int, float]], src: int
) -> tuple[list[float], list[int]] | None:
    """Return the shortest path from the source to all nodes in the graph or None if a negative cycle is detected."""
    predecessors = [-1] * n
    dist = [INF] * n
    dist[src] = 0

    # Relax each edges n - 1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                predecessors[v] = u

    # Detect negative cycles: Last scan to see if there are still updates
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None  # Negative cycle detected

    return dist, predecessors


def bellman_ford_opti(
    n: int, edges: Iterable[tuple[int, int, float]], src: int
) -> tuple[list[float], list[int]] | tuple[None, list[int]]:
    """Return shortest paths or a detected negative cycle."""
    predecessors = [-1] * n
    dist = [INF] * n
    dist[src] = 0

    # Relax each edges n - 1 times
    for _ in range(n - 1):
        keep_iterating = False
        for u, v, w in edges:
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                keep_iterating = True
                dist[v] = new_dist
                predecessors[v] = u
        if not keep_iterating:
            return dist, predecessors

    # Detect negative cycles: Last scan to see if there are still updates
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            # v is reachable from a negative cycle
            predecessors[v] = u

            # Find the cycle
            visited = [False] * n
            visited[v] = True

            current = u
            while not visited[current]:
                visited[current] = True
                current = predecessors[current]
            # node is now a vertex in a negative cycle
            cycle_node = current
            cycle = [cycle_node]
            while predecessors[current] != cycle_node:
                current = predecessors[current]
                cycle.append(current)
            cycle.reverse()

            return None, cycle

    return dist, predecessors
