
# @Title: 寻找数组的中心索引 (Find Pivot Index)
# @Author: qinxinlei
# @Date: 2018-11-06 16:24:33
# @Runtime: 68 ms
# @Memory: N/A

class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        x=sum(nums)
        for i,num in enumerate(nums):
            x-=num
            if x==0:
                return i
            x-=num
        return -1
