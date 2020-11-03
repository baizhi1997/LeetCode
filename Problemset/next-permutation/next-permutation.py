
# @Title: 下一个排列 (Next Permutation)
# @Author: qinxinlei
# @Date: 2018-09-28 10:24:17
# @Runtime: 36 ms
# @Memory: N/A

class Solution(object):
    def nextPermutation(self, nums):
        l=len(nums)
        i=l-1
        j=l-1
        while i and nums[i]<=nums[i-1]:
            i-=1
        if i==0:
            nums[i:] = nums[i:][::-1]
        else:
            while nums[j]<=nums[i-1]:
                j-=1
            nums[j],nums[i-1]=nums[i-1],nums[j]
            nums[i:]=nums[i:][::-1]

