
# @Title: 最小面积矩形 (Minimum Area Rectangle)
# @Author: qinxinlei
# @Date: 2018-12-04 13:19:03
# @Runtime: 108 ms
# @Memory: N/A

class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        nx=len(set(x for x,y in points))
        ny=len(set(y for x,y in points))
        if nx==len(points) or ny==len(points):
            return 0
        hashSet=collections.defaultdict(list)
        if nx>ny:
            for x,y in points:
                hashSet[x].append(y)
        else:
            for x,y in points:
                hashSet[y].append(x)
        res=float('Inf')
        lastx={}
        for x in sorted(hashSet):
            hashSet[x].sort()
            for m in range(len(hashSet[x])-1):
                for n in range(m+1,len(hashSet[x])):
                    y1,y2=hashSet[x][m],hashSet[x][n]
                    if (y1,y2) in lastx:
                        res=min(res,(x-lastx[y1,y2])*(y2-y1))
                    lastx[y1,y2]=x
        return res if res<float('inf') else 0
