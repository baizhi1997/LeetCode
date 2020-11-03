
# @Title: 颠倒二进制位 (Reverse Bits)
# @Author: qinxinlei
# @Date: 2018-11-10 13:17:39
# @Runtime: 20 ms
# @Memory: N/A

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2::].zfill(32)[::-1],2)
