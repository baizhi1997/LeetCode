
# @Title: 字符串中的第一个唯一字符 (First Unique Character in a String)
# @Author: qinxinlei
# @Date: 2018-10-28 10:56:59
# @Runtime: 116 ms
# @Memory: N/A

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic=collections.Counter(s)
        for i,c in enumerate(s):
            if dic[c]==1:
                return i
        return -1
