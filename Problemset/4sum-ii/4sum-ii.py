
# @Title: 四数相加 II (4Sum II)
# @Author: qinxinlei
# @Date: 2018-12-01 16:16:11
# @Runtime: 356 ms
# @Memory: N/A

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic=collections.Counter(a+b for a in A for b in B)
        return sum(dic[-c-d] for c in C for d in D)
