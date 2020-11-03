
# @Title: 和为K的子数组 (Subarray Sum Equals K)
# @Author: qinxinlei
# @Date: 2018-12-03 21:13:56
# @Runtime: 76 ms
# @Memory: N/A

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d={0:1}
        t=0
        ans=0
        for num in nums:
            t+=num
            ans+=d.get(t-k,0)
            d[t]=d.get(t,0)+1
        return ans
