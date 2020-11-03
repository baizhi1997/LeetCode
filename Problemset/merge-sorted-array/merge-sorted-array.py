
# @Title: 合并两个有序数组 (Merge Sorted Array)
# @Author: qinxinlei
# @Date: 2018-09-28 16:01:02
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m and n:
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
        if not m:
            nums1[:n]=nums2[:n]
