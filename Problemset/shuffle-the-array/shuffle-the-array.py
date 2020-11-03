
# @Title: 重新排列数组 (Shuffle the Array)
# @Author: qinxinlei
# @Date: 2020-07-28 12:11:17
# @Runtime: 40 ms
# @Memory: 13.2 MB

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * 2*n
        ans[::2] = nums[:n]
        ans[1::2] = nums[n:]
        return ans
