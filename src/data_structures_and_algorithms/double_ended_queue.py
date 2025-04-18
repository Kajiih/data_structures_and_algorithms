"""
Double-ended queue implementation with doubly linked list.

FIFO
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


class LinkedNode:  # noqa: B903
    """A node for a doubly linked list."""

    def __init__(
        self, val: int, left: LinkedNode | None = None, right: LinkedNode | None = None
    ) -> None:
        self.val: int = val
        self.left: LinkedNode | None = left
        self.right: LinkedNode | None = right


class DQueue:
    """Double Ended Queue."""

    def __init__(self, elems: Sequence[int] | None = None) -> None:
        self.left_node: LinkedNode | None = None
        self.right_node: LinkedNode | None = None
        self.size: int = 0
        for x in elems or []:
            self.push_right(x)

    def __len__(self) -> int:
        return self.size

    def __bool__(self) -> bool:
        return bool(self.size)

    def push_left(self, x: int) -> None:
        """Push x to the left of the queue."""
        node = LinkedNode(x, right=self.left_node)
        if self.left_node is None:
            self.right_node = self.left_node = node
        else:
            self.left_node.left = node
            self.left_node = node
        self.size += 1

    def push_right(self, x: int) -> None:
        """Push x to the right of the queue."""
        node = LinkedNode(x, left=self.right_node)
        if self.right_node is None:
            self.right_node = self.left_node = node
        else:
            self.right_node.right = node
            self.right_node = node
        self.size += 1

    def pop_left(self) -> int:
        """Pop the leftmost element."""
        node = self.left_node
        assert node
        if not node.right:
            self.left_node = self.right_node = None
        else:
            node.right.left = None
            self.left_node = node.right

        self.size -= 1
        return node.val

    def pop_right(self) -> int:
        """Pop the rightmost element."""
        node = self.right_node
        assert node
        if not node.left:
            self.left_node = self.right_node = None
        else:
            node.left.right = None
            self.right_node = node.left

        self.size -= 1
        return node.val
