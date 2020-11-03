
# @Title: 统计好三元组 (Count Good Triplets)
# @Author: qinxinlei
# @Date: 2020-08-02 15:52:30
# @Runtime: 616 ms
# @Memory: 13.4 MB

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        for x, y, z in itertools.combinations(arr, 3):
            if abs(x-y) <= a and abs(y-z) <= b and abs(x-z) <= c:
                ans += 1
        return ans
