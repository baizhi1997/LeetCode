
# @Title: 可以被一步捕获的棋子数 (Available Captures for Rook)
# @Author: qinxinlei
# @Date: 2019-02-28 16:00:41
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        x0,y0=0,0
        for i in range(8):
            for j in range(8):
                if board[i][j]=='R':
                    x0,y0=i,j
        ans=0
        for i,j in [[1,0],[0,1],[-1,0],[0,-1]]:
            x,y=x0+i,y0+j
            while 0<=x<8 and 0<=y<8 and board[x][y]!='B':
                if board[x][y]=='p':
                    ans+=1
                    break
                x,y=x+i,y+j
        return ans
