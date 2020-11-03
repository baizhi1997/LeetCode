
# @Title: 不用加号的加法 (Add Without Plus LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 11:48:40
# @Runtime: 64 ms
# @Memory: 13.3 MB

class Solution:
    def add(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b != 0:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)

