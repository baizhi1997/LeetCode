
# @Title: 除自身以外数组的乘积 (Product of Array Except Self)
# @Author: qinxinlei
# @Date: 2018-11-28 17:55:51
# @Runtime: 96 ms
# @Memory: N/A

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)-1
        p=1
        ans=[]
        for num in nums:
            ans.append(p)
            p*=num
        p=1
        for i,num in enumerate(nums[::-1]):
            ans[l-i]*=p
            p*=num
        return ans
