
# @Title: 等差数列划分 (Arithmetic Slices)
# @Author: qinxinlei
# @Date: 2018-11-23 17:26:26
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans=0
        x=1
        for i in range(2,len(A)):
            if A[i]+A[i-2]==A[i-1]*2:
                ans+=x
                x+=1
            else:
                x=1
        return ans
