
# @Title: 和为目标值的最大数目不重叠非空子数组数目 (Maximum Number of Non-Overlapping Subarrays With Sum Equals Target)
# @Author: qinxinlei
# @Date: 2020-08-10 17:37:24
# @Runtime: 140 ms
# @Memory: 20 MB

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        s,sums,ans={0},0,0
        for num in nums:
            sums+=num            
            if sums-target in s:
                ans+=1
                s,sums={0},0
            else:
                s.add(sums)
        return ans

