
# @Title: 迷路的机器人 (Robot in a Grid LCCI)
# @Author: qinxinlei
# @Date: 2020-07-17 16:43:12
# @Runtime: 64 ms
# @Memory: 13.8 MB

class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        ans, r, c = [], len(obstacleGrid), len(obstacleGrid[0])
        def f(path):
            if not ans:
                i, j = path[-1]
                if not obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 1
                    i < r - 1 and f(path + [[i + 1, j]])
                    j < c - 1 and f(path + [[i, j + 1]])
                    if (i, j) == (r - 1, c - 1):
                        ans.extend(path)
        f([[0, 0]])
        return ans

