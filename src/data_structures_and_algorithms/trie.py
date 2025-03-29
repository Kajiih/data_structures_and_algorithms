"""
Prefix Tree/Trie.

Associative table (dictionnaire) useful to store words and retrieving prefixes.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Trie:
    """Prefix Trie."""

    children: dict[str, Trie] = field(default_factory=dict)
    is_word: bool = False

    def add(self, word: str, i: int) -> None:
        """Add the word starting at the index i (word[i:]) to the trie."""
        if i == len(word):
            self.is_word = True
            return

        c = word[i]
        node = self.children.get(c)
        if node is None:
            node = Trie()
        self.children[c] = node

        node.add(word, i + 1)

    def search(self, word: str, i: int) -> bool:
        """Return whether the word starting from the index i belongs to the trie."""
        if i == len(word):
            return self.is_word

        node = self.children.get(word[i])
        if node is None:
            return False
        return node.search(word, i + 1)

    def remove(self, word: str, i: int) -> None:
        """Remove the word starting from index i from the tree."""
        if i == len(word):
            self.is_word = False
            return

        node = self.children[word[i]]

        node.remove(word, i + 1)

    def is_prefix(self, word: str, i: int) -> bool:
        return self.find_node(word, i) is not None

    def find_node(self, word: str, i: int, create_new: bool = False) -> Trie | None:
        """Return the node of the end of the word if it exists."""
        if i == len(word):
            return self

        c = word[i]
        node = self.children.get(c)
        if node is None:
            if not create_new:
                return None
            node = Trie()
            self.children[c] = node
        return node.find_node(word, i + 1, create_new=create_new)
