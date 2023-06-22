from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        res_arr = [None] * (n+2)
        res_arr[0] = 0
        self.helper(n+1, res_arr)
        return res[n+1]

    # distince ways climbing to staircase i
    def helper(self, i: int, res_arr):
        if i==0:
            res_arr[i] = 0
            return
        if i==1:
            res_arr[i] = 1
            return

        if (res_arr[i] != None): return


        if (res_arr[i-1] is None):
            res_arr[i-1] = self.helper(i-1, res_arr)
        if (res_arr[i-2] is None):
            res_arr[i-2] = self.helper(i-2, res_arr)
        res_arr[i] = res_arr[i-1] + res_arr[i-2]
        return

# test
if __name__ == '__main__':
    res = Solution().climbStairs(2)
    print(res)
