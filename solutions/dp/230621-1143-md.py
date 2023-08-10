# 还未通过，time limit exceed


"""
if w1[0] == w2[0]:
    LCS(w1, w2) = LCS(w1[1:], w2[1:]) + 1

else:
    LCS(w1, w2) = max(
        LCS(w1, w2[1:]),
        LCS(w1[1:], w2),
        LCS(w1[1:], w2[1:])
    )

edge case:
    if len(w1)==1 || len(w2) ==1:
        if w1.contains(w2) or w2.contains(w1): return 1
        else: return 0

WHAT IS THE TIME COST?
- recursion T = 递归的次数 * 每次递归中的操作次数
- 假设w1和w2的长度都是N。每次多比1个char。所以会递归N次。
- 每次的时间是
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.helper(text1, text2)

    # return the len of longestCommonSubsequence for <w1, w2>
    def helper(self, w1: str, w2: str) -> int:
        i f(len(w1 )= =1 or len(w2 )= =1):
            i f(w1 in w2 or w2 in w1):
                return 1
            else: return 0

        i f(w1[0] == w2[0]):
            return self.helper(w1[1:], w2[1:]) + 1

        return max(
            self.helper(w1, w2[1:]),
            self.helper(w1[1:], w2)
        )

"""
超时了^^
时间复杂度是O(m*n) - 假设w1和w2的长度分别是N和M。则一共有N*M个子问题。？？？
考虑存一下中间结果？
考虑自底向上？

create a 2-D array lcs[m][n], m=len(w1), n=len(w2)
lcs[i][j] means len of LCS of w1[i:] & w2[j:]
    i, j start from 0
    i<=m-1, j<=n-1
target: lcs[0][0]

init: 
if(w1[m-1] == w2[n-1]): lcs[m-1][n-1]=1
else: lcs[m-1][n-1]=0 

if(w1[m-1] is in w2): lcs[m-1][0~n-1] all = 1
else: all =0
if(w2[n-1] is in w1): lcs[0~m-1][n-1] all = 1
else: all =0

lcs[m-2][n-1]:
    if w1[]
lcs[m-1][n-2]
lcs[m-2][n-2]


参考文章：https://zhuanlan.zhihu.com/p/107756084
"""



# test
if __name__ == '__main__':
    res = Solution().getMaximumGenerated(7)
    print(res)
