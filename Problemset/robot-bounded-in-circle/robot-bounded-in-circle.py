
# @Title: 困于环中的机器人 (Robot Bounded In Circle)
# @Author: qinxinlei
# @Date: 2019-05-19 19:58:17
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        print(dirs)
        x, y = 0, 0
        d = 0
        for i in instructions * 4:
            if i == 'L':
                d = (d - 1) % 4
            elif i == 'R':
                d = (d + 1) % 4
            else:
                x += dirs[d][0]
                y += dirs[d][1]
        if x == 0 and y == 0:
            return True
        else:
            return False
