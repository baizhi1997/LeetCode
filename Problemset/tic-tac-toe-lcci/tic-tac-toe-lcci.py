
# @Title: 井字游戏 (Tic-Tac-Toe LCCI)
# @Author: qinxinlei
# @Date: 2020-07-15 22:46:22
# @Runtime: 44 ms
# @Memory: 13.3 MB

class Solution:
    def tictactoe(self, board: List[str]) -> str:
        n = len(board)
        def check(c):
            s = c * n
            return any((
                any(row == s for row in board),
                any(col == s for col in map(''.join, zip(*board))),
                all(board[i][i] == c for i in range(n)),
                all(board[i][n - i - 1] == c for i in range(n))
            ))
        if check('X'):
            return 'X'
        if check('O'):
            return 'O'
        if ' ' in ''.join(board):
            return 'Pending'
        return 'Draw'

