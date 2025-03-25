"""
Kadane's algorithm.

Greedy/sliding window algorithm for computing maximum subarrays in O(n).
(subarray = contiguous // subsequence = not contiguous)

Grow window while the sum is greater than 0, and start new window when the sum
is smaller.
"""


def kadane_max_sub_array(nums: list[int]) -> tuple[int, int, int]:
    """Return the sum and the start and end indices of the maximum sub-array."""
    max_sum = max(nums)
    # Special case if not stricly positive values.
    if max_sum <= 0:
        idx = nums.index(max_sum)
        return idx, idx + 1, max_sum
    max_sum -= 1

    print(f"{nums = }")
    max_l, max_r = 0, 0
    curr_sum = 0
    l = 0
    for i, x in enumerate(nums):
        new_sum = x + curr_sum
        print(f"{i = }, {x = }")
        print(f"{curr_sum = }")
        if new_sum <= 0:
            new_sum = 0
            l = i + 1
        elif new_sum > max_sum:
            max_l = l
            max_r = i + 1
            max_sum = new_sum
        curr_sum = new_sum

        print(f"{new_sum = }")

    return max_l, max_r, max_sum
