
# @Title: 无重复字符的最长子串 (Longest Substring Without Repeating Characters)
# @Author: qinxinlei
# @Date: 2018-11-05 20:45:03
# @Runtime: 84 ms
# @Memory: N/A

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={}
        ans,p=0,-1
        for i,c in enumerate(s):
            if c in dic:
                p=max(dic[c],p)
            ans=max(ans,i-p)
            dic[c]=i
        return ans
