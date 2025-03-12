from data_structures_and_algorithms.bellman_ford import bellman_ford, bellman_ford_opti

INF = float("inf")


def test_bellman_ford_simple_graph():
    n = 3
    edges = [(0, 1, 1), (0, 2, 4), (1, 2, 2)]
    src = 0
    result = bellman_ford(n, edges, src)
    assert result is not None
    dist, pred = result
    assert dist == [0, 1, 3]
    assert pred == [-1, 0, 1]


def test_bellman_ford_negative_edge_no_cycle():
    n = 3
    edges = [(0, 1, -1), (1, 2, 2)]
    src = 0
    result = bellman_ford(n, edges, src)
    assert result is not None
    dist, pred = result
    assert dist == [0, -1, 1]
    assert pred == [-1, 0, 1]


def test_bellman_ford_unreachable_negative_cycle():
    n = 4
    edges = [(0, 1, 1), (2, 3, 1), (3, 2, -3)]
    src = 0
    result = bellman_ford(n, edges, src)
    assert result is not None
    dist, pred = result
    assert dist[0] == 0
    assert dist[1] == 1
    assert dist[2] == INF
    assert dist[3] == INF
    assert pred == [-1, 0, -1, -1]


def test_bellman_ford_reachable_negative_cycle():
    n = 3
    edges = [(0, 1, 2), (1, 2, 1), (2, 0, -4)]
    src = 0
    result = bellman_ford(n, edges, src)
    assert result is None


def test_bellman_ford_source_in_negative_cycle():
    n = 3
    edges = [(0, 1, 1), (1, 2, -2), (2, 0, -1)]
    src = 0
    result = bellman_ford(n, edges, src)
    assert result is None


def test_bellman_ford_opti_returns_cycle():
    n = 3
    edges = [(0, 1, 2), (1, 2, 1), (2, 0, -4)]
    src = 0
    result, cycle = bellman_ford_opti(n, edges, src)
    assert result is None
    assert set(cycle) == {0, 1, 2}


def test_bellman_ford_opti_negative_cycle_unreachable():
    n = 4
    edges = [(0, 1, 1), (2, 3, 1), (3, 2, -3)]
    src = 0
    dist, pred = bellman_ford_opti(n, edges, src)
    assert dist is not None
    assert dist[0] == 0
    assert dist[1] == 1
    assert dist[2] == INF
    assert dist[3] == INF
    assert pred == [-1, 0, -1, -1]
