'''

参考链接：https://leetcode-cn.com/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/
先猜一个数（有效范围 [left, right]里的中间数 mid），然后统计原始数组中小于等于这个中间数的元素的个数 cnt，如果 cnt 严格大于 mid，（注意我加了着重号的部分「小于等于」、「严格大于」）。根据抽屉原理，重复元素就在区间 [left, mid] 里

比如[1,3,4,2,2]
数字范围是[1, 4], 总共有5个数
我们从[1,4]里面随便挑一个数字出来。二分的话就找中间数，3
之后统计<=3的数字有几个。如果不存在duplicate的话，应该有3个。如果存在duplicate的话，应该>3个
因此如果>3的话，证明duplicate存在于[1, 3]之间。

接下来一轮就二分搜索[1, 3]
mid=2
cnt=2, >2

接下来二分搜索[1, 2]
mid=1
cnt=1, ==1

此时l==r==2
所以结果为2
'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)  # numbers between [1, n]; total number count=n+1

        # find a random number in between [1, n], calc how many numbers <= this rand number. if cnt=rand number, then duplication should be between (rand, n]. else should between [1, cnt]
        l = 1
        r = n

        while l < r:
            mid = int((l + r) / 2)  # 注意python里面3/2 = 2.5; int(2.6) = 2
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
                # r = n
            else:
                # l = 1
                r = mid

        return l