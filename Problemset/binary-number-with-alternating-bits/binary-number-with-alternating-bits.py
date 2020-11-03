
# @Title: 交替位二进制数 (Binary Number with Alternating Bits)
# @Author: qinxinlei
# @Date: 2018-11-12 13:08:52
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n=bin(n)[2:]
        for i in range(len(n)-1):
            if n[i]==n[i+1]:
                return False
        return True
