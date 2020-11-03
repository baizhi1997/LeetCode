
# @Title: 供暖器 (Heaters)
# @Author: qinxinlei
# @Date: 2018-11-04 21:07:36
# @Runtime: 104 ms
# @Memory: N/A

class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        ans=0
        heaters=[-math.inf]+sorted(heaters)+[math.inf]
        houses.sort()
        i=0
        for house in houses:
            while house>heaters[i]:
                i+=1
            ans=max(ans,min(heaters[i]-house,house-heaters[i-1]))
        return ans
