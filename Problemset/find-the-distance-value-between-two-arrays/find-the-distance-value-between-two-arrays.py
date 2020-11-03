
# @Title: 两个数组间的距离值 (Find the Distance Value Between Two Arrays)
# @Author: qinxinlei
# @Date: 2020-07-29 12:40:17
# @Runtime: 44 ms
# @Memory: 13.2 MB

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        cnt = 0
        for x in arr1:
            p = bisect.bisect_left(arr2, x)
            if p == len(arr2) or abs(x - arr2[p]) > d:
                if p == 0 or abs(x - arr2[p - 1]) > d:
                    cnt += 1
        return cnt

