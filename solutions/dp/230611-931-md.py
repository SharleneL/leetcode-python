from typing import List

import sys


# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         n = len(matrix)
#         res = sys.maxsize
#         for i in range(n):
#             res = min(res, self.helper(0, i, matrix))
#         return res

#     # min sum of falling path starting from [i][j]
#     def helper(self, i, j, matrix: List[List[int]]) -> int:
#         n = len(matrix)

#         if(j<0 or j>=n):
#             return sys.maxsize
#         if(i == n-1):
#             return matrix[i][j]

#         return min(
#             self.helper(i+1, j-1, matrix),
#             self.helper(i+1, j, matrix),
#             self.helper(i+1, j+1, matrix)
#         ) + matrix[i][j]


# 优化：我只需要知道上一行的optimal result。如果我用一个lastRowOptimalArr存储：
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if (n == 1):
            return matrix[0][0]

        nextRowOptimalArr = matrix[n - 1]
        for i in range(n - 2, -1, -1):
            curOptimalArr = self.helper(i, matrix, nextRowOptimalArr)
            nextRowOptimalArr = curOptimalArr

        return min(nextRowOptimalArr)

    # sub optimal (minFallPathSum) of each elem in row[i]
    def helper(self, i, matrix, nextRowOptimalArr: List[int]) -> List[int]:
        n = len(matrix)  # n>=2
        if (i == n - 1):
            return matrix[i]

        curOptimal = []
        for j in range(n):  # n>=2
            if j == 0:
                curOptimal.append(
                    min(
                        nextRowOptimalArr[0],
                        nextRowOptimalArr[1]
                    ) + matrix[i][j]
                )
            elif j == n - 1:
                curOptimal.append(
                    min(
                        nextRowOptimalArr[n - 2],
                        nextRowOptimalArr[n - 1]
                    ) + matrix[i][j]
                )
            else:
                curOptimal.append(
                    min(
                        nextRowOptimalArr[j - 1],
                        nextRowOptimalArr[j],
                        nextRowOptimalArr[j + 1],
                    ) + matrix[i][j]
                )

        return curOptimal


# test
if __name__ == '__main__':
    res = Solution().minFallingPathSum([[-19,57],[-40,-5]])
    print(res)


"""
input: n x n matrix
output: an int. min sum of [falling path]
    - falling path: 
        - start from any elem in matrix[0]
            matrix[0][j]
        - pick elem in matrix[1]: matrix[1][j-1] or matrix[1][j+1]

can iterate over all possible solutions, calculate sum for each, then pick the min sum.

global optimal
last step's optimal
I only need to know prev row's optimal

helper(i, j) => min sum of falling path starting from [i][j]
    i>=0 <=n-1; j>=0 <=n-1

imagine I already know helper(i+1, j-1), helper(i+1, j), helper(i+1, j+1)
    helper(i, j) = min[
        helper(i+1, j-1), 
        helper(i+1, j), 
        helper(i+1, j+1)
    ] + matric[i][j]

edge case:
i=n-1:
    return matrix[i, j]
or
j=0:
    helper(i, j) = min[
        helper(i+1, j), 
        helper(i+1, j+1)
    ] + matric[i][j]
or
j=n-1:
    helper(i, j) = min[
        helper(i+1, j-1), 
        helper(i+1, j)
    ] + matric[i][j]

"""