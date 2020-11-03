
# @Title: 不用加减乘除做加法 (不用加减乘除做加法 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-26 11:30:31
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)


