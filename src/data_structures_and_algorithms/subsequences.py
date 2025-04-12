"""
Generate all unique (non-empty) subsequences of a sequence (sous-suite/suite extraite).

Example:
[1,2,3] -> [[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
[2,1,2] -> [[2],[2,1],[2,1,2],[2,2],[1],[1,2]]


NB:
- Generating subsequences is the same as generating subsets if we keep the order of the element. Just remove the empty set after


Tips:
- use set of tuple

Complexity:
O(2^n)

"""


def subsequences(nums: list[int]) -> set[tuple[int, ...]]:
    """Generate all unique subsequences of nums."""
    n = len(nums)
    res: set[tuple[int, ...]] = set()

    curr = []

    def backtrack(i: int) -> None:
        if i == n:
            res.add(tuple(curr))
            return

        # Subsequences with nums[i]
        curr.append(nums[i])
        backtrack(i + 1)
        curr.pop()

        # Subsequences without nums[i]
        backtrack(i + 1)

    backtrack(0)
    res.remove(())  # We need to remove () because it is added

    return res


print(subsequences([1, 2, 3]))

# TODO: Add counting distinct subsequences without generating them all
