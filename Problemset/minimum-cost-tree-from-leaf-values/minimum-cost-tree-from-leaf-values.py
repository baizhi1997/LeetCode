
# @Title: 叶值的最小代价生成树 (Minimum Cost Tree From Leaf Values)
# @Author: qinxinlei
# @Date: 2020-10-09 17:08:22
# @Runtime: 44 ms
# @Memory: 13.5 MB

class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        res, n = 0, len(A)
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res

