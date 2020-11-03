
# @Title: 拿硬币 (拿硬币)
# @Author: qinxinlei
# @Date: 2020-07-24 10:01:57
# @Runtime: 48 ms
# @Memory: 13.4 MB

class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum((coin+1)//2 for coin in coins)
