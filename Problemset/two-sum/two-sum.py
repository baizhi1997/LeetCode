
# @Title: 两数之和 (Two Sum)
# @Author: qinxinlei
# @Date: 2018-11-05 20:23:25
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i,num in enumerate(nums):
            if num in dic:
                return [dic[num],i]
            dic[target-num]=i
