
# @Title: 第 N 个泰波那契数 (N-th Tribonacci Number)
# @Author: qinxinlei
# @Date: 2019-07-31 11:23:50
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def tribonacci(self, n: int) -> int:
        x, y, z = 0, 1, 1
        for _ in range(n):
            x, y, z = y, z, x+y+z
        return x
