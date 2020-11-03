
# @Title: n个骰子的点数 (n个骰子的点数  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-26 11:55:55
# @Runtime: 44 ms
# @Memory: 13.3 MB

class Solution:
    def twoSum(self, n: int) -> List[float]:
        dp = [[0 for i in range(n*6+1)] for j in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(i, i*6+1):
                x = max(0, j-6)
                dp[i][j] = sum(dp[i-1][x:j])/6
        return dp[n][n:n*6+1]
