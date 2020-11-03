
# @Title: 数字的补数 (Number Complement)
# @Author: qinxinlei
# @Date: 2018-10-20 13:08:24
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return pow(2,num.bit_length())-num-1
)-num-1
