
# @Title: 煎饼排序 (Pancake Sorting)
# @Author: qinxinlei
# @Date: 2019-03-13 11:08:13
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A: return []
        i=A.index(len(A))
        return [i+1,len(A)]+self.pancakeSort(A[-1:i:-1]+A[:i])
