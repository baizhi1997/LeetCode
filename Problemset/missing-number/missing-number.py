
# @Title: 丢失的数字 (Missing Number)
# @Author: qinxinlei
# @Date: 2018-10-03 19:27:42
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        return l*(l+1)/2-sum(nums)
