
# @Title: 子数组最大平均数 I (Maximum Average Subarray I)
# @Author: qinxinlei
# @Date: 2018-11-09 16:56:25
# @Runtime: 192 ms
# @Memory: N/A

class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        x=sum(nums[:k])
        tmp=x
        for i in range(len(nums)-k):
            tmp=tmp+nums[i+k]-nums[i]
            x=max(x,tmp)
        return x/k
