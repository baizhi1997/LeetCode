
# @Title: 重塑矩阵 (Reshape the Matrix)
# @Author: qinxinlei
# @Date: 2018-11-17 13:29:38
# @Runtime: 88 ms
# @Memory: N/A

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c!=len(nums)*len(nums[0]):
            return nums
        items=[y for x in nums for y in x]
        return [items[i*c:((i+1)*c)] for i in range(r)]
