
# @Title: 数组中出现次数超过一半的数字 (数组中出现次数超过一半的数字  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 22:20:35
# @Runtime: 52 ms
# @Memory: 14.7 MB

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        ans = nums[0]
        for n in nums:
            if n == ans:
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                ans = n
                cnt = 1
        return ans
