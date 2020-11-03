
# @Title: 二进制中1的个数 (二进制中1的个数 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 23:19:15
# @Runtime: 36 ms
# @Memory: 13.4 MB

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
