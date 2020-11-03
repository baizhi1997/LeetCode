
# @Title: 主要元素 (Find Majority Element LCCI)
# @Author: qinxinlei
# @Date: 2020-07-09 16:10:19
# @Runtime: 68 ms
# @Memory: 14.8 MB

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for num in nums:
            if cnt == 0:
                ans = num
                cnt = 1
            elif num == ans:
                cnt += 1
            else:
                cnt -= 1
        cnt = 0
        for num in nums:
            if num == ans:
                cnt += 1
        return ans if cnt > len(nums) // 2 else -1
