
# @Title: 单词搜索 (Word Search)
# @Author: qinxinlei
# @Date: 2018-09-29 13:03:37
# @Runtime: 180 ms
# @Memory: N/A

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
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
