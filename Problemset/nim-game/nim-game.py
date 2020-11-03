
# @Title: Nim 游戏 (Nim Game)
# @Author: qinxinlei
# @Date: 2018-10-08 20:53:12
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if n%4 else False
