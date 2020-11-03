
# @Title: 全局倒置与局部倒置 (Global and Local Inversions)
# @Author: qinxinlei
# @Date: 2019-01-15 11:58:01
# @Runtime: 120 ms
# @Memory: N/A

class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i,n in enumerate(A):
            if abs(i-n)>1:
                return False
        return True
