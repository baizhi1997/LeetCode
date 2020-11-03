
# @Title: 买卖股票的最佳时机 (Best Time to Buy and Sell Stock)
# @Author: qinxinlei
# @Date: 2018-10-13 11:37:27
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=float('inf')
        profit=0
        for price in prices:
            min_price=min(price,min_price)
            profit=max(profit,price-min_price)
        return profit
