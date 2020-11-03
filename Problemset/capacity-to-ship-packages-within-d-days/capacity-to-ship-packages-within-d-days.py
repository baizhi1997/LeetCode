
# @Title: 在 D 天内送达包裹的能力 (Capacity To Ship Packages Within D Days)
# @Author: qinxinlei
# @Date: 2019-03-18 10:03:05
# @Runtime: 296 ms
# @Memory: N/A

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def solve(weights,x):
            days=1
            tmp=x
            for w in weights:
                if tmp>=w:
                    tmp-=w
                else:
                    tmp=x-w
                    days+=1
            return days
        l=max(weights)
        r=sum(weights)
        while l<r:
            m=(l+r)//2
            if solve(weights,m)<=D:
                r=m
            else:
                l=m+1
        return l
