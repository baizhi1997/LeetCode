
# @Title: 矩阵中的路径 (矩阵中的路径  LCOF)
# @Author: qinxinlei
# @Date: 2020-07-03 14:44:15
# @Runtime: 292 ms
# @Memory: 14.4 MB

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,k):
            if k==len(word):
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[k]!=board[i][j]:
                return False
            board[i][j]=''
            ans=dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
            board[i][j]=word[k]
            return ans
        if not word:
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
