class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minPrice = sys.maxsize
        maxProfit = -sys.maxsize - 1
        for p in prices:
            if p < minPrice:
                minPrice = p
            if p - minPrice > maxProfit:
                maxProfit = p - minPrice
        return maxProfit


'''
解法：
过一遍, 用两个变量来记录当前最佳。
use *minPrice* to maintain the so-far min price
then go thru the whole list to cal the *maxDiff*
'''