"""
Quicksort implementation.

Inplace sort.

Select pivot (last elem or random + move to last) and move larger elem to the
right of it and continue recursively on both sub-arrays.
Stop when single elem.

Tips:
- Edge case when pivot - 1 == i
    - Don't triple assign but first swap i and pivot - 1 then swap pivot and pivot - 1
- Only increment i when not swapping//decreasing pivot when swapping

"""


def quick_sort(elems: list[int]) -> None:
    """Sort the list."""

    def quick_sort_between(start: int, end: int) -> None:
        """Inplace sort between i included and j excluded."""
        if end - start <= 1:
            return
        pivot = end - 1

        i = start
        while i < pivot:
            if elems[i] > elems[pivot]:
                elems[pivot - 1], elems[i] = elems[i], elems[pivot - 1]
                elems[pivot - 1], elems[pivot] = elems[pivot], elems[pivot - 1]
                pivot -= 1
            else:
                i += 1

        quick_sort_between(start, pivot)
        quick_sort_between(pivot + 1, end)

    quick_sort_between(0, len(elems))
