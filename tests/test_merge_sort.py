from data_structures_and_algorithms.merge_sort import (
    _merge,
    merge_sort,
)  # Replace with the actual module name


# Tests for _merge function
def test_merge_empty_lists():
    assert _merge([], []) == []


def test_merge_one_empty():
    assert _merge([1, 2, 3], []) == [1, 2, 3]
    assert _merge([], [4, 5]) == [4, 5]


def test_merge_all_l1_smaller():
    assert _merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_merge_all_l2_smaller():
    assert _merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]


def test_merge_interleaved():
    assert _merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_merge_duplicates():
    assert _merge([1, 2, 2, 3], [2, 3, 4]) == [1, 2, 2, 2, 3, 3, 4]


def test_merge_different_lengths():
    assert _merge([1, 3], [2, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert _merge([2, 4, 5], [1, 3]) == [1, 2, 3, 4, 5]


# Tests for merge_sort function
def test_empty_list():
    assert merge_sort([]) == []


def test_single_element():
    assert merge_sort([5]) == [5]


def test_two_elements_sorted():
    assert merge_sort([1, 2]) == [1, 2]


def test_two_elements_unsorted():
    assert merge_sort([2, 1]) == [1, 2]


def test_already_sorted():
    input = [1, 2, 3, 4, 5]
    assert merge_sort(input) == input


def test_reverse_sorted():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_duplicates():
    assert merge_sort([2, 3, 2, 1, 3]) == [1, 2, 2, 3, 3]


def test_all_duplicates():
    assert merge_sort([5, 5, 5, 5]) == [5, 5, 5, 5]


def test_random_order():
    input = [3, 1, 4, 1, 5, 9, 2, 6]
    assert merge_sort(input) == sorted(input)


def test_odd_length():
    input = [3, 1, 4, 1, 5]
    assert merge_sort(input) == [1, 1, 3, 4, 5]


def test_large_list():
    import random

    input = [random.randint(0, 1000) for _ in range(1000)]
    assert merge_sort(input) == sorted(input)


def test_original_list_unchanged():
    input = [3, 2, 1]
    original = input.copy()
    merge_sort(input)
    assert input == original  # Ensure input is not modified
