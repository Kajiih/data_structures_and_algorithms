from heapq import heapify, heappop, heappush

import pytest

from data_structures_and_algorithms.binary_heap import MinHeap


@pytest.fixture
def empty_heap():
    return MinHeap()


def test_initialization(empty_heap):
    assert len(empty_heap.arr) == 0


def test_push_single_element(empty_heap):
    empty_heap.push(5)
    assert len(empty_heap.arr) == 1
    assert empty_heap.arr[0] == 5


def test_pop_single_element(empty_heap):
    empty_heap.push(5)
    val = empty_heap.pop()
    assert val == 5
    assert len(empty_heap.arr) == 0


def test_push_pop_multiple_elements():
    heap = MinHeap()
    elements = [3, 1, 2, 5, 4]
    for el in elements:
        heap.push(el)
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert heap.pop() == 3
    assert heap.pop() == 4
    assert heap.pop() == 5


def test_heap_property_after_push():
    heap = MinHeap()
    elements = [4, 2, 6, 1, 3, 5]
    for el in elements:
        heap.push(el)
        assert _is_min_heap(heap.arr)


def test_heap_property_after_pop():
    heap = MinHeap()
    elements = [4, 2, 6, 1, 3, 5]
    for el in elements:
        heap.push(el)
    for _ in elements:
        heap.pop()
        assert _is_min_heap(heap.arr)


@pytest.mark.parametrize(
    "test_input",
    [
        [1],
        [3, 1, 2],
        [5, 3, 8, 1, 2],
        [2, 2, 2],
        [5, 4, 3, 2, 1],
    ],
)
def test_against_stdlib_heapq(test_input):
    custom_heap = MinHeap()
    std_heap = []
    for num in test_input:
        heappush(std_heap, num)
        custom_heap.push(num)
    while std_heap:
        std_val = heappop(std_heap)
        custom_val = custom_heap.pop()
        assert custom_val == std_val


def _is_min_heap(arr):
    for i in range(len(arr)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(arr) and arr[i] > arr[left]:
            return False
        if right < len(arr) and arr[i] > arr[right]:
            return False
    return True


@pytest.fixture(
    params=[
        # (input_array, expected_heapified_array)
        ([], []),  # Empty array
        ([5], [5]),  # Single element
        ([1, 2, 3, 4], [1, 2, 3, 4]),  # Already a valid min-heap
        ([4, 3, 2, 1], [1, 3, 2, 4]),  # Reverse-sorted array
        ([3, 2, 1, 2, 4], [1, 2, 3, 2, 4]),  # Unsorted with duplicates
        ([5, 4, 3, 2, 1], [1, 2, 3, 5, 4]),  # Larger reverse-sorted
        ([2, 2, 2], [2, 2, 2]),  # All elements equal
        ([9, 3, 7, 1, 5], [1, 3, 7, 9, 5]),  # Complex unsorted case
    ]
)
def heap_test_case(request):
    return request.param


def test_heapify_from_existing_array(heap_test_case):
    input_arr, expected_arr = heap_test_case
    heap = MinHeap(input_arr)
    # Verify the heapified array matches the expected structure
    assert heap.arr == expected_arr
    # Ensure the heap property is maintained
    assert _is_min_heap(heap.arr)


def test_heapify_against_stdlib(heap_test_case):
    input_arr, _ = heap_test_case
    if not input_arr:
        return  # Skip empty case for heapq
    # Compare with Python's heapq
    std_heap = input_arr.copy()
    heapify(std_heap)
    custom_heap = MinHeap(input_arr)
    # Ensure both produce the same minimum element sequence
    while std_heap:
        std_min = std_heap[0]
        custom_min = custom_heap.pop()
        assert custom_min == std_min
        # Re-heapify std_heap after "pop" (for demonstration)
        std_heap[0] = std_heap[-1]
        std_heap.pop()
        if std_heap:
            heapify(std_heap)
