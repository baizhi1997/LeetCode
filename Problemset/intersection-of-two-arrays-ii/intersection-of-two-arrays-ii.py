
# @Title: 两个数组的交集 II (Intersection of Two Arrays II)
# @Author: qinxinlei
# @Date: 2018-10-25 17:13:20
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic=collections.Counter(nums1)&collections.Counter(nums2)
        return [x for i in dic for x in [i]*dic[i]]
