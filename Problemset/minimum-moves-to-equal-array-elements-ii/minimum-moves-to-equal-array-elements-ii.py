
# @Title: 最少移动次数使数组元素相等 II (Minimum Moves to Equal Array Elements II)
# @Author: qinxinlei
# @Date: 2018-11-23 20:00:28
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        k=len(nums)//2
        m=nums[k]
        ans=0
        for num in nums[:k]:
            ans+=(m-num)
        for num in nums[k+1:]:
            ans+=(num-m)
        return ans
