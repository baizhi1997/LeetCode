
# @Title: 最长特殊序列 Ⅰ (Longest Uncommon Subsequence I)
# @Author: qinxinlei
# @Date: 2018-11-17 13:45:18
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if a==b else max(len(a),len(b))
