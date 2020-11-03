
# @Title: 找出第 N 个二进制字符串中的第 K 位 (Find Kth Bit in Nth Binary String)
# @Author: qinxinlei
# @Date: 2020-08-10 16:38:04
# @Runtime: 48 ms
# @Memory: 13.4 MB

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k <= 1:
            return "0"
        tmp = 2
        while tmp < k:
            tmp *= 2
        return "1" if self.findKthBit(n, tmp-k) == "0" else "0"
        
