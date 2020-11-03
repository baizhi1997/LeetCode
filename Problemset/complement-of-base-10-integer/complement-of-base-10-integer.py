
# @Title: 十进制整数的反码 (Complement of Base 10 Integer)
# @Author: qinxinlei
# @Date: 2019-03-18 09:27:04
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        x=2
        while N>x-1:
            x*=2
        return x-1-N
