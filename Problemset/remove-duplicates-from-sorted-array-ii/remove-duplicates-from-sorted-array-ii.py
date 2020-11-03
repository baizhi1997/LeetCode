
# @Title: 删除排序数组中的重复项 II (Remove Duplicates from Sorted Array II)
# @Author: qinxinlei
# @Date: 2018-09-27 22:40:57
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def removeDuplicates(self, nums):
        l=len(nums)
        if l<2:
            return l
        i=2
        for num in nums[2:]:
            if num!=nums[i-2]:
                nums[i]=num
                i+=1
        return i
