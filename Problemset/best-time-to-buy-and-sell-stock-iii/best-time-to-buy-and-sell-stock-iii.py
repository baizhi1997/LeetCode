
# @Title: 买卖股票的最佳时机 III (Best Time to Buy and Sell Stock III)
# @Author: qinxinlei
# @Date: 2018-10-13 15:07:50
# @Runtime: 60 ms
# @Memory: N/A

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1,buy2,sell1,sell2=float('-inf'),float('-inf'),0,0
        for price in prices:
            buy1=max(buy1,-price)
            sell1=max(sell1,buy1+price)
            buy2=max(buy2,sell1-price)
            sell2=max(sell2,buy2+price)
        return sell2
