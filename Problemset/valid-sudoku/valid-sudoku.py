
# @Title: 有效的数独 (Valid Sudoku)
# @Author: qinxinlei
# @Date: 2018-12-04 13:12:43
# @Runtime: 84 ms
# @Memory: N/A

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        x,y,z=[""]*9,[""]*9,[""]*9
        for i in range(9):
            for j in range(9):
                c=board[i][j]
                if c!='.':
                    x[i]+=c
                    y[j]+=c
                    z[i//3+j//3*3]+=c
        return all(len(s)==len(set(s)) for s in x) and all(len(s)==len(set(s)) for s in y) and all(len(s)==len(set(s)) for s in z)
