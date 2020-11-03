
# @Title: 八皇后 (Eight Queens LCCI)
# @Author: qinxinlei
# @Date: 2020-07-19 21:11:10
# @Runtime: 64 ms
# @Memory: 13.5 MB

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        st = [['.' for i in range(n)] for j in range(n)]
        res = []
        def dfs(x_d, y_d, cur):
            j = len(cur)
            if len(cur) == n:
                m = []
                for i in st: m.append(''.join(i))
                res.append(m)
            for i in range(n):
                if i not in cur and i + j not in x_d and i-j not in y_d:
                    st[j][i] = 'Q'
                    dfs(x_d+[i+j],y_d+[i-j],cur+[i])
                    st[j][i] = '.'
        dfs([], [], [])
        return res

