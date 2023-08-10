from typing import List

# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         max_row_cnt = len(triangle)
#         min_sum_matrix = [
#             [None for _ in range(i+1)] for i in range(max_row_cnt)
#         ]
#
#         for cur_row in range(max_row_cnt - 1, -1, -1):  # iterate [rows-1 -> 0]
#             for cur_col in range(len(triangle[cur_row])):
#                 if cur_row == max_row_cnt - 1:
#                     min_sum_matrix[cur_row][cur_col] = triangle[cur_row][cur_col]
#                 else:
#                     if cur_col + 1 < len(triangle[cur_row + 1]):
#                         min_sum_matrix[cur_row][cur_col] = min(
#                             min_sum_matrix[cur_row + 1][cur_col],
#                             min_sum_matrix[cur_row + 1][cur_col + 1]
#                         ) + triangle[cur_row][cur_col]
#                     else:
#                         min_sum_matrix[cur_row][cur_col] = triangle[cur_row + 1][cur_col]
#
#         return min_sum_matrix[0][0]

"""
优化：如果我只用一行arr存上一行的min
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        max_row_cnt = len(triangle)
        max_col_cnt = len(triangle[max_row_cnt - 1])
        min_sum_row = [None for _ in range(max_col_cnt)]

        for cur_row in range(max_row_cnt - 1, -1, -1):  # iterate [rows-1 -> 0]
            for cur_col in range(len(triangle[cur_row])):
                if cur_row == max_row_cnt - 1:
                    min_sum_row[cur_col] = triangle[cur_row][cur_col]
                else:
                    if cur_col + 1 < len(triangle[cur_row + 1]):
                        cur_min_sum = min(
                            min_sum_row[cur_col],
                            min_sum_row[cur_col+1],
                        ) + triangle[cur_row][cur_col]
                        min_sum_row[cur_col] = cur_min_sum
                    else:
                        min_sum_row[cur_col] = triangle[cur_row + 1][cur_col]

        return min_sum_row[0]


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
    input = [[2],[3,4],[6,5,7],[4,1,8,3]]
    res = Solution().minimumTotal(input)
    print(res)