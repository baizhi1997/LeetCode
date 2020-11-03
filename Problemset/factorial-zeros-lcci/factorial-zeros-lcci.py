
# @Title: 阶乘尾数 (Factorial Zeros LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 11:17:58
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans
