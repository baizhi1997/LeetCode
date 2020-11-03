
# @Title: 至少是其他数字两倍的最大数 (Largest Number At Least Twice of Others)
# @Author: qinxinlei
# @Date: 2018-11-06 16:40:34
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1,x2=-math.inf,-math.inf
        ans=-1
        for i,num in enumerate(nums):
            if num>x1:
                x1,x2=num,x1
                ans=i
            elif num>x2:
                x2=num
        return ans if x1-x2*2>=0 else -1
