
# @Title: 所有蚂蚁掉下来前的最后一刻 (Last Moment Before All Ants Fall Out of a Plank)
# @Author: qinxinlei
# @Date: 2020-07-05 11:22:15
# @Runtime: 60 ms
# @Memory: 14 MB

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not left:
            return n - min(right)
        if not right:
            return max(left)
        x, y = min(right), max(left)
        return max(y, n-x)
