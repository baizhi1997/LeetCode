
# @Title: 移动石子直到连续 (Moving Stones Until Consecutive)
# @Author: qinxinlei
# @Date: 2019-05-19 21:26:48
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x = max(a, b, c) - min(a, b, c) - 2
        y = 1 if abs(a - b) < 3 or abs(b -c) < 3 or abs(c - a) < 3 else 2
        if x == 0 : y = 0
        return [y, x]
