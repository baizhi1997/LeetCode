
# @Title: 逆波兰表达式求值 (Evaluate Reverse Polish Notation)
# @Author: qinxinlei
# @Date: 2019-05-24 10:42:50
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = set(['+', '-', '*', '/'])
        for t in tokens:
            if t not in s:
                stack.append(int(t))
            else:
                y = stack.pop()
                x = stack.pop()
                if t == '+':
                    stack.append(x + y)
                elif t == '-':
                    stack.append(x - y)
                elif t == '*':
                    stack.append(x * y)
                else:
                    stack.append(int(x / y))
        return stack[0]
