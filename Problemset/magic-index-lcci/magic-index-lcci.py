
# @Title: 魔术索引 (Magic Index LCCI)
# @Author: qinxinlei
# @Date: 2020-07-09 16:05:59
# @Runtime: 36 ms
# @Memory: 14 MB

class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        i = 0
        length = len(nums)
        while i < length:
            if i == nums[i]: return i
            if nums[i] > i: i = nums[i]
            else: i += 1
        return -1

