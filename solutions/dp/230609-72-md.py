# TODO：还没有通过。递归算法的时间 & 空间复杂度是多少？
# 第一种做法 直接用递归：time limit exceed。所以得找个二维数组存中间值。
# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         return self.dp(word1, word2)
#
#     def dp(self, w1, w2) -> int:
#         if len(w1) == 0:
#             return len(w2)
#         elif len(w2) == 0:
#             return len(w1)
#
#         if w1[0] == w2[0]:
#             return self.dp(w1[1:], w2[1:])
#         return min(
#             self.dp(w1[1:], w2[1:]) + 1,
#             self.dp(w1, w2[1:]) + 1,
#             self.dp(w1[1:], w2) + 1
#         )

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.dp(word1, word2)

    # len(w1)=i, len(w2)=j, how many ops btw w1 & w2
    # fill in dis[i][j] with ops btw word1 & word2
    def dp(self, w1, w2) -> int:
        if len(w1) == 0:
            # return len(w2)
        elif len(w2) == 0:
            # return len(w1)

        if w1[0] == w2[0]:
            return self.dp(w1[1:], w2[1:])
        return min(
            self.dp(w1[1:], w2[1:]) + 1,
            self.dp(w1, w2[1:]) + 1,
            self.dp(w1[1:], w2) + 1
        )

# test
if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    res = Solution().minDistance(word1, word2)
    print(res)

"""
input: word1 & word2
output: a num. min ops num to convert w1 to w2
    - what is convert op?
    1. insert
    2. delete
    3. replace

horse
ros

ors
os

or
o

1. 定义dp数组
dp[i][j]: len(w1)=i, len(w2)=j, how many ops btw w1 & w2

2. 找递推
    假设我们知道w1[i-1]和w2[j-1]之间需要dp(i-1, j-1)步
    - 如果w1[i] == w2[j] 那么不需要调整。dp[i][j] = dp[i-1][j-1]
    - 如果w1[i] != w2[j]：那么需要调整。有三种方法进行调整：
        1. 把w1[i]替换成w2[j]。所以需要dp[i-1][j-1]+1步。
        2. 在w1[i]的前/后插入一个和w2[j]相等的值。所以需要dp[i][j-1]+1步。
        3. 把w1[i]替换成w2[j]。所以需要dp[i-1][j-1]+1步。

3. 初始值
    - 如果i=0: dp[i][j] = j (w2只需要insert j次)
    - 如果j=0: dp[i][j] = i (w1只需要insert j次)

"""