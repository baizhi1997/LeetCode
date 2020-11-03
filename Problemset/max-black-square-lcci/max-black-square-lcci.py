
# @Title: 最大黑方阵 (Max Black Square LCCI)
# @Author: qinxinlei
# @Date: 2020-07-19 13:57:22
# @Runtime: 228 ms
# @Memory: 14.3 MB

class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m,n = len(matrix),len(matrix[0])
        dp0 = [[0]*n for _ in range(m)]
        dp1 = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp0[i][j] = dp0[i][j-1]+1 if j>0 else 1
                    dp1[i][j] = dp1[i-1][j]+1 if i>0 else 1
                    w = min(dp0[i][j],dp1[i][j])
                    for k in range(w,0,-1):
                        if dp1[i][j-k+1]>=k and dp0[i-k+1][j]>=k:
                            if not ans or ans[-1]<k:
                                ans = [i-k+1,j-k+1,k]
                            break
        return ans

