"""Merge sort."""


def merge_sort(elems: list[int]) -> list[int]:
    """Sort the list."""
    n = len(elems)
    if n <= 1:
        return elems
    mid = n // 2
    return _merge(merge_sort(elems[0 : mid]), merge_sort(elems[mid:]))


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
