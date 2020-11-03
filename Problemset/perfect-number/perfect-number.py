
# @Title: 完美数 (Perfect Number)
# @Author: qinxinlei
# @Date: 2018-10-04 11:25:34
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in [6,28,496,8128,33550336]
