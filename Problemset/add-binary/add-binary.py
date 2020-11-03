
# @Title: 二进制求和 (Add Binary)
# @Author: qinxinlei
# @Date: 2018-10-01 14:48:37
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2)+int(b,2))[2:]
