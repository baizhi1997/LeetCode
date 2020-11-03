
# @Title: 最长重复子数组 (Maximum Length of Repeated Subarray)
# @Author: qinxinlei
# @Date: 2018-12-03 12:45:35
# @Runtime: 88 ms
# @Memory: N/A

class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        def check(m):
            seen={A[i:i+m] for i in range(la-m+1)}
            return any(B[j:j+m] in seen for j in range(lb-m+1))
        A=''.join(map(chr,A))
        B=''.join(map(chr,B))
        la=len(A)
        lb=len(B)
        l,r=0,min(len(A),len(B))
        while l<r:
            m=(l+r+1)//2
            if check(m):
                l=m
            else:
                r=m-1
        return l
