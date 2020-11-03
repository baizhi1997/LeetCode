
# @Title: 传递信息 (传递信息)
# @Author: qinxinlei
# @Date: 2020-07-24 10:20:14
# @Runtime: 32 ms
# @Memory: 13.1 MB

class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dp = [[0]*(n+1) for t in range(0,k+1)]
        dp[0][0] = 1

        for t in range(0,k):
            for x,y in relation:
                dp[t+1][y] += dp[t][x]
        return dp[k][n-1]

