
# @Title: 玩筹码 (Minimum Cost to Move Chips to The Same Position)
# @Author: qinxinlei
# @Date: 2020-07-31 13:47:59
# @Runtime: 48 ms
# @Memory: 13.3 MB

class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        x = sum(i & 1 for i in chips)
        return min(x, len(chips)-x)
