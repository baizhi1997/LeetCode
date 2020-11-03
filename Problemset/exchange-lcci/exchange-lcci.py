
# @Title: 配对交换 (Exchange LCCI)
# @Author: qinxinlei
# @Date: 2020-07-08 20:20:05
# @Runtime: 40 ms
# @Memory: 13.1 MB

class Solution:
    def exchangeBits(self, num: int) -> int:
        return ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)
