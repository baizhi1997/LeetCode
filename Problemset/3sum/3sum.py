
# @Title: 三数之和 (3Sum)
# @Author: qinxinlei
# @Date: 2018-09-21 16:40:29
# @Runtime: 600 ms
# @Memory: N/A

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len1=len(nums)
        if len1<3:
            return []
        ans=[]
        nums.sort()
        if nums[len1-1]<0:
            return []
        for i in range(len1-2):
            if i and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            r=len1-1
            l=i+1
            while r>l:
                curr_sum=nums[r]+nums[l]+nums[i]
                if curr_sum>0:
                    r-=1
                elif curr_sum<0:
                    l+=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l<len1-1 and nums[l]==nums[l+1]:
                        l+=1
                    while r>0 and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return ans
