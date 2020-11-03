
# @Title: 两数之和 II - 输入有序数组 (Two Sum II - Input array is sorted)
# @Author: qinxinlei
# @Date: 2018-10-14 12:37:23
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        r=len(numbers)-1
        l=0
        while l<r:
            t=numbers[l]+numbers[r]-target
            if t>0:
                r-=1
            elif t<0:
                l+=1
            else:
                return [l+1,r+1] 
