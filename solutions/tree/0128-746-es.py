from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost or len(cost) == 1:
            return 0

        length = len(cost)
        dp = [0] * length
        dp[0] = 0
        dp[1] = 0
        for i in range(2, length):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[length - 1]

if __name__ == '__main__':
    res = Solution().minCostClimbingStairs([0,0,1,1])
    print(res)