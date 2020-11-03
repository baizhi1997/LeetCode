
# @Title: 换酒问题 (Water Bottles)
# @Author: qinxinlei
# @Date: 2020-07-29 15:53:36
# @Runtime: 40 ms
# @Memory: 13.3 MB

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottle, ans = numBottles, numBottles
        while bottle >= numExchange:
            bottle -= numExchange
            ans += 1
            bottle += 1
        return ans

