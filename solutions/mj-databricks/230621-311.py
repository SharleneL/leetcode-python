from typing import List

"""
总结：有点脑筋急转弯。得想到将sparse转换成dense。
1. 用map表示dense matrix，坐标(i, j)作为key；sparse_matrix[i][j]的值作为value
2. 之后遍历dense_A的每个key-value pair，再在dense_B里面找是否有可以和这个坐标相乘的非零值。逐渐加总。 
step2 是主要难度。有点绕，需要想清楚A的哪行和B的哪列相乘。

=====语法总结: map=====
my_map = {}                         # init a map
my_map[(i, j)] = xxx                # map的key可以是tuplet
for (i, j) in my_map.keys()         # iterate keys
for ((i, j), val) in my_map.items() # iterate k-v pairs
"""

# 基本解法：逐个计算。
# class Solution:
#     def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
#         rowA = len(A)
#         # colA = len(A[0])
#         # rowB = len(B)
#         colB = len(B[0])
#
#         # res should be rowA * colB dimension
#         res = [[0] * colB for _ in range(rowA)]
#         for i in range(rowA):
#             for j in range(colB):
#                 res[i][j] = self.calculateGrid(A, B, i, j)
#
#         return res
#
#     # multiple A[row=i] and B[col=j]
#     def calculateGrid(self, A: List[List[int]], B: List[List[int]], i: int, j: int) -> int:
#         sum = 0
#
#         total = len(A)
#         for k in range(total+1):
#             sum += A[i][k] * B[k][j]
#
#         return sum

# 升级解法：
# 第一遍把A和B都转化成dense matrix：用一个map来存非零位置的值。dens_A_map[(i, j)] = A[i][j]
# 第二遍，双重遍历。外层遍历dense_A_map里面的每个key，也就是(i, j)。内层：查找B的第j行所有非零元素（从dens_B_map里面找）。如果有的话则相乘
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        dense_A = self.encode(A)
        dense_B = self.encode(B)
        res = [[0] * len(B[0]) for _ in range(len(A))]

        """这里的乘法规则有点绕。。需要好好想清楚，画个图"""
        # i-th row in A -> save to i-th row in res;
        # j-th col in A -> multiply with each elem (k) in j-th row in B, then save to res[i][k]
        for (i, j) in dense_A.keys():
            for k in range(len(B[0])):
                if (j, k) in dense_B:
                    res[i][k] += dense_A[(i, j)] * dense_B[(j, k)]

        return res

    def encode(self, sparse_m: List[List[int]]) -> {}:
        dense_m = {}
        for i in range(len(sparse_m)):
            for j in range(len(sparse_m[0])):
                if sparse_m[i][j] != 0:
                    dense_m[(i, j)] = sparse_m[i][j]

        return dense_m

# test
if __name__ == '__main__':
    A = [
        [1,0,0],
        [-1,0,3]
    ]

    B = [
        [7, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    res = Solution().multiply(A, B)
    print(res)
