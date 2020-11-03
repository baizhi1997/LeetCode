
# @Title: 存在重复元素 (Contains Duplicate)
# @Author: qinxinlei
# @Date: 2018-10-11 21:47:30
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums)!=len(set(nums))
