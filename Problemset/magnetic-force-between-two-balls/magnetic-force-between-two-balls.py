
# @Title: 两球之间的磁力 (Magnetic Force Between Two Balls)
# @Author: qinxinlei
# @Date: 2020-08-17 16:30:50
# @Runtime: 1088 ms
# @Memory: 23.8 MB

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def check(x):
            cnt = 1
            t = position[0]
            for i in range(1, len(position)):
                if position[i]-t > x:
                    cnt += 1
                    t = position[i]
            return cnt >= m
        
        l, r = 0, position[-1]
        while l < r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid+1
            else:
                r = mid
        return l

