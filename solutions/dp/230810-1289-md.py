from typing import List

import sys


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]

        # n>=2
        min_path_sum = [None for _ in range(n)]
        last_min_path_sum = [None for _ in range(n)]
        for row in range(n - 1, -1, -1):
            for col in range(n):
                if row == n - 1:
                    min_path_sum[col] = grid[row][col]
                else:
                    min_path_sum[col] = self.getLastMinPathSumVal(last_min_path_sum, col) + grid[row][col]

            for i in range(n):
                last_min_path_sum[i] = min_path_sum[i]

        res = sys.maxsize
        for i in range(n):
            res = min(res, min_path_sum[i])
        return res

    def getLastMinPathSumVal(self, arr:List[int], idx: int) -> int:
        res = sys.maxsize
        size = len(arr)
        for i in range(size):
            if i == idx:
                continue
            else:
                res = min(res, arr[i])
        return res


# test
if __name__ == '__main__':
    # input =  [[1,2,3],[4,5,6],[7,8,9]]
    input = [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]
    res = Solution().minFallingPathSum(input)
    print(res)


