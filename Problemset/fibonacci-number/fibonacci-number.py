
# @Title: 斐波那契数 (Fibonacci Number)
# @Author: qinxinlei
# @Date: 2019-03-01 16:28:35
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def fib(self, N: int) -> int:
        a,b=0,1
        for _ in range(N):
            a,b=b,a+b
        return a
