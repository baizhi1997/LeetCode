
# @Title: 跳跃游戏 II (Jump Game II)
# @Author: qinxinlei
# @Date: 2018-09-23 17:37:38
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        j=0
        k=0
        for i in range(len(nums)-1):
            j=max(j,i+nums[i])
            if (i==k):
                k=j
                ans+=1
        return ans

