
# @Title: 可以到达所有点的最少点数目 (Minimum Number of Vertices to Reach All Nodes)
# @Author: qinxinlei
# @Date: 2020-08-24 16:32:20
# @Runtime: 196 ms
# @Memory: 41.5 MB

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        set1, set2 = set(), set()
        for (x, y) in edges:
            set1.add(x)
            set2.add(y)
        set1 = set1 - set2
        return list(set1)
