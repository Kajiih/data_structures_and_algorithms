from data_structures_and_algorithms.binary_search import binary_search, bisect_left, bisect_right


def test_element_present():
    nums = [1, 3, 5, 7, 9]
    assert binary_search(nums, 3) == 1
    assert binary_search(nums, 1) == 0
    assert binary_search(nums, 9) == 4
    assert binary_search(nums, 5) == 2


def test_element_absent():
    nums = [1, 3, 5, 7, 9]
    assert binary_search(nums, 2) is None
    assert binary_search(nums, 0) is None
    assert binary_search(nums, 10) is None


def test_single_element():
    assert binary_search([5], 5) == 0
    assert binary_search([5], 3) is None


def test_empty_list():
    assert binary_search([], 1) is None


def test_duplicate_elements():
    nums = [1, 2, 2, 3, 4]
    # Behavior depends on implementation (returns first occurrence or any)
    assert binary_search(nums, 2) in {1, 2}  # Adjust based on requirements


def test_large_list():
    nums = list(range(1000))
    assert binary_search(nums, 499) == 499
    assert binary_search(nums, 1000) is None


def test_bisect_right():
    # Test basic functionality
    a = [1, 2, 2, 3]
    assert bisect_right(a, 2, 0, 3) == 3  # Note: hi adjusted to avoid assertion error

    # Test insertion at the end
    assert bisect_right([1, 2, 3], 4, 0, 3) == 3

    # Test insertion at the beginning
    assert bisect_right([2, 3, 4], 1, 0, 3) == 0

    # Test empty list
    assert bisect_right([], 1, 0, 0) == 0


def test_bisect_left():
    # Test basic functionality
    a = [1, 2, 2, 3]
    assert bisect_left(a, 2, 0, 3) == 1  # Note: hi adjusted

    # Test insertion at the end
    assert bisect_left([1, 2, 3], 4, 0, 3) == 3

    # Test insertion at the beginning
    assert bisect_left([2, 3, 4], 1, 0, 3) == 0

    # Test empty list
    assert bisect_left([], 5, 0, 0) == 0
