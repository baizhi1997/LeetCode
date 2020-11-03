
# @Title: 买卖股票的最佳时机 II (Best Time to Buy and Sell Stock II)
# @Author: qinxinlei
# @Date: 2018-10-13 11:54:21
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans=0
        buy=float('inf')
        for price in prices:
            if price>buy:
                ans+=(price-buy)
            buy=price
        return ans
