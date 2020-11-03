
# @Title: 多数元素 (Majority Element)
# @Author: qinxinlei
# @Date: 2018-10-08 17:22:33
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        ans=0
        for n in nums:
            if i==0:
                ans=n
            if n==ans:
                i+=1
            else:
                i-=1
        return ans
