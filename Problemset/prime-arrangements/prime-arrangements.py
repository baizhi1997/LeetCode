
# @Title: 质数排列 (Prime Arrangements)
# @Author: qinxinlei
# @Date: 2020-08-02 20:38:54
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isPrime(n):
            if n == 1:
                return False
            for i in range(2, n):
                if n%i == 0:
                    return False
            return True
        ans = 1
        x = 0
        y = 0
        for i in range(1, n+1):
            if isPrime(i):
                x += 1
                ans *= x
            else:
                y += 1
                ans *= y
            ans %= 10**9+7
        return ans
