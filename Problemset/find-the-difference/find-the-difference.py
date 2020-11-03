
# @Title: 找不同 (Find the Difference)
# @Author: qinxinlei
# @Date: 2018-10-25 20:30:11
# @Runtime: 36 ms
# @Memory: N/A

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return list(collections.Counter(t)-collections.Counter(s))[0]
