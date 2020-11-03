
# @Title: 栈的压入、弹出序列 (栈的压入、弹出序列 LCOF)
# @Author: qinxinlei
# @Date: 2020-07-03 14:20:43
# @Runtime: 60 ms
# @Memory: 13.5 MB

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack

