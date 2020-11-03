
# @Title: 硬币 (Coin LCCI)
# @Author: qinxinlei
# @Date: 2020-07-14 23:22:46
# @Runtime: 896 ms
# @Memory: 63.2 MB

class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10**9 + 7
        coins = [25, 10, 5, 1]

        f = [1] + [0] * n
        for coin in coins:
            for i in range(coin, n + 1):
                f[i] += f[i - coin]
        return f[n] % mod


