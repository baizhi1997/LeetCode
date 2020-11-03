
# @Title: 调整数组顺序使奇数位于偶数前面 (调整数组顺序使奇数位于偶数前面 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 22:05:45
# @Runtime: 64 ms
# @Memory: 17.4 MB

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] & 1:
                i += 1
            else:
                if nums[j] & 1:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j -= 1
        return nums
