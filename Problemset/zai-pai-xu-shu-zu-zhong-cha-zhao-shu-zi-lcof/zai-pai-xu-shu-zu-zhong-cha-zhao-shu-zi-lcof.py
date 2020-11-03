
# @Title: 在排序数组中查找数字 I (在排序数组中查找数字  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-26 12:06:51
# @Runtime: 40 ms
# @Memory: 14.3 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect.bisect_right(nums, target) - bisect.bisect_left(nums, target)

