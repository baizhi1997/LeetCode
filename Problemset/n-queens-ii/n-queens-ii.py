
# @Title: N皇后 II (N-Queens II)
# @Author: qinxinlei
# @Date: 2019-05-04 21:03:14
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        def dfs(queens, xydif, xysum):
            p = len(queens)
            if n == p:
                self.ans += 1
                return
            for i in range(n):
                if i not in queens and i - p not in xydif and i + p not in xysum:
                    dfs(queens + [i], xydif + [i - p], xysum + [i + p])
        dfs([], [], [])
        return self.ans
