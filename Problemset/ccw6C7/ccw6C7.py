
# @Title: 黑白方格画 (黑白方格画)
# @Author: qinxinlei
# @Date: 2020-10-28 15:57:28
# @Runtime: 36 ms
# @Memory: 13.4 MB

class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        def c(n,a):
            res = 1
            for i in range(n,n-a,-1):
                res *= i
            for j in range(1,a+1):
                res //= j
            return res
        ans = 0
        x = n*n-k
        if x == 0:
            return 1
        for i in range(1, n+1):
            if x%i == 0 and x//i < n+1:
                ans += c(n,i)*c(n,x//i)
        return ans
