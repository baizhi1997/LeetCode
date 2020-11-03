
# @Title: 找到所有数组中消失的数字 (Find All Numbers Disappeared in an Array)
# @Author: qinxinlei
# @Date: 2018-11-22 14:47:15
# @Runtime: 176 ms
# @Memory: N/A

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for num in nums:
            tmp=abs(num)
            nums[tmp-1]=-abs(nums[tmp-1])
        for i,num in enumerate(nums):
            if num>0:
                ans.append(i+1)
        return ans
