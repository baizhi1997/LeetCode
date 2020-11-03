
# @Title: 有效括号的嵌套深度 (Maximum Nesting Depth of Two Valid Parentheses Strings)
# @Author: qinxinlei
# @Date: 2020-06-02 21:04:09
# @Runtime: 60 ms
# @Memory: 13.6 MB

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = list()
        for i, ch in enumerate(seq):
            if ch == '(':
                ans.append(i % 2)
            else:
                ans.append(1 - i % 2)
        return ans

