
# @Title: 你可以获得的最大硬币数目 (Maximum Number of Coins You Can Get)
# @Author: qinxinlei
# @Date: 2020-08-24 16:28:55
# @Runtime: 140 ms
# @Memory: 22.7 MB

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        l = len(piles)
        piles.sort(reverse=True)
        return sum(piles[1:l//3*2:2])

