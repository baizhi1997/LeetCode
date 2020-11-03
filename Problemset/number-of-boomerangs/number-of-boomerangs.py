
# @Title: 回旋镖的数量 (Number of Boomerangs)
# @Author: qinxinlei
# @Date: 2018-11-18 22:26:03
# @Runtime: 596 ms
# @Memory: N/A

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans=0
        for x1,y1 in points:
            dic={}
            for x2,y2 in points:
                dx=x1-x2
                dy=y1-y2
                d=dx*dx+dy*dy
                if d in dic:
                    ans+=dic[d]
                    dic[d]+=1
                else:
                    dic[d]=1
        return 2*ans
