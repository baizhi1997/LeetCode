
# @Title: 股票的最大利润 (股票的最大利润  LCOF)
# @Author: qinxinlei
# @Date: 2020-05-14 16:30:39
# @Runtime: 56 ms
# @Memory: 14.2 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price-min_price)
        return max_profit

