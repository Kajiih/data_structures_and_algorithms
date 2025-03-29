"""
Binary Search.

Bisect left returns the first index such that the element can be inserted by
preserving the sorted property. All elements before the index are strictly lower,
all elements starting from the index are larger than or equal to the element.
Bisect right: same but return the last index. All element before are smaller or
equal, all elements starting from the index are strictly larger.


Tips:
- always move hi to mid (because if it is the desired position, lo will
    eventually end at the same index than hi)
"""


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


def bisect_right(a: list[int], x: int, lo: int = 0, hi: int | None = None) -> int:
    """
    Return the rightmost insertion point of x in a for a to stay sorted after insertion.

    The returned index idx is the index of the first element strictly greater
    than x (or the length of the list).
    """
    if hi is None:
        hi = len(a)
    assert lo >= 0
    assert hi <= len(a)

    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] > x:
            hi = mid
        else:
            lo = mid + 1
    return lo


def bisect_left(a: list[int], x: int, lo: int = 0, hi: int | None = None) -> int:
    """
    Return the leftmost insertion point of x in a for a to stay sorted after insertion.

    The returned index idx is the index of the first element greater than or
    equal to x (or the length of the list).
    """
    if hi is None:
        hi = len(a)
    assert lo >= 0
    assert hi <= len(a)

    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] >= x:
            hi = mid
        else:
            lo = mid + 1
    return lo
