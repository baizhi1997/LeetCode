
# @Title: 括号 (Bracket LCCI)
# @Author: qinxinlei
# @Date: 2020-06-02 15:06:18
# @Runtime: 52 ms
# @Memory: 13.4 MB

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        ans = []
        for i in range(0, n):
            for x in self.generateParenthesis(i):
                for y in self.generateParenthesis(n-i-1):
                    ans.append('('+x+')'+y)
        return ans
