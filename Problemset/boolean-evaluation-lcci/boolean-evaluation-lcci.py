
# @Title: 布尔运算 (Boolean Evaluation LCCI)
# @Author: qinxinlei
# @Date: 2020-07-15 16:59:20
# @Runtime: 136 ms
# @Memory: 13.3 MB

class Solution:
    def countEval(self, s: str, result: int) -> int:
        """
        {
            符号: {
                需要计算出的结果: {
                    [(左子式需要计算的结果，右子式需要计算的结果)]
                }
            }
            
        }
        """
        self.ops = {
            '&': {
                True: [(True, True)],
                False: [(True, False), (False, True), (False, False)]
            },
            '|': {
                True: [(True, False), (False, True), (True, True)],
                False: [(False, False)]
            },
            '^': {
                True: [(True, False), (False, True)],
                False: [(True, True), (False, False)]
            }
        }
        return self.dfs(s, result, {})
        
    def dfs(self, expression, result, memo):
        # 查询备忘录，有结果则直接返回
        if (expression, result) in memo:
            return memo[(expression, result)]
        
        # 边界情况
        if len(expression) == 1:
            val = int(expression)
            return int(bool(val) == result)
        
        # 递归计算左右子式的结果
        total = 0
        for i in range(len(expression)):
            if expression[i] in self.ops:
                for lr, rr in self.ops[expression[i]][result]:
                    total += self.dfs(expression[:i], lr, memo)*self.dfs(expression[i+1:], rr, memo)
        memo[(expression, result)] = total
        return total

