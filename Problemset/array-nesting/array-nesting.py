
# @Title: 数组嵌套 (Array Nesting)
# @Author: qinxinlei
# @Date: 2018-12-13 11:54:24
# @Runtime: 72 ms
# @Memory: N/A

class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        set1=set()
        for n in nums:
            if n in set1:
                continue
            tmp=0
            while n not in set1:
                set1.add(n)
                n=nums[n]
                tmp+=1
            ans=max(tmp,ans)
        return ans
