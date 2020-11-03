
# @Title: 数组中的第K个最大元素 (Kth Largest Element in an Array)
# @Author: qinxinlei
# @Date: 2018-12-02 21:26:26
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res
