
# @Title: 买卖股票的最佳时机含手续费 (Best Time to Buy and Sell Stock with Transaction Fee)
# @Author: qinxinlei
# @Date: 2020-06-24 15:07:47
# @Runtime: 920 ms
# @Memory: 20.6 MB

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        buy = float('-inf')
        sell = 0
        for i in range(len(prices)):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i] - fee)
        return sell
