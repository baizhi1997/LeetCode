
# @Title: 最小覆盖子串 (Minimum Window Substring)
# @Author: qinxinlei
# @Date: 2018-10-03 10:28:04
# @Runtime: 132 ms
# @Memory: N/A

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnts=collections.Counter(t)
        k=len(t)
        size=float("inf")
        ans=""
        l=0
        for r in range(len(s)):
            if cnts[s[r]]>0:
                k-=1
            cnts[s[r]]-=1
            while k==0:
                if r-l+1<size:
                    size=r-l+1
                    ans=s[l:r+1]
                if cnts[s[l]]==0:
                    k+=1
                cnts[s[l]]+=1
                l+=1
        return ans
