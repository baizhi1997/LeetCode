
# @Title: 字符串中的单词数 (Number of Segments in a String)
# @Author: qinxinlei
# @Date: 2018-11-08 16:18:34
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
