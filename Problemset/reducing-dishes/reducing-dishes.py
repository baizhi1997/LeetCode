
# @Title: 做菜顺序 (Reducing Dishes)
# @Author: qinxinlei
# @Date: 2020-07-29 12:26:17
# @Runtime: 52 ms
# @Memory: 13.4 MB

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        presum, ans = 0, 0
        for si in satisfaction:
            if presum + si > 0:
                presum += si
                ans += presum
            else:
                break
        return ans

