
# @Title: 有效的括号 (Valid Parentheses)
# @Author: qinxinlei
# @Date: 2018-09-30 21:26:50
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic={')':'(',']':'[','}':'{'}
        stack=[]
        for c in s:
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
            elif not stack or stack.pop()!=dic[c]:
                return False
        return len(stack)==0
