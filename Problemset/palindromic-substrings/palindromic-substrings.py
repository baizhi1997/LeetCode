
# @Title: 回文子串 (Palindromic Substrings)
# @Author: qinxinlei
# @Date: 2018-12-07 09:57:14
# @Runtime: 56 ms
# @Memory: N/A

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        i=0
        while i<len(s):
            start=i
            while i+1<len(s) and s[i+1]==s[i]:
                i+=1
            end=i
            ans+=(end-start+2)*(end-start+1)//2
            while start-1>=0 and end+1<len(s) and s[start-1]==s[end+1]:
                ans+=1
                start-=1
                end+=1
            i+=1
        return ans
