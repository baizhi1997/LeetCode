
# @Title: 圆形赛道上经过次数最多的扇区 (Most Visited Sector in  a Circular Track)
# @Author: qinxinlei
# @Date: 2020-10-28 22:43:03
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start, end = rounds[0], rounds[-1]
        if start <= end:
            return list(range(start, end + 1))
        else:
            leftPart = range(1, end + 1)
            rightPart = range(start, n + 1)
            return list(itertools.chain(leftPart, rightPart))

