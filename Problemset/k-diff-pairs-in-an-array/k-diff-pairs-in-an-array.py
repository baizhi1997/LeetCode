
# @Title: 数组中的 k-diff 数对 (K-diff Pairs in an Array)
# @Author: qinxinlei
# @Date: 2018-11-05 17:25:59
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<0:
            return 0
        dic=collections.Counter(nums)
        if k==0:
            return sum(v>1 for v in dic.values())
        ans=0
        for i in dic:
            if i+k in dic:
                ans+=1
        return ans
