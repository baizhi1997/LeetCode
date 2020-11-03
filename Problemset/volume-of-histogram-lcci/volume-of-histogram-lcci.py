
# @Title: 直方图的水量 (Volume of Histogram LCCI)
# @Author: qinxinlei
# @Date: 2020-07-19 14:51:11
# @Runtime: 44 ms
# @Memory: 13.8 MB

class Solution:
    def trap(self, height: List[int]) -> int:
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
