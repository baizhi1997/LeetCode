
# @Title: 括号生成 (Generate Parentheses)
# @Author: qinxinlei
# @Date: 2018-10-01 11:47:02
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp=[[] for i in range(n+1)]
        dp[0].append('')
        for i in range(n+1):
            for j in range(i):
                dp[i]+=['('+x+')'+y for x in dp[j] for y in dp[i-j-1]]
        return dp[n]
    
