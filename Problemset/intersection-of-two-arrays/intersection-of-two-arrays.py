
# @Title: 两个数组的交集 (Intersection of Two Arrays)
# @Author: qinxinlei
# @Date: 2018-10-11 21:38:17
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1)&set(nums2))
