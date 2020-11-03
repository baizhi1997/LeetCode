
# @Title: 超级次方 (Super Pow)
# @Author: qinxinlei
# @Date: 2019-01-15 11:01:30
# @Runtime: 96 ms
# @Memory: N/A

class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        return pow(a,int(''.join(map(str,b))),1337)
