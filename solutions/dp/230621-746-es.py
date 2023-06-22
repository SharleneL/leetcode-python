from typing import List



# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         return min(self.cost(0, n, cost), self.cost(1, n, cost))
#
#     def cost(self, i: int, n: int, cost: List[int]) -> int:
#         if (i>=n-2): return cost[i]
#
#         return cost[i] + min(self.cost(i + 1, n, cost), self.cost(i + 2, n, cost))
# above solution time limit reached. => create a structure to save the middle result

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        min_cost = [None] * len(cost)
        return min(self.cost(0, n, cost, min_cost), self.cost(1, n, cost, min_cost))

    def cost(self, i: int, n: int, cost: List[int], min_cost: List[int]) -> int:
        if (min_cost[i] != None): return min_cost[i]
        if (i>=n-2): return cost[i]

        min_cost[i] = cost[i] + min(self.cost(i + 1, n, cost, min_cost), self.cost(i + 2, n, cost, min_cost))
        return min_cost[i]


# test
if __name__ == '__main__':
    res = Solution().minCostClimbingStairs([10,15,20])
    print(res)
