
# @Title: 为运算表达式设计优先级 (Different Ways to Add Parentheses)
# @Author: qinxinlei
# @Date: 2020-06-04 21:16:54
# @Runtime: 28 ms
# @Memory: 13.4 MB

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        res = []
        for i, char in enumerate(input):
            if char in ['+', '-', '*']:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res

