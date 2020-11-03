
# @Title: 最长和谐子序列 (Longest Harmonious Subsequence)
# @Author: qinxinlei
# @Date: 2018-11-06 14:16:21
# @Runtime: 92 ms
# @Memory: N/A

class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic=collections.Counter(nums)
        return max([dic[i]+dic[i+1] for i in dic if i+1 in dic]+[0])
