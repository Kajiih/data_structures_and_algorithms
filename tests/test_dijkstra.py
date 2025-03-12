from data_structures_and_algorithms.dijkstra import dijkstra


def test_no_path():
    """Test case where there is no path from src to dest."""
    edges = [(0, 1, 10), (1, 2, 10), (3, 2, 10)]
    n = 4
    src = 0
    dest = 3
    result = dijkstra(n, edges, src, dest)
    assert result is None, "Expected None as there is no valid path from src to dest"


def test_single_path():
    """Test case where there's exactly one path from src to dest."""
    edges = [(0, 1, 10), (1, 2, 10)]
    n = 3
    src = 0
    dest = 2
    result = dijkstra(n, edges, src, dest)
    assert result == 20, f"Expected 20 but got {result}"


def test_multiple_paths():
    """Test case where there are multiple paths, with one shorter than the others."""
    edges = [(0, 1, 10), (1, 2, 10), (0, 2, 5)]
    n = 3
    src = 0
    dest = 2
    result = dijkstra(n, edges, src, dest)
    assert result == 5, f"Expected 5 but got {result}"


def test_disconnected_graph():
    """Test case where src and dest are in disconnected components of the graph."""
    edges = [(0, 1, 10)]
    n = 3
    src = 0
    dest = 2
    result = dijkstra(n, edges, src, dest)
    assert result is None, "Expected None as there is no path between src and dest"


def test_multiple_edges_same_nodes():
    """Test case where there are multiple edges between the same nodes."""
    edges = [(0, 1, 10), (0, 1, 5), (1, 2, 10)]
    n = 3
    src = 0
    dest = 2
    result = dijkstra(n, edges, src, dest)
    assert result == 15, f"Expected 15 but got {result}"


def test_single_node():
    """Test case where the graph consists of only a single node."""
    edges = []
    n = 1
    src = 0
    dest = 0
    result = dijkstra(n, edges, src, dest)
    assert result == 0, f"Expected 0 but got {result}"


def test_large_graph():
    """Test case for performance with a large graph."""
    edges = [(i, i + 1, 1) for i in range(999)]  # Creating a linear graph with 1000 nodes
    n = 1000
    src = 0
    dest = 999
    result = dijkstra(n, edges, src, dest)
    assert result == 999, f"Expected 999 but got {result}"
