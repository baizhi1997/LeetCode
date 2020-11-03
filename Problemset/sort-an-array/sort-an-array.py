
# @Title: 排序数组 (Sort an Array)
# @Author: qinxinlei
# @Date: 2019-09-01 22:42:47
# @Runtime: 196 ms
# @Memory: N/A

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        arr = [0] * 100001
        for n in nums:
            arr[n + 50000] += 1
        ans = []
        for i in range(100001):
            if arr[i]:
                ans += [i - 50000] * arr[i]
        return ans
