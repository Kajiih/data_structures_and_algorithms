from data_structures_and_algorithms.disjoint_set import DisjointSet


def test_initialization():
    """Test that each element is its own representative initially."""
    n = 10
    dsu = DisjointSet(n)
    for i in range(n):
        assert dsu.find(i) == i, f"Element {i} should be its own representative."


def test_union_and_find():
    """Test that union properly merges two sets."""
    dsu = DisjointSet(5)
    dsu.union(0, 1)
    dsu.union(2, 3)
    # After union, 0 and 1 should have the same representative.
    assert dsu.find(0) == dsu.find(1), "0 and 1 should be in the same set."
    # Similarly for 2 and 3.
    assert dsu.find(2) == dsu.find(3), "2 and 3 should be in the same set."
    # Merging two sets: union (1,2) should merge sets {0,1} and {2,3}.
    dsu.union(1, 2)
    rep = dsu.find(0)
    for i in [1, 2, 3]:
        assert dsu.find(i) == rep, f"Element {i} should be in the same set as 0."


def test_redundant_union():
    """Test that union on already unified elements does not alter the DSU state."""
    dsu = DisjointSet(5)
    dsu.union(0, 1)
    initial_rep = dsu.find(0)
    # Performing the union again should change nothing.
    dsu.union(0, 1)
    assert dsu.find(0) == initial_rep, "Redundant union should not change the representative."


def test_chain_union():
    """Test union operations that merge a chain of elements into one component."""
    dsu = DisjointSet(10)
    # Create a chain: 0-1, 1-2, 2-3, ..., 8-9.
    for i in range(1, 10):
        dsu.union(i - 1, i)
    rep = dsu.find(0)
    for i in range(10):
        assert dsu.find(i) == rep, (
            f"Element {i} should have the same representative after chain unions."
        )


def test_connected_components():
    """Test that the DSU can correctly determine the number of connected components."""
    # Create 5 elements with two separate groups:
    # Group 1: {0, 1, 2}, Group 2: {3, 4}
    dsu = DisjointSet(5)
    dsu.union(0, 1)
    dsu.union(1, 2)
    dsu.union(3, 4)
    component_reps = {dsu.find(i) for i in range(5)}
    assert len(component_reps) == 2, "There should be exactly two connected components."


def test_union_with_itself():
    """Test that unioning an element with itself does not change the DSU state."""
    dsu = DisjointSet(5)
    parent_before = dsu.parent.copy()
    dsu.union(0, 0)
    assert dsu.parent == parent_before, "Union of an element with itself should not alter the DSU."
