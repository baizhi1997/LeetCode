
# @Title: 连续的子数组和 (Continuous Subarray Sum)
# @Author: qinxinlei
# @Date: 2018-11-27 21:16:40
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l=len(nums)
        if l<2:
            return False
        if k==0:
            for i in range(l-1):
                if nums[i]==nums[i+1]==0:
                    return True
            return False
        set1={0,nums[0]%k}
        tmp=nums[0]
        for num in nums[1:]:
            tmp+=num
            if tmp%k in set1:
                return True
            set1.add(tmp%k)
        return False
