"""
Matrix Chain Multiplication (MCM).

Computing the minimum number of operations required to multiply a chain of matrix.

Matrices dimensions are given in an array arr such that matrix i (1-indexed) has dimension arr[i-1] x arr[i].

It's a type of DP problem.

Remainder:
- Multiplying a matrix (n x k) by a matrix (k x m) gives a matrix of dim (n x m)
- The cost of multiplying (n x k) and (k x m) is n * k * m (k operations for each of the n * m values in the final matrix)


Tips:
- Think of multiplying along/popping one dimension (common size between 2 adjacent matrices) instead of directly matrices (because matrices will change when multiplied with adjacent matrices, but dimensions will stay until popped)
- given a range i, j between which we want to compute MCM, poppable dimensions are range from i + 1 to j - 1
- recurrence relation:
    - MCM(i, i + 1) = 0
    - MCM(i, j) = min(MCM(i, k) + MCM(k, j) + arr[i] * arr[k] * arr[j] for k in range(i + 1, j))
- recursive solution is easier
- for dp start with difference than i + d = j

"""


def MCM_DP(arr: list[int]) -> int:
    """Dynamically compute the minimum number of operations to multiply matrices with dimensions in arr."""
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    # dp[i][j] = MCM for indices between i and j included

    for d in range(2, n):  # j = i + d >= i + 2 and i + d <= n - 1; d <= n - 1 - i
        for i in range(n - d):  # i + d <= n - 1 -> i <= n - 1 - d -> i < n - d
            j = i + d
            dp[i][j] = min(dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j] for k in range(i + 1, j))
    return dp[0][n - 1]


def MCM_recursive(arr: list[int]) -> int:
    """Recursively compute the minimum number of operations to multiply matrices with dimensions in arr."""
    n = len(arr)

    cache = {}

    def dfs(i: int, j: int) -> int:
        if j <= i + 1:
            return 0
        res = cache.get((i, j))
        if res is not None:
            return res

        res = min(dfs(i, k) + dfs(k, j) + arr[i] * arr[k] * arr[j] for k in range(i + 1, j))

        cache[i, j] = res
        return res

    return dfs(0, n - 1)


def check(arr: list[int], val: int) -> None:
    res1 = MCM_DP(arr)
    res2 = MCM_recursive(arr)
    print("DP:", res1)
    print("Rec:", res2)
    assert res1 == res2 == val


MCM = MCM_recursive

check([10, 30, 5, 60], 4500)
check([30, 5, 60, 10], 4500)
check([5, 60, 10, 30], 4500)
check([60, 10, 30, 5], 4500)
check([1, 4, 3, 2], 18)
check([10, 15, 20, 25], 8000)
check([4, 5, 3, 2], 70)
check([5, 3, 2, 4], 70)
check([3, 2, 4, 5], 70)
check([2, 4, 5, 3], 70)
