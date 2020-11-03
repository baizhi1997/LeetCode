
# @Title: 石子游戏 II (Stone Game II)
# @Author: qinxinlei
# @Date: 2020-08-14 14:02:04
# @Runtime: 168 ms
# @Memory: 13.5 MB

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        s = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            s[i] = s[i + 1] + piles[i]
        dp = [[0 for _ in range(n+1)] for _ in range(n + 1)]
        for i in range(n - 1,-1,-1):
            for M in range(1,n+1):
                if i + 2 * M >= n:
                    dp[i][M] = s[i]
                    continue
                x = 1
                while x <= 2 * M:
                    dp[i][M] = max(dp[i][M],s[i] - dp[i+x][max(x,M)])
                    x += 1
        return dp[0][1]

