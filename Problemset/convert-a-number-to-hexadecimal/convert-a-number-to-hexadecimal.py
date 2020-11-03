
# @Title: 数字转换为十六进制数 (Convert a Number to Hexadecimal)
# @Author: qinxinlei
# @Date: 2018-11-10 14:46:44
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        return hex(num)[2:] if num>=0 else hex(0xffffffff+num+1)[2:]
