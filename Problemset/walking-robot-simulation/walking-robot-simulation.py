
# @Title: 模拟行走机器人 (Walking Robot Simulation)
# @Author: qinxinlei
# @Date: 2018-11-17 20:11:37
# @Runtime: 120 ms
# @Memory: N/A

class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        ans=0
        x,y,d=0,0,0
        direc=[(0,1),(1,0),(0,-1),(-1,0)]
        obstacles=set(map(tuple,obstacles))
        for command in commands:
            if command==-1:
                d=(d+1)%4
            elif command==-2:
                d=(d-1)%4
            else:
                dx,dy=direc[d]
                for i in range(command):
                    if (x+dx,y+dy) in obstacles:
                        break
                    x+=dx
                    y+=dy
                ans=max(ans,x*x+y*y)
        return ans
