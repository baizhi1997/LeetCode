
# @Title: 寻找重复数 (Find the Duplicate Number)
# @Author: qinxinlei
# @Date: 2020-06-22 21:52:22
# @Runtime: 112 ms
# @Memory: 15.8 MB

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
