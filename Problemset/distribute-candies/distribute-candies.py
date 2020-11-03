
# @Title: 分糖果 (Distribute Candies)
# @Author: qinxinlei
# @Date: 2018-10-20 13:02:33
# @Runtime: 120 ms
# @Memory: N/A

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)),len(candies)//2)
es)/2)
