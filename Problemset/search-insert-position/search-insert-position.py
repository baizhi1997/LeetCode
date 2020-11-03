
# @Title: 搜索插入位置 (Search Insert Position)
# @Author: qinxinlei
# @Date: 2018-09-28 09:56:23
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums,target)

