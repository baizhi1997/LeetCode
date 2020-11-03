
# @Title: 水域大小 (Pond Sizes LCCI)
# @Author: qinxinlei
# @Date: 2020-07-13 16:03:32
# @Runtime: 328 ms
# @Memory: 18.4 MB

class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        def dfs(i, j):
            if land[i][j] != 0:
                return
            self.cnt += 1
            land[i][j] = 1
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if 0 <= i+x < m and 0 <= j+y < n:
                        dfs(i+x, j+y)

        
        self.cnt = 0
        ans = []
        m, n = len(land), len(land[0])
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    dfs(i, j)
                    ans.append(self.cnt)
                    self.cnt = 0
        return sorted(ans)
