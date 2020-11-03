
# @Title: 棒球比赛 (Baseball Game)
# @Author: qinxinlei
# @Date: 2018-11-06 14:38:37
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack=[]
        for op in ops:
            if op=='+':
                stack.append(stack[-1]+stack[-2])
            elif op=='D':
                stack.append(stack[-1]*2)
            elif op=='C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
