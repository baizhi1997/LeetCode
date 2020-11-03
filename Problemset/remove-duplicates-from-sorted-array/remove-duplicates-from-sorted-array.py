
# @Title: 删除排序数组中的重复项 (Remove Duplicates from Sorted Array)
# @Author: qinxinlei
# @Date: 2018-09-21 19:02:35
# @Runtime: 44 ms
# @Memory: N/A

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i=1
        for num in nums:
            if num!=nums[i-1]:
                nums[i]=num
                i+=1
        return i

