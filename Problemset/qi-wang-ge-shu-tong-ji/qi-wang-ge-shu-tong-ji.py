
# @Title: 期望个数统计 (期望个数统计)
# @Author: qinxinlei
# @Date: 2020-07-24 10:32:52
# @Runtime: 84 ms
# @Memory: 25.8 MB

class Solution:
    def expectNumber(self, scores: List[int]) -> int:
        return len(set(scores))
