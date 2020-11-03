
# @Title: 错误的集合 (Set Mismatch)
# @Author: qinxinlei
# @Date: 2018-10-04 14:23:28
# @Runtime: 40 ms
# @Memory: N/A

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        z=sum(set(nums))
        return [sum(nums)-z,(l*(l+1))/2-z]
