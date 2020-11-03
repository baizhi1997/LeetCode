
# @Title: 腐烂的橘子 (Rotting Oranges)
# @Author: qinxinlei
# @Date: 2019-03-05 11:21:33
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
        ans=0
        while q:
            tmp=[]
            for x,y in q:
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    a,b=x+dx,y+dy
                    if 0<=a<len(grid) and 0<=b<len(grid[0]) and grid[a][b]==1:
                        grid[a][b]=2
                        tmp.append((a,b))
            q=tmp
            if q:
                ans+=1
        if any(1 in row for row in grid):
            return -1
        return ans
