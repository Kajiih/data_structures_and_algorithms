from data_structures_and_algorithms.kadane import kadane_max_sub_array


def test_all_positive():
    nums = [1, 2, 3]
    assert kadane_max_sub_array(nums) == (0, 3, 6)


def test_all_negative():
    nums = [-3, -1, -2]
    assert kadane_max_sub_array(nums) == (1, 2, -1)


def test_single_element_positive():
    nums = [5]
    assert kadane_max_sub_array(nums) == (0, 1, 5)


def test_single_element_negative():
    nums = [-5]
    assert kadane_max_sub_array(nums) == (0, 1, -5)


def test_max_subarray_in_middle():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert kadane_max_sub_array(nums) == (3, 7, 6)


def test_max_subarray_with_zeros():
    nums = [0, 0, 0, 1, 2, -1, 0]
    assert kadane_max_sub_array(nums) == (3, 5, 3)


def test_max_subarray_starting_at_zero():
    nums = [2, -1, 2]
    assert kadane_max_sub_array(nums) == (0, 3, 3)


def test_max_subarray_at_end():
    nums = [-1, -2, 3]
    assert kadane_max_sub_array(nums) == (2, 3, 3)


def test_all_zeros():
    nums = [0, 0, 0]
    assert kadane_max_sub_array(nums) == (0, 1, 0)


def test_reset_and_new_window():
    nums = [-1, 2, -3, 4]
    assert kadane_max_sub_array(nums) == (3, 4, 4)


def test_increasing_sum_after_decrease():
    nums = [5, -2, -2, 5]
    assert kadane_max_sub_array(nums) == (0, 4, 6)


def test_multiple_possible_max_subarrays():
    nums = [1, -1, 1, -1, 1]
    assert kadane_max_sub_array(nums) == (0, 1, 1)


def test_large_values():
    nums = [10, -20, 30, -40, 50]
    assert kadane_max_sub_array(nums) == (4, 5, 50)


def test_alternating_sequence():
    nums = [3, -2, 3, -2, 3]
    assert kadane_max_sub_array(nums) == (0, 5, 5)
