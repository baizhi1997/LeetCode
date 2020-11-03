
# @Title: 整数转换 (Convert Integer LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 14:02:45
# @Runtime: 44 ms
# @Memory: 13.3 MB

class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        return bin((A & 0xffffffff) ^ (B & 0xffffffff)).count('1')
