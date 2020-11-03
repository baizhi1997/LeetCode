
# @Title: 统计作战单位数 (Count Number of Teams)
# @Author: qinxinlei
# @Date: 2020-06-01 16:36:43
# @Runtime: 64 ms
# @Memory: 13.2 MB

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        for j in range(0, n):
            l, r = 0, 0
            for i in range(0, j):
                if rating[i] < rating[j]:
                    l += 1
            for k in range(j + 1, n):
                if rating[j] < rating[k]:
                    r += 1
            ans += (l * r) + (j - l) * (n - 1 - j - r)  
        return ans

