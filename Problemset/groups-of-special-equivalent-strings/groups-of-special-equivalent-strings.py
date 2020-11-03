
# @Title: 特殊等价字符串组 (Groups of Special-Equivalent Strings)
# @Author: qinxinlei
# @Date: 2018-10-20 13:06:55
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return len(set((''.join(sorted(s[::2])),''.join(sorted(s[1::2]))) for s in A))
