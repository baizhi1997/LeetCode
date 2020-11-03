
# @Title: 计算器 (Calculator LCCI)
# @Author: qinxinlei
# @Date: 2020-07-17 16:17:34
# @Runtime: 148 ms
# @Memory: 15 MB

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        stack = []
        res = 0
        cur = ''
        for i in range(len(s)+1):
            c = 'E' if i >= len(s) else s[i]
            if c.isnumeric():
                cur += c
            else:
                cur = int(cur)
                if  stack and (stack[-1] == '*' or stack[-1] == '/'):
                    if stack[-1] == '*': cur*=stack[-2]
                    else: cur = stack[-2] // cur
                    stack.pop()
                    stack.pop()
                stack.append(cur)
                cur = ''
                if i < len(s):
                    stack.append(c)
                else:
                    res = stack[0]
                    for i in range(2, len(stack)):
                        if type(stack[i]) is int:
                            if stack[i-1] == '+':
                                res += stack[i]
                            else: res -= stack[i]
                    return res
