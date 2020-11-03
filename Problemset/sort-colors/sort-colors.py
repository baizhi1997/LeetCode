
# @Title: 颜色分类 (Sort Colors)
# @Author: qinxinlei
# @Date: 2018-09-27 13:39:07
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)-1
        k=0
        while k<=j:
            if nums[k]==0 and k!=i:
                nums[k],nums[i]=nums[i],nums[k]
                i+=1
            elif nums[k]==2:
                nums[k],nums[j]=nums[j],nums[k]
                j-=1
            else:
                k+=1

