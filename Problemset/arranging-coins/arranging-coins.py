
# @Title: 排列硬币 (Arranging Coins)
# @Author: qinxinlei
# @Date: 2018-10-04 10:53:47
# @Runtime: 44 ms
# @Memory: N/A

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n*2+0.25)-0.5)
