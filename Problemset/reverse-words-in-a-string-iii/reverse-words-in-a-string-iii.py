
# @Title: 反转字符串中的单词 III (Reverse Words in a String III)
# @Author: qinxinlei
# @Date: 2018-10-19 11:30:31
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s[::-1].split()[::-1])
