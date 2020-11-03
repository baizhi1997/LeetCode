
# @Title: 最长不含重复字符的子字符串 (最长不含重复字符的子字符串 LCOF)
# @Author: qinxinlei
# @Date: 2020-07-04 11:28:40
# @Runtime: 76 ms
# @Memory: 13.4 MB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        ans,p=0,-1
        for i,c in enumerate(s):
            if c in dic:
                p=max(dic[c],p)
            ans=max(ans,i-p)
            dic[c]=i
        return ans
