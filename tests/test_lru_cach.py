import pytest

from data_structures_and_algorithms.lru_cache import (  # Replace with actual module name
    LRUCache,
    Node,
)


def test_basic_operations():
    """Test basic set and get functionality."""
    cache = LRUCache(3)
    cache.set("A", 1)
    assert cache.get("A") == 1
    assert cache.size == 1
    assert cache.lru is cache.mru
    assert cache.lru
    assert cache.lru.key == "A"


def test_eviction_when_exceeding_capacity():
    """Test LRU eviction when capacity is exceeded."""
    cache = LRUCache(3)
    cache.set("A", 1)
    cache.set("B", 2)
    cache.set("C", 3)
    cache.set("D", 4)

    # Verify evictions and state
    assert cache.get("A") is None
    assert cache.get("B") == 2
    assert cache.get("C") == 3
    assert cache.get("D") == 4
    assert cache.size == 3


def test_get_updates_mru():
    """Test that get operations promote nodes to MRU."""
    cache = LRUCache(3)
    cache.set("A", 1)
    cache.set("B", 2)
    cache.set("C", 3)

    # Access A to make it MRU
    cache.get("A")

    # Add new element to trigger eviction
    cache.set("D", 4)

    # Verify state after eviction
    assert cache.get("B") is None  # B should be evicted
    assert cache.get("A") == 1
    assert cache.get("C") == 3
    assert cache.get("D") == 4


def test_update_existing_key():
    """Test updating existing values and MRU promotion."""
    cache = LRUCache(3)
    cache.set("A", 1)
    cache.set("B", 2)
    cache.set("C", 3)

    # Update B and verify promotion
    cache.set("B", 200)
    assert cache.get("B") == 200

    # Add new element
    cache.set("D", 4)

    # Verify eviction order
    assert cache.get("A") is None
    assert cache.get("B") == 200
    assert cache.get("C") == 3
    assert cache.get("D") == 4


def test_internal_links_after_operations():
    """Verify linked list integrity after operations."""
    cache = LRUCache(3)
    cache.set("A", 1)
    cache.set("B", 2)
    cache.set("C", 3)

    # Initial link check
    assert cache.lru
    assert cache.mru
    assert cache.lru.next
    assert cache.mru.prev
    assert cache.lru.key == "A"
    assert cache.lru.next.key == "B"
    assert cache.mru.prev.key == "B"

    # Promote A to MRU
    cache.get("A")

    # Verify new links
    assert cache.lru.key == "B"
    assert cache.lru.next.key == "C"
    assert cache.mru.key == "A"
    assert cache.mru.prev.key == "C"




def test_consecutive_evictions():
    """Test multiple consecutive insertions beyond capacity."""
    cache = LRUCache(3)
    cache.set("A", 1)
    cache.set("B", 2)
    cache.set("C", 3)
    cache.set("D", 4)  # Evict A
    cache.set("E", 5)  # Evict B

    # Verify cache state
    assert "A" not in cache.nodes_map
    assert "B" not in cache.nodes_map
    assert len(cache.nodes_map) == 3  # C, D, E
    assert cache.size == 3


def test_node_promotion_logic():
    """Test _move_to_tail method directly."""
    cache = LRUCache(3)
    node_b = Node(2, "B")

    # Test with empty cache
    cache.mru = node_b
    cache.lru = node_b
    cache.size = 1

    # Promote existing node
    cache._move_to_tail(node_b)
    assert cache.mru == node_b
    assert cache.lru == node_b


if __name__ == "__main__":
    pytest.main([__file__])
