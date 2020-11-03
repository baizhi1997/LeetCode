
# @Title: 前 K 个高频元素 (Top K Frequent Elements)
# @Author: qinxinlei
# @Date: 2018-12-02 21:13:17
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic=collections.Counter(nums)
        return heapq.nlargest(k,dic,key=lambda x:dic[x])
