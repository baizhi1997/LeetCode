
# @Title: 最接近的三数之和 (3Sum Closest)
# @Author: qinxinlei
# @Date: 2018-09-21 15:32:46
# @Runtime: 56 ms
# @Memory: N/A

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len1=len(nums)
        ans=0
        nums.sort()
        for i in range (len1-2):
            if i and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len1-1
            while(l<r):
                dis=nums[i]+nums[l]+nums[r]-target
                if ans==0 or (abs(ans)>abs(dis)):
                    ans=dis
                if dis==0:
                    return target
                elif dis>0:
                    r-=1
                else:
                    l+=1
        return ans+target              
                    
