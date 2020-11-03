
# @Title: 分发糖果 (Candy)
# @Author: qinxinlei
# @Date: 2019-05-13 15:53:57
# @Runtime: 68 ms
# @Memory: N/A

class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                ans[i] = ans[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if  ratings[i] > ratings[i + 1]:
                ans[i] = max(ans[i], ans[i + 1] + 1)
        return sum(ans)
