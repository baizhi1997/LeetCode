
# @Title: 按奇偶排序数组 (Sort Array By Parity)
# @Author: qinxinlei
# @Date: 2018-10-17 21:19:51
# @Runtime: 72 ms
# @Memory: N/A

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        len1=len(A)
        l=0
        r=len1-1
        while l<r:
            while l<len1 and A[l]%2==0:
                l+=1
            while r>=0 and A[r]%2:
                r-=1
            if l<r:
                A[l],A[r]=A[r],A[l]
            l+=1
            r-=1
        return A
