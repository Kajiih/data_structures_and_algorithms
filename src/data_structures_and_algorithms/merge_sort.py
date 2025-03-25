"""
Merge sort.

Recursively cut in two and merge.

Tips:
- Base case for len <= 1
- Define merge(list1, list2)
"""


def merge_sort(elems: list[int]) -> list[int]:
    """Return a sorted copy of the list."""
    n = len(elems)
    if n <= 1:
        return elems
    mid = n // 2
    return _merge(merge_sort(elems[0:mid]), merge_sort(elems[mid:]))


def _merge(l1: list[int], l2: list[int]) -> list[int]:
    i1, i2 = 0, 0
    n = len(l1)
    m = len(l2)
    res = []
    while i1 < n and i2 < m:
        if l1[i1] <= l2[i2]:
            res.append(l1[i1])
            i1 += 1
        else:
            res.append(l2[i2])
            i2 += 1

    res += l1[i1:]
    res += l2[i2:]
    return res


# This is useless
def merge_sort_inplace(elems: list[int]) -> None:
    """Return a sorted copy of the list."""

    def merge(L: int, M: int, R: int) -> None:
        i1, i2 = L, M
        res = []
        while i1 < M and i2 < R:
            if elems[i1] <= elems[i2]:
                res.append(elems[i1])
                i1 += 1
            else:
                res.append(elems[i2])
                i2 += 1

        res += elems[i1:M]
        res += elems[i2:R]

        elems[L:R] = res

    def sort_between(L: int, R: int) -> None:
        if R - L <= 1:
            return
        M = (L + R) // 2

        sort_between(L, M)
        sort_between(M, R)
        merge(L, M, R)

    sort_between(0, len(elems))
