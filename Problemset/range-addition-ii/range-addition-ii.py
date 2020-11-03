
# @Title: 范围求和 II (Range Addition II)
# @Author: qinxinlei
# @Date: 2018-10-04 11:38:53
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        return min([op[0] for op in ops])*min([op[1] for op in ops]) if ops else m*n
