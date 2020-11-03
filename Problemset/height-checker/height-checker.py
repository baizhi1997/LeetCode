
# @Title: 高度检查器 (Height Checker)
# @Author: qinxinlei
# @Date: 2019-06-24 16:57:21
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(x!=y for (x, y) in zip(heights, sorted(heights)))
