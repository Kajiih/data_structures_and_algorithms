from data_structures_and_algorithms.dijkstra import dijkstra


# Test case 1: Basic case with a simple graph
def test_simple_graph():
    edges = [(0, 1, 1), (1, 2, 2), (0, 2, 4)]
    result = dijkstra(3, edges, 0, 2)
    assert result == [0, 1, 2], f"Expected [0, 1, 2], but got {result}"


# Test case 2: No path exists between source and destination
def test_no_path():
    edges = [(0, 1, 1), (2, 3, 1)]
    result = dijkstra(4, edges, 0, 3)
    assert result is None, f"Expected None, but got {result}"


# Test case 3: Graph with multiple paths and varying weights
def test_multiple_paths():
    edges = [(0, 1, 2), (1, 2, 2), (0, 2, 5), (1, 3, 1), (2, 3, 3)]
    result = dijkstra(4, edges, 0, 3)
    assert result == [0, 1, 3], f"Expected [0, 1, 3], but got {result}"


# Test case 4: Single node graph
def test_single_node():
    edges = []
    result = dijkstra(1, edges, 0, 0)
    assert result == [0], f"Expected [0], but got {result}"


# Test case 5: Disconnected graph with multiple components
def test_disconnected_graph():
    edges = [(0, 1, 1), (1, 2, 1)]
    result = dijkstra(4, edges, 0, 3)
    assert result is None, f"Expected None, but got {result}"


# Test case 6: Empty graph
def test_empty_graph():
    edges = []
    result = dijkstra(0, edges, 0, 0)
    assert result is None, f"Expected None, but got {result}"


# Test case 7: Graph with the same distance for multiple paths
def test_equal_distances():
    edges = [(0, 1, 1), (0, 2, 1), (1, 3, 1), (2, 3, 1)]
    result = dijkstra(4, edges, 0, 3)
    assert result in [[0, 1, 3], [0, 2, 3]], f"Expected [0, 1, 3] or [0, 2, 3], but got {result}"


# Test case 8: Large graph (edge case testing performance)
def test_large_graph():
    edges = [(i, i + 1, 1) for i in range(9999)]  # A chain of 10000 nodes
    result = dijkstra(10000, edges, 0, 9999)
    assert result == list(range(10000)), f"Expected a path from 0 to 9999, but got {result}"


# Test case 9: Source is the same as destination
def test_source_equals_destination():
    edges = [(0, 1, 1), (1, 2, 1)]
    result = dijkstra(3, edges, 0, 0)
    assert result == [0], f"Expected [0], but got {result}"
