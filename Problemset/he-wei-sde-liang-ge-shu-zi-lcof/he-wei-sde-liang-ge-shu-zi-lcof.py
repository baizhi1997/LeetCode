
# @Title: 和为s的两个数字 (和为s的两个数字 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 22:14:20
# @Runtime: 140 ms
# @Memory: 24.3 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        while i < j:
            tmp = nums[i] + nums[j]
            if tmp > target:
                j -= 1
            elif tmp < target:
                i += 1
            else:
                return [nums[i], nums[j]]
        return None
