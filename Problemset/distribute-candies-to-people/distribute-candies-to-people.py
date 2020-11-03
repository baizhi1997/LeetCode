
# @Title: 分糖果 II (Distribute Candies to People)
# @Author: qinxinlei
# @Date: 2019-07-01 21:45:03
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        i = 0
        while candies > i:
            ans[i % num_people] += (i+1)
            candies -= (i+1)
            i += 1
        ans[i % num_people] += candies
        return ans
