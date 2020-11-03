
# @Title: 正则表达式匹配 (Regular Expression Matching)
# @Author: qinxinlei
# @Date: 2018-09-30 18:06:07
# @Runtime: 88 ms
# @Memory: N/A

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        tmp=re.match(p,s)
        if tmp!=None and tmp.group()==s:
            return True
        return False
    
