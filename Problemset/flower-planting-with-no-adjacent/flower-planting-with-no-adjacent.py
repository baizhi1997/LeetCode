
# @Title: 不邻接植花 (Flower Planting With No Adjacent)
# @Author: qinxinlei
# @Date: 2019-06-24 18:31:08
# @Runtime: 184 ms
# @Memory: N/A

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [0] * N
        G = [[] for i in range(N)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
        return res
