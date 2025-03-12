"""
Khan's algorithm.

Return a topological sort of the graph if it is possible, and detects cycles.
Works for multiple connected components.

Algorithm:
- Count the incoming degree of each node
- Initialize empty order list
- DFS (or BFS) starting on every node with incoming degree 0:
    - Base case:
        - Add node to the order
    - Recursion; for each neighbor node:
        - Decrement its degree by one
        - Run dfs on it if its degree is 0
- !!Check if the length of the order is the same as the number of nodes, as there could be connected components without node of degree 0

Note: Can also be done by removing edges in the graph instead of counting incoming degree.
In this case, you can the check if there is any remaining edges instead of checking the length of the order

Complexity:
- O(V + E) as a traversal where each node is visited once and each edge taken once

Tips:
- Start the traversal on each node with incoming degree of 0 to handle multiple connected components.
- Check the length of the order at the end in case there is a connected component without any node of incoming degree 0
- !!You don't need to explicitly check for cycles since a cycle will never be added to the order list -> so no need visited array either
"""

from collections import deque
from collections.abc import Iterable


def khan_dfs(n: int, edges: Iterable[tuple[int, int]]) -> list[int] | None:
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
    order = []

    def dfs(node: int) -> None:
        # Base case
        order.append(node)

        # Recursion
        for neib in neighbors[node]:
            in_degrees[neib] -= 1
            if in_degrees[neib] == 0:
                dfs(neib)

    sources = [node for node, degree in enumerate(in_degrees) if degree == 0]
    for node in sources:
        dfs(node)

    # Check if the length is coherent
    if len(order) != n:
        print(order)
    return order if len(order) == n else None


def khan_bfs(n: int, edges: Iterable[tuple[int, int]]) -> list[int] | None:
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
    order = []

    q = deque([node for node, degree in enumerate(in_degrees) if degree == 0])

    while q:
        node = q.popleft()
        # Base case
        order.append(node)

        # iteration
        for neib in neighbors[node]:
            in_degrees[neib] -= 1
            if in_degrees[neib] == 0:
                q.append(neib)

    # Check if the length is coherent
    if len(order) != n:
        print(order)

    return order if len(order) == n else None
