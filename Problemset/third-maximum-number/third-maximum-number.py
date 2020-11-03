
# @Title: 第三大的数 (Third Maximum Number)
# @Author: qinxinlei
# @Date: 2018-10-10 20:48:43
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[float('-inf'),float('-inf'),float('-inf')]
        for num in nums:
            if num not in ans:
                if num>ans[0]:
                    ans=[num,ans[0],ans[1]]
                elif num>ans[1]:
                    ans[1:]=[num,ans[1]]
                elif num>ans[2]:
                    ans[2]=num
        return ans[2] if ans[2]!=float('-inf') else ans[0]
