
# @Title: 砖墙 (Brick Wall)
# @Author: qinxinlei
# @Date: 2018-12-02 17:07:34
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        dic=collections.defaultdict(int)
        k=dic[0]=0
        for w in wall:
            k=0
            for i in w[:-1]:
                k+=i
                dic[k]+=1
        return len(wall)-max(dic.values())
