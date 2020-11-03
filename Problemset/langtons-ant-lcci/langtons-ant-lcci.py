
# @Title: 兰顿蚂蚁 (Langtons Ant LCCI)
# @Author: qinxinlei
# @Date: 2020-07-13 16:27:55
# @Runtime: 2620 ms
# @Memory: 554.8 MB

class Solution:
    def printKMoves(self, K: int) -> List[str]:
        R,T,L,D = 0,0,0,0
        def move_ant(ant) :
            nonlocal R,T,L,D
            y, x = ant[0]
            if ant[1] == 0 : ant[0] = (y, x+1)
            if ant[1] == 1 : ant[0] = (y+1, x)
            if ant[1] == 2 : ant[0] = (y, x-1)
            if ant[1] == 3 : ant[0] = (y-1, x)
            y, x = ant[0]
            R,T,L,D = max(R,x), min(T,y), min(L,x), max(D,y)

        ant = [(0,0),0] # 0-R 1-D 2-L 3-U
        grids = collections.defaultdict(lambda : '_')
        for _ in range(K) :
            if grids[ant[0]] == 'X' : # black
                ant[1] = (ant[1]+3)%4
                grids[ant[0]] = '_'
            else : # white
                ant[1] = (ant[1]+1)%4
                grids[ant[0]] = 'X'
            move_ant(ant)
    
        grids[ant[0]] = ['R','D','L','U'][ant[1]]
        return [''.join([grids[(y,x)] for x in range(L,R+1)]) for y in range(T,D+1)]

