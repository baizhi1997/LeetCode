
# @Title: 下一个更大元素 II (Next Greater Element II)
# @Author: qinxinlei
# @Date: 2018-12-10 14:13:57
# @Runtime: 172 ms
# @Memory: N/A

class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        ans=[-1]*l
        stack=[]
        for i,n in enumerate(nums*2):
            while stack and nums[stack[-1]]<n:
                ans[stack.pop()]=n
            if i<l:
                stack.append(i)
        return ans
