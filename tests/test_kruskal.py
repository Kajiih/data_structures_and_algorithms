from data_structures_and_algorithms.kruskal import kruskal


def total_weight(edges: list[tuple[int, int, float]]) -> float:
    """Compute the total weight of an edge list."""
    return sum(w for _, _, w in edges)


def test_empty_graph():
    """Test that a graph with a single node returns an empty MST."""
    n = 1
    edges = []
    mst = kruskal(n, edges)
    assert mst == [], "A single-node graph should produce an empty MST."


def test_single_edge():
    """Test that a graph with two nodes and one edge returns that edge."""
    n = 2
    edges = [(0, 1, 1.0)]
    mst = kruskal(n, edges)
    assert len(mst) == 1, "MST should have one edge for a two-node graph."
    assert mst[0] == (0, 1, 1.0), "The MST edge should match the input edge."


def test_triangle_graph():
    """Test a triangle graph (3 nodes, 3 edges) where the MST should include the two lowest-weight edges."""
    n = 3
    edges = [(0, 1, 1.0), (1, 2, 1.0), (0, 2, 2.0)]
    mst = kruskal(n, edges)
    # The MST should have 2 edges with a total weight of 2.0.
    assert len(mst) == 2, "MST for a triangle graph should have 2 edges."
    assert total_weight(mst) == 2.0, "Total weight of MST should be 2.0."
    # Ensure that the heavier edge (weight 2.0) is not selected.
    for edge in mst:
        assert edge[2] != 2.0, "The edge with weight 2.0 should not be part of the MST."


def test_disconnected_graph():
    """Test a disconnected graph. The MST function returns the edges available even if the graph is not fully connected."""
    n = 4
    # Two disconnected components: component1: (0,1) and component2: (2,3).
    edges = [(0, 1, 1.0), (2, 3, 1.0)]
    mst = kruskal(n, edges)
    # Since the graph is disconnected, we expect exactly the two provided edges.
    assert len(mst) == 2, "Disconnected graph should return the available edges."
    assert set(mst) == {(0, 1, 1.0), (2, 3, 1.0)}, "The MST should include the given edges."


def test_complex_graph():
    """Test a more complex graph and verify the total weight of the MST."""
    n = 5
    # Graph edges: (u, v, weight)
    # Example graph:
    # 0-1: 4, 0-2: 3, 1-2: 1, 1-3: 2, 2-3: 4, 3-4: 2, 2-4: 5.
    edges = [
        (0, 1, 4.0),
        (0, 2, 3.0),
        (1, 2, 1.0),
        (1, 3, 2.0),
        (2, 3, 4.0),
        (3, 4, 2.0),
        (2, 4, 5.0),
    ]
    mst = kruskal(n, edges)
    # For a connected graph of 5 nodes, a valid MST should have 4 edges.
    assert len(mst) == 4, "MST should have n-1 edges for a connected graph."
    # Expected MST (by weight): (1,2,1.0), (1,3,2.0), (3,4,2.0), (0,2,3.0) with total weight = 8.0.
    assert total_weight(mst) == 8.0, "Total weight of the MST should be 8.0."
