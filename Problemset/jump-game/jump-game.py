
# @Title: 跳跃游戏 (Jump Game)
# @Author: qinxinlei
# @Date: 2018-09-23 22:18:26
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)
        s=0
        for i in range(l):
            s=max(s,i+nums[i])
            if s>=(l-1):
                return True
            if i==s:
                break
        return False
