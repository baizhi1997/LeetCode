
# @Title: 数组中重复的数据 (Find All Duplicates in an Array)
# @Author: qinxinlei
# @Date: 2018-11-22 15:04:56
# @Runtime: 248 ms
# @Memory: N/A

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for x in nums:
            i=abs(x)-1
            if nums[i]<0:
                ans.append(i+1)
            else:
                nums[i]*=-1
        return ans
