
# @Title: 峰与谷 (Peaks and Valleys LCCI)
# @Author: qinxinlei
# @Date: 2020-06-22 23:00:55
# @Runtime: 48 ms
# @Memory: 14.1 MB

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if i & 1:
                if nums[i] > nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            else:
                if nums[i] < nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]

