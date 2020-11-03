
# @Title: 有效的回旋镖 (Valid Boomerang)
# @Author: qinxinlei
# @Date: 2019-05-19 21:41:50
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def isBoomerang(self, p: List[List[int]]) -> bool:
        return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1])
