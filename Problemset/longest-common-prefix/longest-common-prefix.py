
# @Title: 最长公共前缀 (Longest Common Prefix)
# @Author: qinxinlei
# @Date: 2018-09-30 20:10:04
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''       
        s1=min(strs)
        s2=max(strs)      
        for i,k in enumerate(s1):
            if k!=s2[i]:
                return s1[:i]
        return s1
