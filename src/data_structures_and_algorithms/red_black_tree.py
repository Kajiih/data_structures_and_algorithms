"""
Red-Black Tree.

A balanced binary search tree where nodes are colored in red or black and all
paths from root to leaf have the same number of black nodes (in the worst case,
the longest paths is at most twice as long as the shortest one).

Binary Search Tree (BST):
- Binary = a node has at most 2 nodes
- Search: left child is lower than the parent and right side is greater
    -> the whole left side is smaller and the whole right side is greater

Red-Black Tree:
- Root and leaves are black
- A red node can only have black children
- All paths from root to leaves have the same amount of black nodes
    -> if a node has only one child, the child must be red (otherwise this rule is violated)

Operations:
- Insertion: O(log(n))
    - 4 rotation rebalance cases on added node Z:
        - Z is root: color black
        - Z's uncle is red: recolor Z's parent, grandparent and uncle and rebalance grandparent
        - Z's uncle is black and node makes a triangle with its parent and grand-parent (left child of a right child or the opposite):
            - Rotate the parent in the opposite direction of Z (e.g. right if it's a left child)
            - Rebalance the former parent (that is now a child of Z)
        - Z's uncle is black and node makes a line with parent and grand-parent (both node and parent are left children or same on right)
            - Rotate the grandparent in the opposite direction of Z (so the parent takes the place of the grand parent) and recolor parent and grandparent (no recursive rebalance)
- Deletion: O(log(n))
    -
- Search: O(log(n))
    - Same as simple BST
- Sorted traversal (left to right): O(n)



Tips:
- Nodes take parent, and key and have grand-parent, sibling, uncle properties
- 2 rotations: left and right
    - left: "exchange with right child" = right child takes place of the node and node become its left child (and exchange children properly)
    - symmetric on the right
- Nodes are red by default (if not root)
- Insert: 4 fix cases
    - define rebalance and recolor_and_rebalance_gp
- Delete:
    - Define transplant
        - Replace node by the rightmost child of the left child (or the right child if the left child doesn't exist)
            - If removed node has only one (or zero) child , this child takes its place. Just change the parent's reference
            - If it has 2 children, chose it like above and pass the new child's right children as left children of its parent,
                then pass the 2 children of the removed node to the new child, and update the parent reference
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator


@dataclass
class BSTNode:
    """Binary Tree node."""

    key: int
    val: int
    is_black: bool = False
    left_child: BSTNode | None = None
    right_child: BSTNode | None = None
    parent: BSTNode | None = None

    @property
    def grandparent(self) -> BSTNode | None:
        """Grand parent of the node."""
        if self.parent is None:
            return None
        return self.parent.parent

    @property
    def sibling(self) -> BSTNode | None:
        """Sibling of the node."""
        if self.parent is None:
            return None
        if self.parent.left_child is not None and self.key == self.parent.left_child.key:
            return self.parent.right_child
        return self.parent.left_child

    @property
    def uncle(self) -> BSTNode | None:
        """Uncle of the node."""
        if self.parent is None:
            return None
        return self.parent.sibling

    @property
    def is_root(self) -> bool:
        """Return whether the node is the root."""
        return self.parent is None

    def is_left_child(self) -> bool:
        """Return whether the node is a left child."""
        assert self.parent is not None

        return self.parent.left_child is not None and self.key == self.parent.left_child.key

    def get_subtree_min_node(self) -> BSTNode:
        """Return the node with minimum key in the subtree."""
        node = self
        while node.left_child is not None:
            node = node.left_child

        return node

    def get_subtree_max_node(self) -> BSTNode:
        """Return the node with maximum key in the subtree."""
        node = self
        while node.right_child is not None:
            node = node.right_child

        return node


class RBTree:
    """Red-Black Tree."""

    def __init__(self) -> None:
        self.root: BSTNode | None = None
        self.size: int = 0

    def insert(self, k: int, val: int) -> None:
        """Insert element."""
        self[k] = val

    def remove(self, k: int) -> None:
        """Remove the element associated with the key."""
        del self[k]

    def search(self, k: int) -> int:
        """Return the value of the element associated with the key."""
        return self[k]

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[int]: ...

    def __getitem__(self, k: int) -> int:
        return self._get_node(k).val

    def __setitem__(self, k: int, val: int) -> None:
        # Set and rotate
        if self.root is None:
            self.root = BSTNode(k, val, is_black=True)
            self.size += 1
            return

        # Find the parent new node
        node_and_parent = self._get_node_or_parent(k)
        if node_and_parent[0] is not None:
            node = node_and_parent[0]
            node.key = val
            return

        # Add the new node
        self.size += 1
        parent = node_and_parent[1]

        new_node = BSTNode(k, val, parent=parent)  # Red by default
        if k < parent.key:
            parent.left_child = new_node
        else:
            parent.right_child = new_node

        # Fix the tree
        self._rebalance(new_node)


    # TODO: Check and update this
    def __delitem__(self, k: int) -> None:
        node = self._get_node(k)
        need_fix = node.is_black
        self.size -= 1

        # Find replacement leaf by going to the left child then iterating on right child until finding a node without right child
        if node.left_child is None:
            new_child = node.right_child
            fixed_node = new_child
        elif node.right_child is None:
            new_child = node.left_child
            fixed_node = new_child
        else:
            new_child = node.left_child.get_subtree_max_node()
            assert new_child.parent

            # Transplant new_child's left child
            if new_child.left_child is not None:
                self._update_parent(
                    new_child.left_child, new_child.parent, replaced_child=new_child
                )
            else:
                new_child.parent.right_child = None
            # Transplant removed node's children
            new_child.left_child = node.left_child
            new_child.left_child.parent = new_child
            new_child.right_child = node.right_child
            new_child.right_child.parent = new_child

            fixed_node = None  # It is the left child of new_node

        # At this point the removed nodes has no more children, they have been transplanted to the new child, or are the new child itself

        # Transplant new child where the removed node was
        if new_child is None:
            # Last node of the tree
            if node.parent is None:
                self.root = None
                return
            if node.is_left_child():
                node.parent.left_child = None
            else:
                node.parent.left_child = None
        else:
            self._update_parent(new_child, node.parent, node)

        # Fixup
        if need_fix:
            ...

    def _get_node(self, k: int) -> BSTNode:
        node = self.root
        while node is not None:
            if node.key == k:
                return node
            node = node.left_child if k < node.key else node.right_child

        raise KeyError(k)

    def _get_node_or_parent(self, k: int) -> tuple[BSTNode, None] | tuple[None, BSTNode]:
        assert self.root is not None

        node = self.root
        # Find the parent new node
        parent = node
        while node is not None:
            if k == node.key:
                return node, None
            parent = node
            node = node.left_child if k < node.key else node.right_child

        return None, parent

    def _rotate_left(self, node: BSTNode) -> None:
        assert node.right_child is not None
        new_parent = node.right_child

        # Update parents
        self._update_parent(new_parent, node.parent, replaced_child=node)
        self._update_parent(node, new_parent)
        # Move children
        node.right_child = new_parent.left_child
        new_parent.left_child = node

    def _rotate_right(self, node: BSTNode) -> None:
        assert node.left_child is not None
        new_parent = node.left_child

        # Update parents
        self._update_parent(new_parent, node.parent, replaced_child=node)
        self._update_parent(node, new_parent)
        # Move children
        node.left_child = new_parent.right_child
        new_parent.right_child = node

    def _update_parent(
        self, node: BSTNode, parent: BSTNode | None, replaced_child: BSTNode | None = None
    ) -> None:
        """
        Update the parent and root reference if necessary.

        If replaced_child is given, the parent's reference to its child will
        also be updated.
        """
        assert replaced_child is None or replaced_child.parent == parent

        if parent is None:
            self.root = node
        node.parent = parent

        # Update parent's child reference
        if replaced_child is not None and parent is not None:
            if replaced_child.is_left_child():
                parent.left_child = node
            else:
                parent.right_child = node

    def _rebalance(self, node: BSTNode) -> None:
        # Case 1: root
        if node.parent is None:
            node.is_black = True
            return

        # Case 0: no rebalance
        if node.parent.is_black:
            return

        assert node.grandparent is not None
        # It is necessarily true in a correct RB tree because
        # - parent is not the root because it's red, and thus grandparent exist
        # - grandparent is black because one of its child is red, and thus it
        #   cannot have only one child

        # Case 2: red uncle
        if node.uncle is not None and not node.uncle.is_black:
            self._recolor_and_rebalance_gp(node)
        # At this point, the uncle is black or None
        # Case 3: black uncle and triangle
        elif (is_left_side := node.is_left_child()) != node.parent.is_left_child():
            # Always rotate on the opposite side of the node
            parent = node.parent
            if is_left_side:
                self._rotate_right(node.parent)
            else:
                self._rotate_left(node.parent)
            self._rebalance(parent)
        # Case 4: black uncle and line
        else:
            node.parent.is_black = True
            node.grandparent.is_black = False
            if is_left_side:
                self._rotate_right(node.grandparent)
            else:
                self._rotate_left(node.grandparent)

    def _recolor_and_rebalance_gp(self, node: BSTNode) -> None:
        assert node.parent
        assert node.uncle
        assert node.grandparent

        node.parent.is_black = True
        node.uncle.is_black = True
        if not node.grandparent.is_root:
            node.grandparent.is_black = False
            self._rebalance(node.grandparent)

    def _delete_fixup(self, x: BSTNode) -> None:
        """Fixup after deletion."""
