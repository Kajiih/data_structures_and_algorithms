import pytest

from data_structures_and_algorithms.double_ended_queue import DQueue


@pytest.fixture
def empty_deque():
    return DQueue()


@pytest.fixture
def single_element_deque():
    return DQueue(elems=[1])


@pytest.fixture
def deque_with_elements():
    return DQueue(elems=[3, 1, 2])  # Structure: 3 <-> 1 <-> 2


def test_constructor_empty():
    dq = DQueue()
    assert len(dq) == 0
    assert dq.left_node is None
    assert dq.right_node is None


def test_constructor_with_empty_list():
    dq = DQueue(elems=[])
    assert len(dq) == 0
    assert not dq


def test_constructor_with_single_element():
    dq = DQueue(elems=[5])
    assert len(dq) == 1
    assert dq.left_node is dq.right_node
    assert dq.pop_left() == 5
    assert len(dq) == 0


def test_constructor_with_multiple_elements():
    dq = DQueue(elems=[1, 2, 3])
    assert len(dq) == 3
    assert dq.pop_left() == 1
    assert dq.pop_left() == 2
    assert dq.pop_left() == 3
    assert len(dq) == 0


def test_constructor_internal_links():
    dq = DQueue(elems=[1, 2, 3])
    left = dq.left_node
    assert left
    assert left.val == 1
    middle = left.right
    assert middle
    assert middle.val == 2
    right = middle.right
    assert right
    assert right.val == 3
    assert right.right is None
    # Check reverse links
    assert right.left == middle
    assert middle.left == left


def test_constructor_push_right_order():
    dq = DQueue(elems=[1, 2, 3])
    assert dq.pop_right() == 3
    assert dq.pop_right() == 2
    assert dq.pop_right() == 1


def test_constructor_and_additional_operations():
    dq = DQueue(elems=[1, 2])
    dq.push_left(0)
    dq.push_right(3)
    assert len(dq) == 4
    assert dq.pop_left() == 0
    assert dq.pop_right() == 3
    assert dq.pop_left() == 1
    assert dq.pop_right() == 2


# Existing tests (revised to use fixtures where applicable)
def test_pop_empty_deque(empty_deque):
    with pytest.raises(AssertionError):
        empty_deque.pop_left()
    with pytest.raises(AssertionError):
        empty_deque.pop_right()


def test_size_after_construction(deque_with_elements):
    assert len(deque_with_elements) == 3


def test_bool_after_construction(single_element_deque):
    assert single_element_deque
    single_element_deque.pop_left()
    assert not single_element_deque


def test_internal_links_after_construction(deque_with_elements):
    left = deque_with_elements.left_node
    assert left.val == 3
    middle = left.right
    assert middle.val == 1
    right = middle.right
    assert right.val == 2
    assert right.left == middle
    assert middle.left == left
    assert left.left is None
    assert right.right is None
