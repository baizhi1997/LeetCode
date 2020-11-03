
# @Title: 使括号有效的最少添加 (Minimum Add to Make Parentheses Valid)
# @Author: qinxinlei
# @Date: 2018-11-19 16:14:56
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        l=0
        r=0
        for c in S:
            if c=="(":
                l+=1
            elif l>0:
                l-=1
            else:
                r+=1
        return l+r
