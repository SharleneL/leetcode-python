from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])  # total cols
        n = len(grid)  # total rows

        minSum = [[None for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.dp(minSum, grid, i, j)

        return minSum[n][m]

    def dp(self, minSum, grid, i, j) -> int:
        if i == 1 and j == 1:
            minSum[i][j] = grid[i-1][j-1]
            return
        elif i == 1:
            minSum[i][j] = grid[i-1][j-1] + minSum[i][j - 1]
            return
        elif j == 1:
            minSum[i][j] = grid[i-1][j-1] + minSum[i - 1][j]
            return

        minSum[i][j] = min(minSum[i-1][j], minSum[i][j-1]) + grid[i-1][j-1]
        return


# Solution 2 - same
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         minPath = [[None for _ in range(cols)] for _ in range(rows)]
#
#         for i in range(rows):
#             for j in range(cols):
#                 if i == 0 and j == 0:
#                     minPath[i][j] = grid[i][j]
#                 elif i == 0:
#                     minPath[i][j] = minPath[i][j - 1] + grid[i][j]
#                 elif j == 0:
#                     minPath[i][j] = minPath[i - 1][j] + grid[i][j]
#                 else:
#                     minPath[i][j] = min(minPath[i][j - 1], minPath[i - 1][j]) + grid[i][j]
#
#         return minPath[rows - 1][cols - 1]


"""
m rows, n cols

can cur step be inferred from prev results? yes
minPath[i][j] = min(minPath[i-1][j], minPath[i][j-1]) + grid[i][j]

if i==0


# test
if __name__ == '__main__':
    grid = [
            [1,3,1],
            [1,5,1],
            [4,2,1]
    ]
    res = Solution().minPathSum(grid)
    print(res)

"""
m col, n rows.
Thus (m+1) in each row. (n+1) rows.
Return value: arr[n][m] "第n行第m列"

each elem: >= 0
output: min sum of path values

1. define dp arr
    dp[i, j]: min sum reaching [i, j]

2. find inferring formula
    dp[i, j] = min(dp[i-1, j], dp[i, j-1]) + grid[i, j]
    i>=1; j>=1
    if i == 1: calc for first row. dp[i, j] = grid[i, j] + dp[i, j-1]
    if j == 1: calc for first col. dp[i, j] = grid[i, j] + dp[i-1, j]
    if i ==1 && j==1: dp[i,j] = grid[i][j]

3. init value
    see above


------------------
pseudo code

# fill in minSum[i][j]
func dp(minSum, grid, i, j):
    if(i==1 && j==1):
        ...
    elif: ...
    elif: ...

    dp[][] = ...
    return
"""