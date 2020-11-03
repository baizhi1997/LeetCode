
# @Title: 斐波那契数列 (斐波那契数列  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-26 13:53:25
# @Runtime: 48 ms
# @Memory: 13.4 MB

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

