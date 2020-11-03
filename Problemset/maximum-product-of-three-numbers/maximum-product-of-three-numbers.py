
# @Title: 三个数的最大乘积 (Maximum Product of Three Numbers)
# @Author: qinxinlei
# @Date: 2018-10-04 13:09:07
# @Runtime: 68 ms
# @Memory: N/A

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,s=heapq.nlargest(3,nums),heapq.nsmallest(2,nums)
        x,y=l[1]*l[2],s[0]*s[1]
        ans=max(x,y)*l[0]
        return ans
