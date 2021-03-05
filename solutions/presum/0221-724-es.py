class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        pre_sum = 0  # sum of [0, i) - exclude i
        for i in range(len(nums)):
            if pre_sum == nums_sum - nums[i] - pre_sum:
                return i
            else:
                pre_sum += nums[i]

        return -1


'''
round1: sum nums
round2: for each i in nums, calc sum[0-i), compare it with sum-num[i]-sum[0-i)]
time: O(N)
space: O(N)

round1: calc presum of each item - Time ON, Space ON
round2: 
'''