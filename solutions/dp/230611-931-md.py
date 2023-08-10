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

"""
input: nxn matrix
output: minSum(fallingPath)
def: `fallingPath`: [i, j] -> [i, j-1] / [i, j] / [i, j+1]


Basic:
iterate over all possible falling paths, find the smallest.
func dfs(i, j): return minSum starting from (i, j)
then return min of all dfs(i=0, j in range(total_col))

func dfs(i, j):
    # termination
    if i==last_row: 
        return matrix[i][j]
    elif j==0:
        return min(dfs(i+1, j), dfs(i+1, j+1)) # need to make sure matrix n>1
    elif j==n-1:
        return min(dfs(i+1, j-1), dfs(i+1, j))
    # process cur
    return min(dfs(i+1,j), dfs(i+1,j-1), dfs(i+1,j+1)) + matrix[i][j] # border: i+1<=last_row, j-1>=0, j+1<=last_col

Optimize:
There will be overlapping child problems. E.g. 1->6 and 2->6. 6 is overlapping problem
We can create a storage to store it.

"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        # n>=2
        min_path_sum_matrix = [[None for _ in range(n)] for _ in range(n)]
        for row in range(n - 1, -1, -1):  # row = [n-1 ~ 0]
            for col in range(n):
                if row == n - 1:
                    min_path_sum_matrix[row][col] = matrix[row][col]
                else:
                    if col == 0:
                        min_path_sum_matrix[row][col] = min(
                            min_path_sum_matrix[row+1][col],
                            min_path_sum_matrix[row+1][col + 1]
                        ) + matrix[row][col]
                    elif col == n - 1:
                        min_path_sum_matrix[row][col] = min(
                            min_path_sum_matrix[row+1][col],
                            min_path_sum_matrix[row+1][col - 1]
                        ) + matrix[row][col]
                    else:
                        min_path_sum_matrix[row][col] = min(
                            min_path_sum_matrix[row+1][col],
                            min_path_sum_matrix[row+1][col - 1],
                            min_path_sum_matrix[row+1][col + 1]
                        ) + matrix[row][col]

        res = sys.maxsize
        for i in range(n):
            res = min(min_path_sum_matrix[0][i], res)
        return res

# # 优化：我只需要知道上一行的optimal result。如果我用一个lastRowOptimalArr存储：
# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         n = len(matrix)
#         if (n == 1):
#             return matrix[0][0]
#
#         nextRowOptimalArr = matrix[n - 1]
#         for i in range(n - 2, -1, -1):
#             curOptimalArr = self.helper(i, matrix, nextRowOptimalArr)
#             nextRowOptimalArr = curOptimalArr
#
#         return min(nextRowOptimalArr)
#
#     # sub optimal (minFallPathSum) of each elem in row[i]
#     def helper(self, i, matrix, nextRowOptimalArr: List[int]) -> List[int]:
#         n = len(matrix)  # n>=2
#         if (i == n - 1):
#             return matrix[i]
#
#         curOptimal = []
#         for j in range(n):  # n>=2
#             if j == 0:
#                 curOptimal.append(
#                     min(
#                         nextRowOptimalArr[0],
#                         nextRowOptimalArr[1]
#                     ) + matrix[i][j]
#                 )
#             elif j == n - 1:
#                 curOptimal.append(
#                     min(
#                         nextRowOptimalArr[n - 2],
#                         nextRowOptimalArr[n - 1]
#                     ) + matrix[i][j]
#                 )
#             else:
#                 curOptimal.append(
#                     min(
#                         nextRowOptimalArr[j - 1],
#                         nextRowOptimalArr[j],
#                         nextRowOptimalArr[j + 1],
#                     ) + matrix[i][j]
#                 )
#
#         return curOptimal


# test
if __name__ == '__main__':
    input = [[2,1,3],[6,5,4],[7,8,9]]
    res = Solution().minFallingPathSum(input)
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