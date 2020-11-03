
# @Title: 四数之和 (4Sum)
# @Author: qinxinlei
# @Date: 2018-09-21 16:41:27
# @Runtime: 140 ms
# @Memory: N/A

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l0=len(nums)
        if l0 < 4:
            return []
        nums.sort()
        if 4*nums[l0-1]<target:
            return []
        ans=[]
        for i in range(l0-3):
            if i and nums[i]==nums[i-1]:
                continue
            if 4*nums[i]>target:
                break
            for j in range (i+1,l0-2):
                if j-i-1 and nums[j]==nums[j-1]:
                    continue
                r=l0-1
                l=j+1
                while r>l:
                    curr_sum=nums[i]+nums[j]+nums[l]+nums[r]
                    if curr_sum>target:
                        r-=1
                    elif curr_sum<target:
                        l+=1
                    else:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        while l<l0-1 and nums[l]==nums[l+1]:
                            l+=1
                        while r>0 and nums[r]==nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
        return ans

