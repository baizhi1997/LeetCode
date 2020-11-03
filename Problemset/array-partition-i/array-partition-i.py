
# @Title: 数组拆分 I (Array Partition I)
# @Author: qinxinlei
# @Date: 2018-10-18 20:34:53
# @Runtime: 100 ms
# @Memory: N/A

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
