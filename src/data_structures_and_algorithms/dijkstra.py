"""
Dijkstra's algorithm.

A greedy algorithm using a priority queue to find the shortest path from a
single source to every other nodes (or a single one) in a weighted graph with
non-negative edges.

Use cases:
- Shortest path to every node or a single node in weighted graph with no negative edges.

Algorithm:
- Initialize dist (inf) and prev arrays (-1)
- Like breadth first search but with a priority queue containing the shortest length of the path to the current node passing by the previous node.
- When a node is visited, its distance is the shortest path from the source to the node.
    - Update prev
    - Break when dest is found
    - Iterate on neighbors if there distance would decrease
        - Update their distance in the loop
- Reconstruct the path with prev (and reverse it)

Complexity: V nodes and E edges
- O(E log E) ~ O(E log V)
    - Each edge can be taken at most once
    - Push and pop cost of the priority queue for each (at most E edges in the priority queue)

Tips:
- In base case, check prev to see if the node is visited and update prev
- In loop, check new neighbor distance and update and push if lower to avoid useless push cost
- Remember to reverse the path at the end
"""

from collections.abc import Iterable
from heapq import heappop, heappush

INF = float("inf")


def dijkstra(
    n: int, edges: Iterable[tuple[int, int, float]], src: int, dest: int
) -> list[int] | None:
    """Return the shortest path from src to dest in the graph or None if no path exists."""
    # Edges cases
    if n == 0:
        return None
    # Adjacency list
    neighbors = [[] for _ in range(n)]
    for i, j, w in edges:
        neighbors[i].append((w, j))  # (weight, node)

    # BFS with priority queue
    pq = [(0, src, -1)]
    dist = [INF] * n
    dist[src] = 0
    prev = [-1] * n

    while pq:
        node_dist, node, prev_node = heappop(pq)
        # Base case
        if prev[node] != -1:
            continue
        prev[node] = prev_node
        if node == dest:
            break

        # Iteration
        for w, neib in neighbors[node]:
            neib_dist = w + node_dist
            if neib_dist >= dist[neib]:
                continue
            dist[neib] = neib_dist
            heappush(pq, (neib_dist, neib, node))
    else:
        return None

    # Reconstruct the path
    path = []
    node = dest
    while node != -1:
        path.append(node)
        node = prev[node]

    return path[::-1]
