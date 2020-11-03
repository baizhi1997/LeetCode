
# @Title: 最大连续1的个数 (Max Consecutive Ones)
# @Author: qinxinlei
# @Date: 2018-10-22 13:44:30
# @Runtime: 68 ms
# @Memory: N/A

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        tmp=0
        nums.append(0)
        for num in nums:
            if num:
                tmp+=1
            else:
                ans=max(ans,tmp)
                tmp=0
        return ans
