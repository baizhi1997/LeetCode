
# @Title: 有效三角形的个数 (Valid Triangle Number)
# @Author: qinxinlei
# @Date: 2018-10-08 11:28:54
# @Runtime: 136 ms
# @Memory: N/A

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans=0
        i=len(nums)-1 
        while i>1:
            r=i-1
            l=0
            while l<r:
                if nums[l]+nums[r]>nums[i]:
                    ans+=r-l
                    r-=1
                else:
                    l+=1
            i-=1          
        return ans
