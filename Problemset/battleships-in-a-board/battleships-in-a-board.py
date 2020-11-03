
# @Title: 甲板上的战舰 (Battleships in a Board)
# @Author: qinxinlei
# @Date: 2020-06-03 22:03:05
# @Runtime: 88 ms
# @Memory: 13.8 MB

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row = len(board)
        col = len(board[0])
        res =  0
        for i in range(row):
            for j in range(col):
                if board[i][j] == ".": continue
                if i > 0 and board[i - 1][j] == "X": continue
                if j > 0 and board[i][j - 1] == "X": continue
                res += 1
        return res
        
