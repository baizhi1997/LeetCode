
# @Title: 在排序数组中查找元素的第一个和最后一个位置 (Find First and Last Position of Element in Sorted Array)
# @Author: qinxinlei
# @Date: 2018-09-22 14:42:55
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(nums)-1
        ans=-1
        while l<=r:
            m=(l+r)/2
            if nums[m]==target:
                ans=m
                break
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        if ans==-1:
            return [-1,-1]
        else:
            ans1=ans
            ans2=ans
            while ans1 and nums[ans1]==nums[ans1-1]:
                ans1-=1
            while ans2<len(nums)-1 and nums[ans2]==nums[ans2+1]:
                ans2+=1
            return [ans1,ans2]

