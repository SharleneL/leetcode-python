from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size == 0:
            return [-1, -1]

        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)

        return [first, last]

    # [1,1,*2*,2,3,3] target: right move to the last 1. left move to the first 2.
    def findFirst(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1  # search range: [left, right]

        while left <= right:  # terminate when left=right+1, aka [right+1, right]
            mid = left + (right - left) // 2  # to avoid overflow
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:  # arr[mid]<target
                left = mid + 1

        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    # [1,1,2,*2*,3,3] target: left move to the first 3. right move to the last 2.
    def findLast(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:  # arr[mid]<target
                left = mid + 1

        if right < 0 or nums[right] != target:
            return -1
        return right


# test
if __name__ == '__main__':
    nums = [1]
    target = 1

    result = Solution().searchRange(nums, target)
    print(result)