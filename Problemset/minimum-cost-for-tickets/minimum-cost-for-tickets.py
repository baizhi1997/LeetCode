
# @Title: 最低票价 (Minimum Cost For Tickets)
# @Author: qinxinlei
# @Date: 2020-08-14 16:52:37
# @Runtime: 52 ms
# @Memory: 13.4 MB

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for _ in range(days[-1] + 1)]
        tmp = days.pop(0)
        days.append(0)
        for i in range(1, len(dp)):
            if i != tmp:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
                tmp = days.pop(0)
        return dp[-1]

