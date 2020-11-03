
# @Title: 数组中两元素的最大乘积 (Maximum Product of Two Elements in an Array)
# @Author: qinxinlei
# @Date: 2020-07-28 15:11:15
# @Runtime: 40 ms
# @Memory: 13.2 MB

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        for num in nums:
            if num > max2:
                max2 = num
                if max2 > max1:
                    max1, max2 = max2, max1
        return (max1-1)*(max2-1)
