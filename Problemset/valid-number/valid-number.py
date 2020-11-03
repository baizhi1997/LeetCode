
# @Title: 有效数字 (Valid Number)
# @Author: qinxinlei
# @Date: 2018-10-03 15:11:35
# @Runtime: 48 ms
# @Memory: N/A

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
        except Exception:
            return False
        return True
