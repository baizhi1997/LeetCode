
# @Title: 最长有效括号 (Longest Valid Parentheses)
# @Author: qinxinlei
# @Date: 2019-05-02 20:20:02
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(i - stack[-1], ans)
        return ans
