
# @Title: 最小移动次数使数组元素相等 (Minimum Moves to Equal Array Elements)
# @Author: qinxinlei
# @Date: 2018-10-04 10:59:15
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)-min(nums)*len(nums)
