
# @Title: 最小差值 I (Smallest Range I)
# @Author: qinxinlei
# @Date: 2018-10-18 21:40:09
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0,max(A)-min(A)-2*K)

