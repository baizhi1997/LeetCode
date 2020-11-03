
# @Title: 按奇偶排序数组 II (Sort Array By Parity II)
# @Author: qinxinlei
# @Date: 2018-10-18 20:08:26
# @Runtime: 168 ms
# @Memory: N/A

class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans=[0]*len(A)
        even=0
        odd=1
        for i in A:
            if i%2==0:
                ans[even]=i
                even+=2
            else:
                ans[odd]=i
                odd+=2
        return ans
    
