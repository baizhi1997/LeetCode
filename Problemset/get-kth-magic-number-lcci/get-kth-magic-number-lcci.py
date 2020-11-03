
# @Title: 第 k 个数 (Get Kth Magic Number LCCI)
# @Author: qinxinlei
# @Date: 2020-07-14 23:25:09
# @Runtime: 48 ms
# @Memory: 13.4 MB

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp, a, b, c = [1] * k, 0, 0, 0
        for i in range(1, k):
            n2, n3, n5 = dp[a] * 3, dp[b] * 5, dp[c] * 7
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]
