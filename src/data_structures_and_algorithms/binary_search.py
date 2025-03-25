"""Binary Search."""


def binary_search(nums: list[int], x: int) -> int | None:
    """Return the index of x in the list (that has to be sorted) or None if it is not in the list."""
    start, end = 0, len(nums)

    while start < end:
        m = (start + end) // 2
        if nums[m] == x:
            return m
        if nums[m] < x:
            start = m + 1
        else:
            end = m
    return None
