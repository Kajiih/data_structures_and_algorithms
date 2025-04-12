"""
Generate all subsets of a list of item with or without repetitions (distinct subsets if there are repetitions).

Without repetitions:
[1,2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


With repetitions:
[1,2,2] -> [[],[1],[1,2],[1,2,2],[2],[2,2]]


Tips:
- If repetitions: count and process with unique values

Complexity:
- O(2^n) for without rep
- O(m^n) for with rep where n is the nb of unique integer and m the maximum repetition of any integer
"""

from collections import Counter


def subsets(nums: set[int]) -> list[list[int]]:
    """Generate subsets of a set of integers (without repetitions)."""
    res = [[]]
    for x in nums:
        res += [[*subset, x] for subset in res]

    return res


def subsets_with_rep(nums: list[int]) -> list[list[int]]:
    """Generate subsets of a list of integers (with repetitions)."""
    res = [[]]
    counts = Counter(nums)
    for x, count in counts.items():
        res += [subset + [x] * k for k in range(1, count + 1) for subset in res]

    return res


print(subsets({1, 2, 3}))
print(subsets_with_rep([1, 2, 2]))
