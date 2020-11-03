
# @Title: 到最近的人的最大距离 (Maximize Distance to Closest Person)
# @Author: qinxinlei
# @Date: 2018-11-17 16:45:36
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        l=len(seats)
        tmp=[i for i in range(l) if seats[i]]
        tmp=[-tmp[0]]+tmp+[2*(l-1)-tmp[-1]]
        return max((tmp[i+1]-tmp[i])//2 for i in range(len(tmp)-1))
