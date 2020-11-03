
# @Title: 盛最多水的容器 (Container With Most Water)
# @Author: qinxinlei
# @Date: 2018-09-21 19:08:39
# @Runtime: 52 ms
# @Memory: N/A

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        ans=-1
        while l<r:
            ans=max(ans,(r-l)*min(height[l],height[r]))
            if height[l]>height[r]:
                r-=1
            elif height[l]<height[r]:
                l+=1
            else:
                l+=1
                r-=1
        return ans

