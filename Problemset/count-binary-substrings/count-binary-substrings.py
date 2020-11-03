
# @Title: 计数二进制子串 (Count Binary Substrings)
# @Author: qinxinlei
# @Date: 2018-11-12 13:22:43
# @Runtime: 120 ms
# @Memory: N/A

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        x=0
        y=0
        p=s[0]
        for c in s+' ':
            if c==p:
                x+=1
            else:
                p=c
                ans+=min(x,y)
                y=x
                x=1
        return ans
