"""
LRU cache implementation with a hash map and a linked list.

Tips:
- liked list with values and hash map from key to nodes
- Remember to update nodes_map and size
- Edge case when the moved node is lru or mru
"""

from __future__ import annotations


class Node:
    """Node of a linked list."""

    def __init__(self, data: int, key: str) -> None:
        self.data: int = data
        self.key: str = key
        self.prev: Node | None = None  # Less recently used
        self.next: Node | None = None  # More recently used


class LRUCache:
    """LRU Cache implementation with a linked list and hash map."""

    def __init__(self, capacity: int = 5) -> None:
        assert capacity > 2
        self.capacity: int = capacity
        self.lru: Node | None = None
        self.mru: Node | None = None
        self.nodes_map: dict[str, Node] = {}
        self.size: int = 0

    def get(self, key: str) -> int | None:
        """Return the values corresponding to the id."""
        # Check if inside
        node = self.nodes_map.get(key)
        if node is None:
            return None

        self._move_to_tail(node)

        return node.data

    def set(self, key: str, val: int) -> None:
        """Set the value of the id in the cache."""
        # get+modify/create node
        node = self.nodes_map.get(key)
        if node is None:
            node = Node(val, key)
            self.nodes_map[key] = node
            # move to tail
            if self.mru is None:
                self.mru = self.lru = node
            else:
                self.mru.next = node
                node.prev = self.mru
                self.mru = node
            self.size += 1
        else:
            node.data = val
            # move to tail
            self._move_to_tail(node)

        # potentially remove head (and del from map)
        if self.size <= self.capacity:
            return
        assert self.lru is not None
        assert self.lru.next is not None

        self.lru.next.prev = None
        del self.nodes_map[self.lru.key]
        self.lru = self.lru.next
        self.size -= 1

    def _move_to_tail(self, node: Node) -> None:
        assert self.mru is not None
        # Remove node
        prev_node = node.prev
        next_node = node.next
        if next_node is None:
            # Already most recently used
            return
        next_node.prev = prev_node
        if prev_node is None:
            # It's the lru
            self.lru = next_node
        else:
            prev_node.next = next_node

        # Move node to tail
        self.mru.next = node
        node.prev = self.mru
        self.mru = node
