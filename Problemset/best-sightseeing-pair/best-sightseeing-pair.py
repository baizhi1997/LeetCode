
# @Title: 最佳观光组合 (Best Sightseeing Pair)
# @Author: qinxinlei
# @Date: 2020-06-17 20:08:14
# @Runtime: 628 ms
# @Memory: 18.3 MB

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        maxscore = 0
        ans = 0
        for i in range(len(A)-1):
            if A[i] + i > maxscore:
                maxscore = A[i] + i
            ans = max(ans, maxscore + A[i+1] - i - 1)
        return ans

