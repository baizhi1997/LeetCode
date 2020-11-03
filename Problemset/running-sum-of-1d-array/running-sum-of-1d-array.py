
# @Title: 一维数组的动态和 (Running Sum of 1d Array)
# @Author: qinxinlei
# @Date: 2020-06-15 20:32:00
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            nums[i+1] += nums[i]
        return nums 
