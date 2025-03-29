import pytest
from data_structures_and_algorithms.trie import Trie


@pytest.fixture
def sample_trie():
    trie = Trie()
    words = ["apple", "app", "banana", "band"]
    for word in words:
        trie.add(word, 0)
    return trie


def test_add_and_search(sample_trie):
    assert sample_trie.search("apple", 0) is True
    assert sample_trie.search("app", 0) is True
    assert sample_trie.search("banana", 0) is True
    assert sample_trie.search("band", 0) is True


def test_search_non_existing_word(sample_trie):
    assert sample_trie.search("bana", 0) is False
    assert sample_trie.search("appl", 0) is False


def test_is_prefix(sample_trie):
    assert sample_trie.is_prefix("app", 0) is True
    assert sample_trie.is_prefix("ban", 0) is True
    assert sample_trie.is_prefix("ana", 0) is False


def test_remove_word(sample_trie):
    sample_trie.remove("app", 0)
    assert sample_trie.search("app", 0) is False
    assert sample_trie.is_prefix("app", 0) is True  # Nodes still exist


def test_remove_non_existing_word(sample_trie):
    with pytest.raises(KeyError):
        sample_trie.remove("xyz", 0)


def test_empty_string():
    trie = Trie()
    trie.add("", 0)
    assert trie.search("", 0) is True
    trie.remove("", 0)
    assert trie.search("", 0) is False


def test_case_sensitivity(sample_trie):
    assert sample_trie.search("Apple", 0) is False
    assert sample_trie.is_prefix("App", 0) is False


def test_find_node_existing(sample_trie):
    node = sample_trie.find_node("app", 0)
    assert node is not None
    assert node.is_word is True  # "app" is a word in the sample trie


def test_find_node_non_existing(sample_trie):
    assert sample_trie.find_node("xyz", 0) is None


def test_find_node_create_new():
    trie = Trie()
    node = trie.find_node("test", 0, create_new=True)
    assert node is not None
    assert trie.children["t"].children["e"].children["s"].children["t"] is node
