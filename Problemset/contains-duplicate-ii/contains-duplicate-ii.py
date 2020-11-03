
# @Title: 存在重复元素 II (Contains Duplicate II)
# @Author: qinxinlei
# @Date: 2018-10-23 17:07:35
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic={}
        for i,n in enumerate(nums):
            if n in dic and i-dic[n]<=k:
                return True
            dic[n]=i
        return False
