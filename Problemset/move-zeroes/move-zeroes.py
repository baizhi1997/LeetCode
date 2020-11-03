
# @Title: 移动零 (Move Zeroes)
# @Author: qinxinlei
# @Date: 2018-10-22 14:46:02
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt=0
        for i in range(len(nums))[::-1]:
            if nums[i]==0:
                del nums[i]
                cnt+=1
        nums+=[0]*cnt
