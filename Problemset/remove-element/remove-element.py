
# @Title: 移除元素 (Remove Element)
# @Author: qinxinlei
# @Date: 2018-09-23 20:43:52
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        n=len(nums)
        while i<n:
            if (nums[i]==val):
                nums[i]=nums[n-1]
                n-=1
            else:
                i+=1
        return n
