
# @Title: 递减元素使数组呈锯齿状 (Decrease Elements To Make Array Zigzag)
# @Author: qinxinlei
# @Date: 2019-08-05 20:58:37
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        nums = [max(nums[0], nums[1]) + 1] + nums +[max(nums[-1], nums[-2]) + 1]
        moves = [max(0, nums[i] - min(nums[i-1], nums[i+1]) + 1) for i in range(1, len(nums)-1)]
        return min(sum(moves[::2]), sum(moves[1::2]))
