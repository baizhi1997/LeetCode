
# @Title: 区域和检索 - 数组不可变 (Range Sum Query - Immutable)
# @Author: qinxinlei
# @Date: 2018-11-13 13:03:35
# @Runtime: 68 ms
# @Memory: N/A

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.list=[0]
        for i in range(len(nums)):
            self.list.append(self.list[-1]+nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.list[j+1]-self.list[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
