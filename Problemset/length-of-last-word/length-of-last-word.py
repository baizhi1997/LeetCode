
# @Title: 最后一个单词的长度 (Length of Last Word)
# @Author: qinxinlei
# @Date: 2018-10-01 14:53:03
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1=s.split()
        if not s1:
            return 0
        return len(s1[-1])
