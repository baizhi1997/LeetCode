
# @Title: 接雨水 (Trapping Rain Water)
# @Author: qinxinlei
# @Date: 2018-09-23 16:26:09
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        lmax,rmax=0,0
        water=0
        while l<r:
            if height[l]<height[r]:
                if height[l]>lmax:
                    lmax=height[l]
                else:
                    water+=lmax-height[l]
                l+=1
            else:
                if height[r]>rmax:
                    rmax=height[r]
                else:
                    water+=rmax-height[r]
                r-=1
        return water

