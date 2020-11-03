
# @Title: 山脉数组的峰顶索引 (Peak Index in a Mountain Array)
# @Author: qinxinlei
# @Date: 2018-10-18 20:49:40
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l=0
        r=len(A)-1
        while l<=r:
            m=(l+r)//2
            if A[m-1]>A[m]:
                r=m-1
            elif A[m]<A[m+1]:
                l=m+1
            else:
                return m
