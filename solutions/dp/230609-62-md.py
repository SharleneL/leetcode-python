class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_arr = [[None for _ in range(m + 1)] for _ in range(n + 1)]
        # dp_arr = [[0]*(m+1)]*(n+1) # this initiation won't work! each row is pointing to the same 1-D array instance.
        for i in range(1, n + 1): # for rows
            for j in range(1, m + 1): # for columns
                self.dp(dp_arr, i, j)

        return dp_arr[n][m]

    def dp(self, dp_arr, i, j):
        if i == 1 and j == 1:
            dp_arr[i][j] = 1
            return
        elif i == 1:
            dp_arr[i][j] = 1
            return
        elif j == 1:
            dp_arr[i][j] = 1
            return

        dp_arr[i][j] = dp_arr[i - 1][j] + dp_arr[i][j - 1]
        return

# test
if __name__ == '__main__':
    res = Solution().uniquePaths(3, 2)
    print(res)