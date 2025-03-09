"""
Khan's algorithm.

Return a topological sort of the graph if it is possible, and detects cycles.
Works for multiple connected components.

Algorithm:
- Count the incoming degree of each node
- Initialize visited and a container for the ordered nodes
- DFS (or BFS) starting on every node with incoming degree 0 and not yet visited:
    - Base case:
        - If node already visited, it means there is a cycle; stop
        - Else, mark as visited and add to the order
    - Recursion; For each neighbor node:
        - Decrement its degree by one
        - Run dfs on it if its degree is 0
-!! Check if the length of the order is the same as the number of nodes, as there could be connected components without node of degree 0

Note: Can also be done by removing edges in the graph instead of counting incoming degree.
In this case, you can the check if there is any remaining edges instead of checking the length of the order

Complexity:
- O(V + E) as a traversal where each node is visited once and each edge taken once

Tips:
- Start the traversal on each node with incoming degree of 0 to handle multiple connected components.
- Check the length of the order at the end in case there is a connected component without any node of incoming degree 0
"""

from collections.abc import Iterable


def khan(n: int, edges: Iterable[tuple[int, int]]) -> list[int] | None:
    """
    Return a topological order if possible, and None if there is at least one cycle.

    Nodes are integers from 0 to n - 1 and edges are considered unique.
    Edges are given as:  (u, v), and the order is a list of nodes.
    """
    # 1. Create graph, e.g. as adjacency list and count incoming degrees
    in_degrees = [0] * n
    neighbors = [[] for _ in range(n)]

    for u, v in edges:
        in_degrees[v] += 1
        neighbors[u].append(v)

    # 2. Traversal on each node with in degree of 0
    visited = [False] * n
    order = []

    def dfs(node: int) -> bool:
        # Base case
        if visited[node]:
            return False
        visited[node] = True
        order.append(node)

        # Recursion
        for neib in neighbors[node]:
            in_degrees[neib] -= 1
            if in_degrees[neib] == 0:
                dfs(neib)

        return True

    for node in range(n):
        if in_degrees[node] == 0 and not visited[node]:
            is_cycle_free = dfs(node)
            if not is_cycle_free:
                return None

    # Check if the length is coherent
    return order if len(order) == n else None
