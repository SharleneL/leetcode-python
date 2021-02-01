class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        max_profit = 0
        prev_price = prices[0]
        for p in prices[1:]:
            if p > prev_price:
                max_profit += p - prev_price
                prev_price = p
            else:
                prev_price = p
        return max_profit


'''
1 pass:
当前价格高于前一天时，将价差计入利润。直到遍历结束，可以得到总利润。
'''