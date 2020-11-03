
# @Title: 整数的各位积和之差 (Subtract the Product and Sum of Digits of an Integer)
# @Author: qinxinlei
# @Date: 2020-07-28 12:19:09
# @Runtime: 48 ms
# @Memory: 13.3 MB

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ji, he = 1, 0
        while n:
            n, tmp = divmod(n, 10)
            ji *= tmp
            he += tmp
        return ji-he
