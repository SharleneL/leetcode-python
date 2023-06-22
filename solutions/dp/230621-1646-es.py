
class Solution:
    def getMaximumGenerated(self, n: int) -> int: # n>=0
        if n == 0: return 0
        if n == 1: return 1

        nums = [0] * (n+1) #n+1>=1
        nums[1] = 1

        # 自底向上
        for i in range(0, n+1):
            if(i*2)<=n:
                nums[i*2] = nums[i]
            if(i*2+1)<=n:
                nums[i*2 + 1] = nums[i] + nums[i+1]

        return max(nums)


# test
if __name__ == '__main__':
    res = Solution().getMaximumGenerated(7)
    print(res)
