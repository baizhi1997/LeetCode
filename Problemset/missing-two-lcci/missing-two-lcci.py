
# @Title: 消失的两个数字 (Missing Two LCCI)
# @Author: qinxinlei
# @Date: 2020-07-17 16:59:50
# @Runtime: 84 ms
# @Memory: 16.3 MB

class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        nums += [1,1]
        for i in range(len(nums)-2):
            nums[abs(nums[i])-1] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]

