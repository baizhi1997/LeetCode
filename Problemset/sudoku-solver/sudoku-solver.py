
# @Title: 解数独 (Sudoku Solver)
# @Author: qinxinlei
# @Date: 2019-05-02 21:26:15
# @Runtime: 472 ms
# @Memory: N/A

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        stack = [(i, j) for i in range(9) for j in range(9) if board[i][j] == "."]
        def dfs():
            if not stack: return
            x, y = stack.pop()
            box = [board[x//3*3+i][y//3*3+j] for i in range(3) for j in range(3)]
            row = [board[x][j] for j in range(9)]
            col = [board[i][y] for i in range(9)]
            for i in "123456789":
                if not any([i in box, i in col, i in row]):
                    board[x][y] = i
                    dfs()
                    if not stack: return
            board[x][y] = "."
            stack.append((x, y))
        dfs()
