
# @Title: 拥有最多糖果的孩子 (Kids With the Greatest Number of Candies)
# @Author: qinxinlei
# @Date: 2020-06-15 20:47:04
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        tmp = max(candies)
        return [x+extraCandies>=tmp for x in candies]
