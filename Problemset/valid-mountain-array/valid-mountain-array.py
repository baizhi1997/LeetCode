
# @Title: 有效的山脉数组 (Valid Mountain Array)
# @Author: qinxinlei
# @Date: 2018-11-18 18:51:08
# @Runtime: 72 ms
# @Memory: N/A

class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        x=len(A)-1
        if x<2 or A[0]>=A[1] or A[-2]<=A[-1]:
            return False
        i=0
        A.append(A[-1])
        while A[i]<A[i+1]:
            i+=1
        while A[i]>A[i+1]:
            i+=1
        return i==x
