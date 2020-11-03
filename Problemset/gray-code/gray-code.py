
# @Title: 格雷编码 (Gray Code)
# @Author: qinxinlei
# @Date: 2018-12-17 20:44:16
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [(i>>1)^i for i in range(2**n)]
