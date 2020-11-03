
# @Title: 重复的子字符串 (Repeated Substring Pattern)
# @Author: qinxinlei
# @Date: 2018-11-14 21:02:38
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s+s)[1:-1]
