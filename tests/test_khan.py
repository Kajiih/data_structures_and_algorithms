from data_structures_and_algorithms.khan import khan


def test_khan_valid_topological_sort():
    # Simple DAG
    assert khan(3, [(0, 1), (1, 2)]) == [0, 1, 2]

    # More complex DAG
    result = khan(6, [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)])
    assert result is not None
    assert result.index(5) < result.index(2)
    assert result.index(5) < result.index(0)
    assert result.index(4) < result.index(0)
    assert result.index(4) < result.index(1)
    assert result.index(2) < result.index(3)
    assert result.index(3) < result.index(1)


def test_khan_cycle_detection():
    # Simple cycle
    assert khan(3, [(0, 1), (1, 2), (2, 0)]) is None

    # Complex cycle
    assert khan(4, [(0, 1), (1, 2), (2, 3), (3, 1)]) is None


def test_khan_disconnected_components():
    # Two independent chains
    result = khan(6, [(0, 1), (2, 3), (4, 5)])
    assert result is not None
    assert set(result) == {0, 1, 2, 3, 4, 5}
    assert result.index(0) < result.index(1)
    assert result.index(2) < result.index(3)
    assert result.index(4) < result.index(5)


def test_khan_single_node():
    assert khan(1, []) == [0]


def test_khan_no_edges():
    res = khan(3, [])
    assert res is not None
    assert set(res) == {0, 1, 2}
