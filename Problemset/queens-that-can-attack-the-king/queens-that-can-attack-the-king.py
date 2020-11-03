
# @Title: 可以攻击国王的皇后 (Queens That Can Attack the King)
# @Author: qinxinlei
# @Date: 2020-06-22 23:32:02
# @Runtime: 56 ms
# @Memory: 13.4 MB

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        ans = []
        for d in directions:
            x, y = king[0], king[1]
            for _ in range(7):
                x = x + d[0]
                y = y + d[1]
                if x < 0 or x > 7 or y < 0 or y > 7:
                    break
                if [x, y] in queens:
                    ans.append([x, y])
                    break
        return ans
