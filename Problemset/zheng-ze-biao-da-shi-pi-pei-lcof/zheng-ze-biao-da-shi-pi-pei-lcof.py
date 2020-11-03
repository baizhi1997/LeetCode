
# @Title: 正则表达式匹配 (正则表达式匹配 LCOF)
# @Author: qinxinlei
# @Date: 2020-07-06 23:02:10
# @Runtime: 64 ms
# @Memory: 13.4 MB

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = '#'+s, '#'+p
        m, n = len(s), len(p)
        dp = [[False]*n for _ in range(m)]
        dp[0][0] = True
        
        for i in range(m):
            for j in range(1, n):
                if i == 0:
                    dp[i][j] = j > 1 and p[j] == '*' and dp[i][j-2]
                elif p[j] in [s[i], '.']:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    dp[i][j] = j > 1 and dp[i][j-2] or p[j-1] in [s[i], '.'] and dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]

