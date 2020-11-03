
# @Title: 单调数列 (Monotonic Array)
# @Author: qinxinlei
# @Date: 2018-10-22 13:25:54
# @Runtime: 200 ms
# @Memory: N/A

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        l=len(A)
        if A[0]>A[-1]:
            for i in range(l-1):
                if A[i]<A[i+1]:
                    return False
        else:
            for i in range(l-1):
                if A[i]>A[i+1]:
                    return False
        return True
