
# @Title: 最小差 (Smallest Difference LCCI)
# @Author: qinxinlei
# @Date: 2020-07-17 10:48:27
# @Runtime: 240 ms
# @Memory: 19.2 MB

class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        i, j = 0, 0
        la, lb = len(a), len(b)
        ans = float('inf')
        while i < la and j < lb:
            x, y = a[i], b[j]
            if x < y:
                ans = min(ans, y-x)
                i += 1
            elif y < x:
                ans = min(ans, x-y)
                j += 1
            else:
                return 0
        return ans
