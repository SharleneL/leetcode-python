from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[None for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue

                if i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[rows - 1][cols - 1]


"""
dp[0][0] = 1
if i==0:
    if obstacleGrid[i][j] == 0:
        dp[i][j] = 0
    else:
        dp[i][j] = dp[i][j-1]
if j==0:
    if obstacleGrid[i][j] == 0:
        dp[i][j] = 0
    else:
        dp[i][j] = dp[i-1][j]
else:
    if obstacleGrid[i][j] == 0:
        dp[i][j] = 0
    else:
        dp[i][j] = dp[i-1][j] + dp[j-1][i]
"""
# test
if __name__ == '__main__':
    res = Solution().uniquePathsWithObstacles([[0,1],[0,0]])
    print(res)