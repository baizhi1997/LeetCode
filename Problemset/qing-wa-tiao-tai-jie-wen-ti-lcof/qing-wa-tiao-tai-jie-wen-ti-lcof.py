
# @Title: 青蛙跳台阶问题 (青蛙跳台阶问题  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-26 13:55:48
# @Runtime: 32 ms
# @Memory: 13.2 MB

class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

