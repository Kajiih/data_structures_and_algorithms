import pytest

from data_structures_and_algorithms.queue import Queue


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def queue_with_elements():
    return Queue(elems=[1, 2, 3])


def test_constructor_empty():
    q = Queue()
    assert len(q) == 0
    assert not q.end 
    assert not q.beginning


def test_constructor_with_elements():
    q = Queue(elems=[1, 2, 3])
    assert len(q) == 3
    # Verify elements are in correct order for FIFO
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3


def test_constructor_with_empty_list():
    q = Queue(elems=[])
    assert len(q) == 0
    with pytest.raises(IndexError):
        q.pop()


def test_push_pop_basic(empty_queue):
    empty_queue.push(1)
    empty_queue.push(2)
    assert empty_queue.pop() == 1
    assert empty_queue.pop() == 2


def test_interleaved_push_pop(queue_with_elements):
    q = queue_with_elements
    q.push(4)
    assert q.pop() == 1
    q.push(5)
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5


def test_len_method():
    q = Queue(elems=[1, 2])
    assert len(q) == 2
    q.pop()
    assert len(q) == 1
    q.push(3)
    assert len(q) == 2


def test_pop_from_empty_queue(empty_queue):
    with pytest.raises(IndexError):
        empty_queue.pop()


def test_push_after_constructor(queue_with_elements):
    q = queue_with_elements
    q.push(4)
    assert len(q) == 4
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4


def test_pop_transfers_end_to_beginning(empty_queue):
    empty_queue.push(1)
    empty_queue.push(2)
    assert empty_queue.pop() == 1  # Transfers from end to beginning
    assert empty_queue.beginning == [2]
    assert not empty_queue.end
