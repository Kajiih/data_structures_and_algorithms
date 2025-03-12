import pytest
from data_structures_and_algorithms.khan import khan_dfs, khan_bfs


# Fixture to provide implementations
@pytest.fixture(params=[khan_dfs, khan_bfs])
def khan_func(request):
    return request.param


def test_khan_valid_topological_sort(khan_func):
    # Simple DAG
    assert khan_func(3, [(0, 1), (1, 2)]) == [0, 1, 2]

    # More complex DAG
    result = khan_func(6, [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)])
    assert result is not None
    assert result.index(5) < result.index(2)
    assert result.index(5) < result.index(0)
    assert result.index(4) < result.index(0)
    assert result.index(4) < result.index(1)
    assert result.index(2) < result.index(3)
    assert result.index(3) < result.index(1)


def test_khan_cycle_detection(khan_func):
    # Simple cycle
    assert khan_func(3, [(0, 1), (1, 2), (2, 0)]) is None

    # Complex cycle
    assert khan_func(4, [(0, 1), (1, 2), (2, 3), (3, 1)]) is None


def test_khan_disconnected_components(khan_func):
    # Two independent chains
    result = khan_func(6, [(0, 1), (2, 3), (4, 5)])
    assert result is not None
    assert set(result) == {0, 1, 2, 3, 4, 5}
    assert result.index(0) < result.index(1)
    assert result.index(2) < result.index(3)
    assert result.index(4) < result.index(5)


def test_khan_single_node(khan_func):
    assert khan_func(1, []) == [0]


def test_khan_no_edges(khan_func):
    res = khan_func(3, [])
    assert res is not None
    assert set(res) == {0, 1, 2}


def test_visited_twice(khan_func):
    res = khan_func(3, [(0, 2), (1, 2)])
    assert res is not None
    assert res.index(0) < res.index(2)
    assert res.index(1) < res.index(2)


def test_khan_cycle_detection_propagation(khan_func):
    """
    Test case to verify that the cycle detection is properly propagated in the dfs function.
    The graph contains a cycle, and the traversal should stop as soon as the cycle is detected.
    """
    n = 6
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 4)]  # Forms a cycle

    # Run the khan function
    result = khan_func(n, edges)

    # The graph has a cycle, so the result should be None
    assert result is None, (
        "Cycle detection failed: the function did not return None for a graph with a cycle"
    )
