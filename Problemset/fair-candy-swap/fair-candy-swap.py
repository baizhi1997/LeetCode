
# @Title: 公平的糖果交换 (Fair Candy Swap)
# @Author: qinxinlei
# @Date: 2018-10-22 14:05:58
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        x=(sum(B)-sum(A))//2
        set1=set(B)
        for i in A:
            if i+x in set1:
                return [i,i+x]
